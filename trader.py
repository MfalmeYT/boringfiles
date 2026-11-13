"""Multi-market trading framework (paper by default).

One script, one config per market (see MARKETS below). Every run it loops over the enabled markets:
  1. skips markets that are closed (currency pairs close on weekends, the gold ETF outside US stock hours)
  2. scores the market with the same 3 checks (EMA trend, longer EMA, RSI)
  3. asks Gemini for a 1-6 confidence on entries, once per cooldown
  4. places orders through a broker adapter (Alpaca for Bitcoin and gold PAXG, OANDA for currency pairs)
  5. currency pairs can go LONG (bet on up) or SHORT (bet on down) with mirrored rules. Alpaca can't short crypto, so
     Bitcoin and Gold stay long-only.

Safety rails (apply to ALL markets):
  - TRADING_ENABLED=false  -> never places orders (kill switch)
  - MAX_OPEN_POSITIONS     -> never holds more than this many positions across all markets
  - live accounts are locked unless ALLOW_LIVE=yes
  - currency pairs: server-side stop loss + take profit on the broker, spread filter,
    no new entries near the weekend, positions closed before the weekend
"""
import datetime
import json
import os
import sys
import time
from zoneinfo import ZoneInfo

import requests

# ---------------------------------------------------------------- settings
GEMINI_KEY = os.environ.get("GEMINI_KEY", "")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")
# An empty or missing value means "enabled". Only an explicit false/0/no/off turns trading off.
TRADING_ENABLED = os.environ.get("TRADING_ENABLED", "").strip().lower() not in ("false", "0", "no", "off")
MAX_OPEN_POSITIONS = int(os.environ.get("MAX_OPEN_POSITIONS") or 3)
# Same idea for shorting: only an explicit false/0/no/off stops NEW short trades (open ones are still managed).
SHORTING_ENABLED = os.environ.get("SHORTING_ENABLED", "").strip().lower() not in ("false", "0", "no", "off")

EMA_FAST, EMA_SLOW, EMA_TREND = 9, 21, 50
RSI_PERIOD, RSI_LOW, RSI_HIGH = 14, 45, 70
ATR_PERIOD = 14
CROSS_LOOKBACK = 3
MIN_ENTRY_SCORE = 2      # need at least 2 of 3 checks to ask Gemini
EXIT_SCORE = 0           # signal exit only when all 3 checks fail
MIN_HOLD_MIN = 30        # no signal exit in the first 30 min after a buy (stops/targets still apply)
REENTRY_COOLDOWN_MIN = 60  # no new buy within 60 min after any sell (stops in-and-out churn)
REQUIRE_FAST_ABOVE_SLOW = True  # never enter while the fast EMA is below the slow EMA
MIN_CONFIDENCE = 3       # Gemini confidence (1-6) needed to buy
MIN_TRADE_USD = 10       # crypto: skip buying if cash is below this

def fx_pair(label, symbol, log, decimals, units=10000):
    """A currency pair on OANDA. units = amount of the FIRST currency per trade (10,000 on the practice account)."""
    return {
        "enabled": True, "label": label, "broker": "oanda", "symbol": symbol,
        "log": log, "session": "fx", "timeframe": "M15", "decimals": decimals,
        "cooldown_min": 15, "units": units,
        "min_hold_min": 90, "reentry_min": 180,
        "exit": {"mode": "atr", "stop_mult": 2.0, "tp_mult": 3.0},   # target 1.5x the stop, so spreads eat less of each win
        "min_confidence": 2,   # paper test: let more setups through, then compare results by confidence in the viewer
        "max_spread_frac": 0.25,
        "flatten_before_weekend": True,
        "allow_short": True,   # also trade DOWN moves (mirrored rules); set False to make this pair long-only
    }


MARKETS = {
    "btc": {
        "enabled": True, "label": "Bitcoin", "broker": "alpaca", "symbol": "BTC/USD",
        "log": "bot_log.csv", "session": "24/7", "timeframe": "5Min", "decimals": 2,
        "cooldown_min": 5, "size_usd": 45,   # Bitcoin and GLD share one Alpaca cash balance, so each uses a smaller slice
        "exit": {"mode": "pct", "stop": 0.02, "tp": 0.02},
    },
    # Gold, traded as PAXG/USD (a token backed by 1 oz of gold) on the same Alpaca paper account. Logged as "Gold USD".
    # PAXG trades thinly, so it uses 15-min candles and looks back 48h to find enough of them.
    "gold": {
        "enabled": True, "label": "Gold USD", "broker": "alpaca", "symbol": "PAXG/USD",
        "log": "bot_log_goldusd.csv", "session": "24/7", "timeframe": "15Min", "decimals": 2,
        "cooldown_min": 15, "size_usd": 45, "lookback_hours": 48,
        "min_hold_min": 90, "reentry_min": 180,
        "exit": {"mode": "pct", "stop": 0.01, "tp": 0.015},   # gold moves less than Bitcoin, so tighter than 2%
    },
    "usdjpy": fx_pair("USD/JPY", "USD_JPY", "bot_log_usdjpy.csv", decimals=3),
    "gbpusd": fx_pair("GBP/USD", "GBP_USD", "bot_log_gbpusd.csv", decimals=5),
    "eurusd": fx_pair("EUR/USD", "EUR_USD", "bot_log_eurusd.csv", decimals=5),
    "eurgbp": fx_pair("EUR/GBP", "EUR_GBP", "bot_log_eurgbp.csv", decimals=5),
}


# ---------------------------------------------------------------- indicators
def ema(values, period):
    k = 2 / (period + 1)
    out = [values[0]]
    for v in values[1:]:
        out.append(v * k + out[-1] * (1 - k))
    return out


def rsi(closes, period=14):
    gains, losses = [], []
    for i in range(1, len(closes)):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0))
        losses.append(max(-d, 0))
    avg_g = sum(gains[:period]) / period
    avg_l = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_g = (avg_g * (period - 1) + gains[i]) / period
        avg_l = (avg_l * (period - 1) + losses[i]) / period
    if avg_l == 0:
        return 100.0
    return 100 - 100 / (1 + avg_g / avg_l)


def atr(bars, period=14):
    trs = []
    for i in range(1, len(bars)):
        h, l, pc = bars[i]["h"], bars[i]["l"], bars[i - 1]["c"]
        trs.append(max(h - l, abs(h - pc), abs(l - pc)))
    a = sum(trs[:period]) / period
    for tr in trs[period:]:
        a = (a * (period - 1) + tr) / period
    return a


def compute_indicators(bars):
    closes = [b["c"] for b in bars]
    fast, slow, trend = ema(closes, EMA_FAST), ema(closes, EMA_SLOW), ema(closes, EMA_TREND)
    price = closes[-1]
    r = rsi(closes, RSI_PERIOD)
    fresh_cross = any(
        fast[i - 1] <= slow[i - 1] and fast[i] > slow[i]
        for i in range(len(closes) - CROSS_LOOKBACK, len(closes))
    )
    checks = {
        "fast_above_slow": fast[-1] > slow[-1],
        "price_above_trend_ema": price > trend[-1],
        "rsi_in_range": RSI_LOW <= r <= RSI_HIGH,
    }
    # Mirror image for shorts: fast below slow, price below the long EMA, RSI between 30 and 55
    fresh_cross_down = any(
        fast[i - 1] >= slow[i - 1] and fast[i] < slow[i]
        for i in range(len(closes) - CROSS_LOOKBACK, len(closes))
    )
    checks_short = {
        "fast_below_slow": fast[-1] < slow[-1],
        "price_below_trend_ema": price < trend[-1],
        "rsi_in_short_range": (100 - RSI_HIGH) <= r <= (100 - RSI_LOW),
    }
    return {
        "price": price, "ema_fast": fast[-1], "ema_slow": slow[-1], "ema_trend": trend[-1],
        "rsi": r, "atr": atr(bars, ATR_PERIOD), "fresh_cross": fresh_cross,
        "checks": checks, "score": sum(checks.values()),
        "fresh_cross_down": fresh_cross_down, "checks_short": checks_short, "score_short": sum(checks_short.values()),
    }


def exit_distances(cfg, price, atr_value):
    """Return (stop_distance, tp_distance) in price units."""
    ex = cfg["exit"]
    if ex["mode"] == "atr":
        return atr_value * ex["stop_mult"], atr_value * ex["tp_mult"]
    return price * ex["stop"], price * ex["tp"]


# ---------------------------------------------------------------- sessions
ET = ZoneInfo("America/New_York")


def session_state(session, now_utc):
    """Return (is_open, allow_new_entries, flatten_now)."""
    if session == "24/7":
        return True, True, False
    if session == "us_stocks":
        et = now_utc.astimezone(ET)
        wd, t = et.weekday(), et.hour * 60 + et.minute
        is_open = wd < 5 and 9 * 60 + 30 <= t < 16 * 60
        entries = is_open and 9 * 60 + 45 <= t < 15 * 60      # skip the first 15 min and the last hour
        flatten = is_open and t >= 15 * 60 + 45               # be flat before the close
        return is_open, entries, flatten
    et = now_utc.astimezone(ET)
    wd, t = et.weekday(), et.hour * 60 + et.minute      # Mon=0 ... Sun=6
    closed = (
        wd == 5                                  # Saturday
        or (wd == 4 and t >= 17 * 60)            # Friday after 17:00 ET
        or (wd == 6 and t < 18 * 60)             # Sunday before 18:00 ET
        or (wd in (0, 1, 2, 3) and 17 * 60 <= t < 18 * 60)  # daily break
    )
    no_entries = wd == 4 and t >= 16 * 60        # no new trades in the last hour before the weekend
    flatten = wd == 4 and t >= 16 * 60 + 30      # close positions in the last 30 minutes
    return (not closed), (not closed and not no_entries), (not closed and flatten)


# ---------------------------------------------------------------- brokers
def http_get(url, **kw):
    """GET with a few retries for temporary gateway errors (429/502/503/504) and dropped connections."""
    for wait in (1, 2, 4, None):
        try:
            r = requests.get(url, **kw)
        except (requests.Timeout, requests.ConnectionError):
            if wait is None:
                raise
            time.sleep(wait)
            continue
        if r.status_code in (429, 502, 503, 504) and wait is not None:
            time.sleep(wait)
            continue
        return r


class NotTradeable(Exception):
    """The broker says this instrument can't be traded on this account (for example XAU_USD on some OANDA accounts)."""


def _check(r, what):
    if r.status_code >= 400:
        body = r.text or ""
        if "INSTRUMENT_NOT_TRADEABLE" in body or "not tradeable" in body.lower():
            raise NotTradeable(f"{what}: not tradeable on this account")
        msg = "temporary gateway error (HTML page)" if "<html" in body[:300].lower() else body[:200]
        raise Exception(f"{what} {r.status_code}: {msg}")
    return r


class AlpacaCrypto:
    server_exits = False

    def __init__(self, symbol):
        key, secret = os.environ.get("ALPACA_KEY", "").strip(), os.environ.get("ALPACA_SECRET", "").strip()
        if not key or not secret:
            raise KeyError("ALPACA_KEY / ALPACA_SECRET")
        env = os.environ.get("ALPACA_ENV", "paper").strip().lower()
        if env == "live" and os.environ.get("ALLOW_LIVE") != "yes":
            raise Exception("Live trading is locked. Set ALLOW_LIVE=yes to enable it.")
        self.trade_url = "https://paper-api.alpaca.markets/v2" if env != "live" else "https://api.alpaca.markets/v2"
        self.data_url = "https://data.alpaca.markets/v1beta3/crypto/us/bars"
        self.headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret}
        self.symbol = symbol
        self.pos_symbol = symbol.replace("/", "")

    def candles(self, timeframe, n=100):
        hours = getattr(self, "lookback_hours", 24)
        start = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
        r = http_get(
            self.data_url, headers=self.headers, timeout=20,
            params={"symbols": self.symbol, "timeframe": timeframe, "limit": n, "sort": "desc", "start": start},
        )
        _check(r, "Alpaca data")
        raw = list(reversed(r.json()["bars"].get(self.symbol, [])))
        return [{"t": b["t"], "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]} for b in raw]

    def quote(self):
        return None  # no spread data used for crypto

    def position(self):
        r = http_get(f"{self.trade_url}/positions/{self.pos_symbol}", headers=self.headers, timeout=20)
        if r.status_code == 404:
            # Fallback: scan all positions in case Alpaca lists the symbol differently (BTCUSD vs BTC/USD)
            r2 = http_get(f"{self.trade_url}/positions", headers=self.headers, timeout=20)
            if r2.status_code < 400:
                for p in r2.json():
                    if p.get("symbol", "").replace("/", "") == self.pos_symbol:
                        return {"qty": p["qty"], "entry": float(p["avg_entry_price"])}
            return None
        _check(r, "Alpaca position")
        p = r.json()
        return {"qty": p["qty"], "entry": float(p["avg_entry_price"])}

    def describe_account(self):
        """One-line summary of what is holding the cash, for the log."""
        parts, n_open = [], "?"
        try:
            r = http_get(f"{self.trade_url}/positions", headers=self.headers, timeout=20)
            if r.status_code < 400:
                for p in r.json():
                    parts.append(f"{p['symbol']} {float(p['qty']):.6f} (${float(p.get('market_value', 0)):.2f})")
            o = http_get(f"{self.trade_url}/orders", headers=self.headers, params={"status": "open"}, timeout=20)
            if o.status_code < 400:
                n_open = len(o.json())
        except Exception as e:
            return f"could not read account ({e.__class__.__name__})"
        return "holds: " + ("; ".join(parts) or "no positions") + f" | open orders: {n_open}"

    def cash(self):
        r = _check(http_get(f"{self.trade_url}/account", headers=self.headers, timeout=20), "Alpaca account")
        return float(r.json().get("cash", 0))

    def _order(self, side, **kw):
        body = {"symbol": self.symbol, "side": side, "type": "market", "time_in_force": getattr(self, "tif", "gtc"), **kw}
        r = requests.post(f"{self.trade_url}/orders", headers=self.headers, json=body, timeout=20)
        if r.status_code >= 400:
            raise Exception(f"Order {side} rejected {r.status_code}: {r.text[:200]}")
        return r.json()["id"]

    def buy(self, cfg, price, sl=None, tp=None, side="long"):
        if side != "long":
            raise Exception("Alpaca crypto can't be shorted")
        cash = self.cash()
        usd = int(min(cfg["size_usd"], cash * 0.99) * 100) / 100
        if usd < MIN_TRADE_USD:
            return None, f"cash ${cash:.2f} too low to buy | {self.describe_account()}"
        return self._order("buy", notional=str(usd)), None

    def close(self, pos):
        return self._order("sell", qty=pos["qty"])

    def last_closed_trade(self):
        return None


class AlpacaStock(AlpacaCrypto):
    """US stocks and ETFs on Alpaca (used for the gold ETF, GLD). Fractional shares, day orders."""
    tif = "day"

    def __init__(self, symbol):
        super().__init__(symbol)
        self.data_url = "https://data.alpaca.markets/v2/stocks/bars"
        self.pos_symbol = symbol

    def candles(self, timeframe, n=100):
        start = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
        r = http_get(
            self.data_url, headers=self.headers, timeout=20,
            params={"symbols": self.symbol, "timeframe": timeframe, "limit": n, "sort": "desc",
                    "start": start, "feed": "iex", "adjustment": "raw"},
        )
        _check(r, "Alpaca stock data")
        raw = list(reversed((r.json().get("bars") or {}).get(self.symbol, []) or []))
        return [{"t": b["t"], "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]} for b in raw]

    def market_open(self):
        r = _check(http_get(f"{self.trade_url}/clock", headers=self.headers, timeout=20), "Alpaca clock")
        return bool(r.json().get("is_open"))


class Oanda:
    server_exits = True

    def __init__(self, symbol):
        token, acct = os.environ.get("OANDA_TOKEN", "").strip(), os.environ.get("OANDA_ACCOUNT_ID", "").strip()
        if not token or not acct:
            raise KeyError("OANDA_TOKEN / OANDA_ACCOUNT_ID")
        env = os.environ.get("OANDA_ENV", "practice").strip().lower()
        if env == "live" and os.environ.get("ALLOW_LIVE") != "yes":
            raise Exception("Live trading is locked. Set ALLOW_LIVE=yes to enable it.")
        self.base = "https://api-fxpractice.oanda.com" if env != "live" else "https://api-fxtrade.oanda.com"
        self.headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        self.acct, self.symbol = acct, symbol

    def _get(self, path, what, **params):
        r = http_get(f"{self.base}{path}", headers=self.headers, params=params, timeout=20)
        return _check(r, what)

    def candles(self, timeframe, n=100):
        r = self._get(f"/v3/instruments/{self.symbol}/candles", "OANDA candles",
                      granularity=timeframe, count=n + 1, price="M")
        out = []
        for c in r.json().get("candles", []):
            if not c.get("complete"):
                continue  # ignore the still-forming candle
            m = c["mid"]
            out.append({"t": c["time"], "o": float(m["o"]), "h": float(m["h"]), "l": float(m["l"]),
                        "c": float(m["c"]), "v": c.get("volume", 0)})
        return out

    def quote(self):
        r = self._get(f"/v3/accounts/{self.acct}/pricing", "OANDA pricing", instruments=self.symbol)
        p = r.json()["prices"][0]
        return {"bid": float(p["bids"][0]["price"]), "ask": float(p["asks"][0]["price"]),
                "tradeable": bool(p.get("tradeable", True))}

    def position(self):
        r = http_get(f"{self.base}/v3/accounts/{self.acct}/positions/{self.symbol}", headers=self.headers, timeout=20)
        if r.status_code == 404:
            return None
        _check(r, "OANDA position")
        p = r.json()["position"]
        lu, su = float(p["long"].get("units", 0)), float(p["short"].get("units", 0))
        if lu > 0:
            return {"qty": lu, "entry": float(p["long"].get("averagePrice", 0)), "side": "long"}
        if su < 0:
            return {"qty": -su, "entry": float(p["short"].get("averagePrice", 0)), "side": "short"}
        return None

    def margin_info(self):
        """Balance and free margin, for the log (never raises)."""
        try:
            a = self._get(f"/v3/accounts/{self.acct}/summary", "OANDA account").json()["account"]
            return f"balance {float(a.get('balance', 0)):.0f}; free margin {float(a.get('marginAvailable', 0)):.0f}"
        except Exception:
            return "balance unknown"

    def buy(self, cfg, price, sl=None, tp=None, side="long"):
        """Opens a long (positive units) or a short (negative units). For a short, sl is above and tp below the price."""
        d = cfg["decimals"]
        sign = 1 if side == "long" else -1
        units, min_units = int(cfg["units"]), int(cfg.get("min_units", 1000))
        while True:
            order = {"type": "MARKET", "instrument": self.symbol, "units": str(units * sign),
                     "timeInForce": "FOK", "positionFill": "DEFAULT"}
            if sl is not None:
                order["stopLossOnFill"] = {"price": f"{sl:.{d}f}"}
            if tp is not None:
                order["takeProfitOnFill"] = {"price": f"{tp:.{d}f}"}
            r = requests.post(f"{self.base}/v3/accounts/{self.acct}/orders", headers=self.headers,
                              json={"order": order}, timeout=20)
            no_margin = False
            if r.status_code >= 400:
                if "INSUFFICIENT_MARGIN" not in r.text:
                    raise Exception(f"Order buy rejected {r.status_code}: {r.text[:200]}")
                no_margin = True
            else:
                j = r.json()
                if "orderCancelTransaction" in j:
                    reason = j["orderCancelTransaction"].get("reason", "unknown")
                    if reason != "INSUFFICIENT_MARGIN":
                        raise Exception(f"Order buy cancelled: {reason}")
                    no_margin = True
            if not no_margin:
                self.last_units = units
                fill = j.get("orderFillTransaction", {})
                return fill.get("id") or j.get("lastTransactionID", "ok"), None
            units //= 2   # not enough free margin: try half the size
            print(f"OANDA says insufficient margin, retrying with {units} units")
            if units < min_units:
                return None, f"no margin for a trade ({self.margin_info()})"

    def close(self, pos):
        r = requests.put(f"{self.base}/v3/accounts/{self.acct}/positions/{self.symbol}/close",
                         headers=self.headers, json={("longUnits" if pos.get("side", "long") == "long" else "shortUnits"): "ALL"}, timeout=20)
        if r.status_code >= 400:
            raise Exception(f"Close rejected {r.status_code}: {r.text[:200]}")
        return r.json().get("lastTransactionID", "ok")

    def last_closed_trade(self):
        r = self._get(f"/v3/accounts/{self.acct}/trades", "OANDA trades",
                      instrument=self.symbol, state="CLOSED", count=1)
        trades = r.json().get("trades", [])
        if not trades:
            return None
        t = trades[0]
        return {"price": float(t.get("averageClosePrice", 0)), "pl": t.get("realizedPL", "?"),
                "short": float(t.get("initialUnits", 0)) < 0}


BROKERS = {"alpaca": AlpacaCrypto, "alpaca_stock": AlpacaStock, "oanda": Oanda}


# ---------------------------------------------------------------- gemini
def ask_gemini(label, bars, ind, exit_text, side="long"):
    short = side == "short"
    summary = {
        "price": round(ind["price"], 4), f"ema{EMA_FAST}": round(ind["ema_fast"], 4),
        f"ema{EMA_SLOW}": round(ind["ema_slow"], 4), f"ema{EMA_TREND}": round(ind["ema_trend"], 4),
        "rsi": round(ind["rsi"], 1),
        ("fresh_ema_crossover_down" if short else "fresh_ema_crossover"): ind["fresh_cross_down" if short else "fresh_cross"],
        "score_out_of_3": ind["score_short" if short else "score"],
        "checks": ind["checks_short" if short else "checks"],
    }
    closes = [round(b["c"], 4) for b in bars[-12:]]
    if short:
        what = "SHORT (a bet that the price falls) paper-trading entry check"
        goal = "hit take profit (the price must FALL) before stop loss (the price rises)"
        bad = "a sharp ongoing rally or an exhausted drop"
    else:
        what = "paper-trading entry check"
        goal = "hit take profit before stop loss"
        bad = "a sharp ongoing drop or an exhausted spike"
    prompt = (
        f"{label} {what}. Trade exits automatically at {exit_text}.\n"
        f"Last 12 closes, oldest first: {closes}\n"
        f"Indicators: {json.dumps(summary)}\n"
        f"Estimate how likely this trade is to {goal}, as a confidence score "
        "from 1 (very unlikely) to 6 (very likely); 3-4 is a coin flip. Mixed indicators are normal, so don't "
        f"default to low scores. Use 1-2 only for clear problems like {bad}.\n"
        'Reply with JSON only: {"confidence": <integer 1-6>, "reason": "<max 12 words>"}.'
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
    r = None
    for attempt, wait in enumerate([2, 5, 10, None]):
        try:
            r = requests.post(
                url, params={"key": GEMINI_KEY}, timeout=30,
                json={"contents": [{"parts": [{"text": prompt}]}],
                      "generationConfig": {"responseMimeType": "application/json",
                                           "thinkingConfig": {"thinkingLevel": "minimal"}}},
            )
            if r.status_code in (429, 500, 503, 504) and wait is not None:
                print(f"Gemini returned {r.status_code}, retrying in {wait}s (attempt {attempt + 1})")
                time.sleep(wait)
                continue
            if r.status_code >= 400:
                raise Exception(f"Gemini {r.status_code}: {r.text[:150]}")
            break
        except (requests.Timeout, requests.ConnectionError) as e:
            if wait is None:
                raise
            print(f"Gemini connection problem ({e.__class__.__name__}), retrying in {wait}s")
            time.sleep(wait)
    cands = r.json().get("candidates") or []
    parts = (cands[0].get("content", {}).get("parts") or []) if cands else []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    if not text.strip():
        raise Exception("Gemini returned an empty reply")
    return json.loads(text)


# ---------------------------------------------------------------- logging
HEADER = "time_utc,price,score,failing_checks,position,action,note\n"


def write_log(path, run):
    new = not os.path.exists(path)
    row = [datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M"),
           run.get("price", ""), run.get("score", ""), run.get("failing", ""),
           run.get("position", ""), run.get("action", ""), run.get("note", "")]
    with open(path, "a") as f:
        if new:
            f.write(HEADER)
        f.write(",".join(str(x).replace(",", ";").replace("\n", " ") for x in row) + "\n")


def _last_rows(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [l.split(",") for l in f.read().splitlines() if l and not l.startswith("time_utc")]


def last_action(path):
    rows = _last_rows(path)
    return rows[-1][5].strip() if rows and len(rows[-1]) >= 6 else None


def minutes_since_last_action(path, actions):
    for c in reversed(_last_rows(path)):
        if len(c) >= 6 and c[5].strip() in actions:
            try:
                t = datetime.datetime.strptime(c[0].strip(), "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc)
            except ValueError:
                return None
            return (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() / 60
    return None


def minutes_since_last_gemini_call(path):
    for c in reversed(_last_rows(path)):
        if len(c) >= 6 and (c[5].strip() in ("gemini_hold", "buy", "short")
                            or (c[5].strip() == "error" and "Order buy rejected" in ",".join(c))
                            or (c[5].strip() == "no_trade" and ("no margin" in ",".join(c) or "too low" in ",".join(c)))):
            try:
                t = datetime.datetime.strptime(c[0].strip(), "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc)
            except ValueError:
                return None
            return (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() / 60
    return None


# ---------------------------------------------------------------- per-market logic
def process_market(name, cfg, broker, pos, open_count, now):
    """Returns (run_dict_or_None, new_open_count). run is None when nothing should be logged."""
    run = {"action": "none", "note": ""}
    is_open, allow_entries, flatten = session_state(cfg["session"], now)
    if not is_open:
        print(f"[{name}] market closed, skipping.")
        return None, open_count
    if hasattr(broker, "market_open") and not broker.market_open():
        print(f"[{name}] broker clock says the market is closed (holiday?), skipping.")
        return None, open_count

    bars = broker.candles(cfg["timeframe"], 100)
    if len(bars) < 60:
        raise Exception(f"Only {len(bars)} candles returned, need 60+")
    ind = compute_indicators(bars)
    price, d = ind["price"], cfg["decimals"]
    quote = broker.quote()
    if quote is not None and not quote["tradeable"]:
        print(f"[{name}] broker says not tradeable right now, skipping.")
        return None, open_count

    run.update(price=round(price, d), score=ind["score"],
               failing="|".join(k for k, v in ind["checks"].items() if not v),
               position="yes" if pos else "no")
    print(f"[{name}] price={price:.{d}f} ema{EMA_FAST}={ind['ema_fast']:.{d}f} ema{EMA_SLOW}={ind['ema_slow']:.{d}f} "
          f"ema{EMA_TREND}={ind['ema_trend']:.{d}f} rsi={ind['rsi']:.1f} atr={ind['atr']:.{d}f} "
          f"fresh_cross={ind['fresh_cross']} score={ind['score']}/3 position={'yes' if pos else 'no'}")
    print(f"[{name}] checks:", ind["checks"])

    # ---- holding: exits
    if pos:
        side = pos.get("side", "long")
        sgn = 1 if side == "long" else -1
        exit_action = "sell" if side == "long" else "cover"
        tag = "" if side == "long" else "SHORT "
        my_score = ind["score"]
        if side == "short":
            my_score = ind["score_short"]
            run.update(score=my_score, failing="|".join(k for k, v in ind["checks_short"].items() if not v))
        entry = pos["entry"]
        change = sgn * (price - entry) / entry       # positive = the trade is making money
        reason = None
        if not broker.server_exits:                  # (long-only brokers)
            stop_d, tp_d = exit_distances(cfg, entry, ind["atr"])
            if price <= entry - stop_d:
                reason = f"STOP LOSS ({change:.1%})"
            elif price >= entry + tp_d:
                reason = f"TAKE PROFIT ({change:.1%})"
        if reason is None and (cfg.get("flatten_before_weekend") or cfg.get("flatten_at_close")) and flatten:
            reason = f"{'WEEKEND' if cfg['session'] == 'fx' else 'END-OF-DAY'} FLATTEN ({change:.1%})"
        if reason is None and my_score <= EXIT_SCORE:
            held = minutes_since_last_action(cfg["log"], ("buy", "short"))
            if held is None or held >= cfg.get("min_hold_min", MIN_HOLD_MIN):
                reason = f"SIGNAL EXIT, score {my_score}/3 ({change:.1%})"
            else:
                print(f"[{name}] Signal weak but held only {held:.0f} min (min hold {cfg.get('min_hold_min', MIN_HOLD_MIN)}). Holding.")
        if reason:
            if TRADING_ENABLED:
                oid = broker.close(pos)
                print(f"[{name}] {tag}{reason}. CLOSED:", oid)
                run.update(action=exit_action, note=reason)
            else:
                run.update(action="holding", note=f"{tag}{reason} but trading disabled")
        else:
            print(f"[{name}] {tag}Holding ({change:.1%}).")
            run.update(action="holding", note=f"{tag}{change:.1%}")
        return run, open_count

    # ---- flat: did the broker close a trade for us (server-side stop / take profit)?
    if broker.server_exits and last_action(cfg["log"]) in ("buy", "short", "holding"):
        closed = broker.last_closed_trade()
        if closed:
            run.update(price=round(closed["price"], d), position="no",
                       action="cover" if closed.get("short") else "sell",
                       note=f"closed by broker stop/TP; P/L {closed['pl']}")
            print(f"[{name}] position was closed by the broker: {run['note']}")
            return run, open_count

    # ---- flat: entries
    if not allow_entries:
        print(f"[{name}] no new entries right now (outside the entry window).")
        run.update(action="no_trade", note="no new entries before weekend" if cfg["session"] == "fx" else "outside entry window")
        return run, open_count
    shorting = bool(cfg.get("allow_short")) and SHORTING_ENABLED
    long_ok = ind["score"] >= MIN_ENTRY_SCORE and (not REQUIRE_FAST_ABOVE_SLOW or ind["checks"]["fast_above_slow"])
    short_ok = shorting and ind["score_short"] >= MIN_ENTRY_SCORE and (
        not REQUIRE_FAST_ABOVE_SLOW or ind["checks_short"]["fast_below_slow"])
    if long_ok:
        side = "long"
    elif short_ok:
        side = "short"
        run.update(score=ind["score_short"], failing="|".join(k for k, v in ind["checks_short"].items() if not v))
    else:
        if shorting:
            note = "no long or short setup"
        elif ind["score"] < MIN_ENTRY_SCORE:
            note = f"score below {MIN_ENTRY_SCORE}"
        else:
            note = "short-term trend not up"
        run.update(action="no_trade", note=note)
        print(f"[{name}] {note}. No trade.")
        return run, open_count
    since_sell = minutes_since_last_action(cfg["log"], ("sell", "cover"))
    if since_sell is not None and since_sell < cfg.get("reentry_min", REENTRY_COOLDOWN_MIN):
        run.update(action="no_trade", note="re-entry cooldown")
        print(f"[{name}] Closed {since_sell:.0f} min ago. Waiting {cfg.get('reentry_min', REENTRY_COOLDOWN_MIN)} min before opening again.")
        return run, open_count
    if open_count >= MAX_OPEN_POSITIONS:
        run.update(action="no_trade", note=f"max {MAX_OPEN_POSITIONS} open positions reached")
        return run, open_count
    stop_d, tp_d = exit_distances(cfg, price, ind["atr"])
    if quote is not None and "max_spread_frac" in cfg:
        spread = quote["ask"] - quote["bid"]
        if spread > cfg["max_spread_frac"] * tp_d:
            run.update(action="no_trade", note=f"spread {spread:.{d}f} too wide vs target")
            return run, open_count
    ago = minutes_since_last_gemini_call(cfg["log"])
    if ago is not None and ago < cfg["cooldown_min"]:
        print(f"[{name}] Gemini was asked {ago:.1f} min ago. Waiting for the next candle.")
        run.update(action="no_trade", note="Gemini cooldown")
        return run, open_count

    vol = ", set from recent volatility" if cfg["exit"]["mode"] == "atr" else ""
    if side == "short":
        exit_text = f"a {tp_d / price:.2%} fall (take profit) or a {stop_d / price:.2%} rise (stop loss){vol}"
    else:
        exit_text = f"+{tp_d / price:.2%} (take profit) or -{stop_d / price:.2%} (stop loss){vol}"
    decision = ask_gemini(cfg["label"], bars, ind, exit_text, side)
    print(f"[{name}] Gemini ({side}):", decision)
    try:
        conf = int(decision.get("confidence", 0))
    except (TypeError, ValueError):
        conf = 0
    note = f"conf {conf}: {decision.get('reason', '')}"
    if conf < cfg.get("min_confidence", MIN_CONFIDENCE):
        run.update(action="gemini_hold", note=note)
        return run, open_count
    if not TRADING_ENABLED:
        run.update(action="gemini_hold", note=note + " (trading disabled)")
        return run, open_count

    # a long is bought at the ask, a short is sold at the bid; the stop goes on the losing side
    if side == "short":
        ref = quote["bid"] if quote else price
        sl = round(ref + stop_d, d) if broker.server_exits else None
        tp = round(ref - tp_d, d) if broker.server_exits else None
    else:
        ref = quote["ask"] if quote else price
        sl = round(ref - stop_d, d) if broker.server_exits else None
        tp = round(ref + tp_d, d) if broker.server_exits else None
    oid, skip = broker.buy(cfg, price, sl, tp, side)
    if skip:
        print(f"[{name}] {skip}. Skipping.")
        run.update(action="no_trade", note=skip)
        return run, open_count
    lu = getattr(broker, "last_units", None)
    if lu and lu != cfg.get("units"):
        note += f" | {lu} units (reduced for margin)"
    print(f"[{name}] {'SHORT' if side == 'short' else 'BUY'} order:", oid, f"(stop {sl}, take profit {tp})" if sl else "")
    run.update(action="short" if side == "short" else "buy", note=note)
    return run, open_count + 1

def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    active = {n: c for n, c in MARKETS.items() if c["enabled"]}
    brokers, problems = {}, []
    for name, cfg in active.items():
        try:
            brokers[name] = BROKERS[cfg["broker"]](cfg["symbol"])
            if "lookback_hours" in cfg:
                brokers[name].lookback_hours = cfg["lookback_hours"]
        except KeyError as e:
            print(f"[{name}] skipped: missing secret {e}")
        except Exception as e:
            print(f"[{name}] ERROR setting up broker: {e}")
            problems.append(name)

    # phase 1: read positions so the open-position limit counts every market
    positions, open_count = {}, 0
    for name, b in brokers.items():
        try:
            positions[name] = b.position()
            open_count += 1 if positions[name] else 0
        except NotTradeable as e:
            positions[name] = "skip"
            print(f"[{name}] skipped: {e}")
        except Exception as e:
            positions[name] = "error"
            print(f"[{name}] ERROR reading position: {e}")
            write_log(active[name]["log"], {"action": "error", "note": str(e)[:120]})
            problems.append(name)

    # phase 2: each market on its own, so one failure never blocks the others
    for name, b in brokers.items():
        if positions.get(name) in ("error", "skip"):
            continue
        cfg = active[name]
        try:
            run, open_count = process_market(name, cfg, b, positions[name], open_count, now)
            if run is not None:
                write_log(cfg["log"], run)
        except NotTradeable as e:
            print(f"[{name}] skipped: {e}")
        except Exception as e:
            print(f"[{name}] ERROR:", e)
            write_log(cfg["log"], {"action": "error", "note": str(e)[:120]})
            problems.append(name)
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
