"""Paper-trading BTC bot: Alpaca (data + paper orders) + multi-indicator score + Gemini confirmation.
Runs once per call. Schedule it with GitHub Actions (see bot.yml).

Entry score (0-3), one point each:
  1. Fast EMA above slow EMA (short-term uptrend)
  2. Price above the longer EMA (bigger-picture uptrend)
  3. RSI between 45 and 70 (momentum, not overbought)

Rules:
- Buy: score >= MIN_ENTRY_SCORE AND Gemini's confidence (1-6) >= MIN_CONFIDENCE.
- Sell: stop loss, take profit, or score falls to EXIT_SCORE or lower.
- Risk rules live in code, not in the LLM.
"""
import datetime
import json
import os
import sys
import time

import requests

ALPACA_KEY = os.environ["ALPACA_KEY"]
ALPACA_SECRET = os.environ["ALPACA_SECRET"]
GEMINI_KEY = os.environ["GEMINI_KEY"]
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")

TRADE_USD = 100          # max size per buy; the bot buys less if your cash is lower
MIN_TRADE_USD = 10       # skip buying if available cash is below this
STOP_LOSS_PCT = 0.02     # sell everything if the position is down 2% from entry
TAKE_PROFIT_PCT = 0.02   # sell everything if the position is up 2% from entry

EMA_FAST = 9
EMA_SLOW = 21
EMA_TREND = 50
RSI_PERIOD = 14
RSI_LOW, RSI_HIGH = 45, 70
CROSS_LOOKBACK = 3       # a crossover within the last 3 candles counts as "fresh"
GEMINI_COOLDOWN_MIN = 5   # ask Gemini at most once per this many minutes (candles are 5 min, so more is wasted)
MIN_CONFIDENCE = 3       # Gemini confidence (1-6) needed to buy; lower = more trades
MIN_ENTRY_SCORE = 2      # need at least 2 of 3 points to ask Gemini; Gemini makes the final call
EXIT_SCORE = 0           # sell on score alone only if all 3 checks fail (stop loss / take profit still apply)

LOG_FILE = "bot_log.csv"
RUN = {"action": "none", "note": ""}   # filled in during the run, written to the log at the end

PAPER = "https://paper-api.alpaca.markets/v2"
DATA = "https://data.alpaca.markets/v1beta3/crypto/us/bars"
HEADERS = {"APCA-API-KEY-ID": ALPACA_KEY, "APCA-API-SECRET-KEY": ALPACA_SECRET}


def get_bars():
    # Ask for the NEWEST 100 candles (sort=desc), looking back 24h so there are always enough.
    # (Without sort/start, Alpaca returns the oldest candles of the current UTC day and the data goes stale.)
    start = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = requests.get(
        DATA,
        headers=HEADERS,
        params={"symbols": "BTC/USD", "timeframe": "5Min", "limit": 100, "sort": "desc", "start": start},
        timeout=20,
    )
    if r.status_code >= 400:
        raise Exception(f"Alpaca data {r.status_code}: {r.text[:200]}")
    bars = list(reversed(r.json()["bars"].get("BTC/USD", [])))  # oldest first
    if len(bars) < 60:
        raise Exception(f"Only {len(bars)} candles returned, need 60+")
    return [{"t": b["t"], "o": b["o"], "h": b["h"], "l": b["l"], "c": b["c"], "v": b["v"]} for b in bars]


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


def compute_indicators(bars):
    closes = [b["c"] for b in bars]
    fast = ema(closes, EMA_FAST)
    slow = ema(closes, EMA_SLOW)
    trend = ema(closes, EMA_TREND)
    fresh_cross = any(
        fast[i - 1] <= slow[i - 1] and fast[i] > slow[i]
        for i in range(len(closes) - CROSS_LOOKBACK, len(closes))
    )
    price = closes[-1]
    checks = {
        "fast_above_slow": fast[-1] > slow[-1],
        "price_above_trend_ema": price > trend[-1],
        "rsi_in_range": RSI_LOW <= rsi(closes, RSI_PERIOD) <= RSI_HIGH,
    }
    return {
        "price": price,
        "ema_fast": fast[-1],
        "ema_slow": slow[-1],
        "ema_trend": trend[-1],
        "rsi": rsi(closes, RSI_PERIOD),
        "fresh_cross": fresh_cross,
        "checks": checks,
        "score": sum(checks.values()),
    }


def get_cash():
    r = requests.get(f"{PAPER}/account", headers=HEADERS, timeout=20)
    if r.status_code >= 400:
        raise Exception(f"Account {r.status_code}: {r.text[:200]}")
    return float(r.json().get("cash", 0))


def get_position():
    r = requests.get(f"{PAPER}/positions/BTCUSD", headers=HEADERS, timeout=20)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()


def gemini_confirms_buy(bars, ind):
    summary = {
        "price": round(ind["price"], 2),
        f"ema{EMA_FAST}": round(ind["ema_fast"], 2),
        f"ema{EMA_SLOW}": round(ind["ema_slow"], 2),
        f"ema{EMA_TREND}": round(ind["ema_trend"], 2),
        "rsi": round(ind["rsi"], 1),
        "fresh_ema_crossover": ind["fresh_cross"],
        "score_out_of_3": ind["score"],
        "checks": ind["checks"],
    }
    closes = [round(b["c"]) for b in bars[-12:]]
    prompt = (
        "BTC paper-trading entry check. Trade exits automatically at +2% (take profit) or -2% (stop loss).\n"
        f"Last 12 five-minute closes, oldest first: {closes}\n"
        f"Indicators: {json.dumps(summary)}\n"
        "Estimate how likely this trade is to hit +2% before -2%, as a confidence score from 1 (very unlikely) "
        "to 6 (very likely); 3-4 is a coin flip. Mixed indicators are normal, so don't default to low scores. "
        "Use 1-2 only for clear problems like a sharp ongoing drop or an exhausted spike.\n"
        'Reply with JSON only: {"confidence": <integer 1-6>, "reason": "<max 12 words>"}.'
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
    # Gemini sometimes returns temporary errors (503 overloaded, 429, 500, 504). Retry a few times.
    for attempt, wait in enumerate([2, 5, 10, None]):
        try:
            r = requests.post(
                url,
                params={"key": GEMINI_KEY},
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {
                        "responseMimeType": "application/json",
                        "thinkingConfig": {"thinkingLevel": "minimal"},  # thinking tokens are billed as output
                    },
                },
                timeout=30,
            )
            if r.status_code in (429, 500, 503, 504) and wait is not None:
                print(f"Gemini returned {r.status_code}, retrying in {wait}s (attempt {attempt + 1})")
                time.sleep(wait)
                continue
            r.raise_for_status()
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


def minutes_since_last_gemini_call():
    """Look in bot_log.csv for the last run that actually asked Gemini."""
    if not os.path.exists(LOG_FILE):
        return None
    with open(LOG_FILE) as f:
        lines = f.read().splitlines()
    for line in reversed(lines):
        c = line.split(",")
        if len(c) >= 6 and (c[5].strip() in ("gemini_hold", "buy") or (c[5].strip() == "error" and "Order buy rejected" in line)):
            try:
                t = datetime.datetime.strptime(c[0].strip(), "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc)
            except ValueError:
                return None
            return (datetime.datetime.now(datetime.timezone.utc) - t).total_seconds() / 60
    return None


def write_log():
    """Append one line per run so all runs can be read in a single file."""
    new = not os.path.exists(LOG_FILE)
    row = [
        datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M"),
        RUN.get("price", ""),
        RUN.get("score", ""),
        RUN.get("failing", ""),
        RUN.get("position", ""),
        RUN.get("action", ""),
        RUN.get("note", ""),
    ]
    with open(LOG_FILE, "a") as f:
        if new:
            f.write("time_utc,price,score,failing_checks,position,action,note\n")
        f.write(",".join(str(x).replace(",", ";").replace("\n", " ") for x in row) + "\n")


def place_order(side, **kwargs):
    body = {"symbol": "BTC/USD", "side": side, "type": "market", "time_in_force": "gtc", **kwargs}
    r = requests.post(f"{PAPER}/orders", headers=HEADERS, json=body, timeout=20)
    if r.status_code >= 400:
        raise Exception(f"Order {side} rejected {r.status_code}: {r.text[:200]}")
    return r.json()


def main():
    bars = get_bars()
    ind = compute_indicators(bars)
    price = ind["price"]
    position = get_position()
    print(
        f"price={price:.2f} ema{EMA_FAST}={ind['ema_fast']:.2f} ema{EMA_SLOW}={ind['ema_slow']:.2f} "
        f"ema{EMA_TREND}={ind['ema_trend']:.2f} rsi={ind['rsi']:.1f} "
        f"fresh_cross={ind['fresh_cross']} score={ind['score']}/3 position={'yes' if position else 'no'}"
    )
    print("checks:", ind["checks"])
    RUN.update(
        price=round(price, 2),
        score=ind["score"],
        failing="|".join(k for k, v in ind["checks"].items() if not v),
        position="yes" if position else "no",
    )

    # Holding: exits are rule-based and ignore Gemini.
    if position:
        entry = float(position["avg_entry_price"])
        change = (price - entry) / entry
        reason = None
        if change <= -STOP_LOSS_PCT:
            reason = f"STOP LOSS ({change:.1%})"
        elif change >= TAKE_PROFIT_PCT:
            reason = f"TAKE PROFIT ({change:.1%})"
        elif ind["score"] <= EXIT_SCORE:
            reason = f"SIGNAL EXIT, score {ind['score']}/3 ({change:.1%})"
        if reason:
            order = place_order("sell", qty=position["qty"])
            print(f"{reason}. SELL order:", order["id"])
            RUN.update(action="sell", note=reason)
        else:
            print(f"Holding ({change:.1%}).")
            RUN.update(action="holding", note=f"{change:.1%}")
        return

    # Flat: need a good enough score, then Gemini must agree.
    if ind["score"] >= MIN_ENTRY_SCORE:
        ago = minutes_since_last_gemini_call()
        if ago is not None and ago < GEMINI_COOLDOWN_MIN:
            print(f"Gemini was asked {ago:.1f} min ago. Waiting for the next candle.")
            RUN.update(action="no_trade", note="Gemini cooldown")
            return
        cash = get_cash()
        buy_usd = int(min(TRADE_USD, cash * 0.99) * 100) / 100   # leave ~1% headroom for fees
        if buy_usd < MIN_TRADE_USD:
            print(f"Cash ${cash:.2f} is too low to buy. Skipping.")
            RUN.update(action="no_trade", note=f"cash ${cash:.2f} too low to buy")
            return
        decision = gemini_confirms_buy(bars, ind)
        print("Gemini:", decision)
        try:
            conf = int(decision.get("confidence", 0))
        except (TypeError, ValueError):
            conf = 0
        note = f"conf {conf}: {decision.get('reason', '')}"
        if conf >= MIN_CONFIDENCE:
            order = place_order("buy", notional=str(buy_usd))
            print("BUY order:", order["id"])
            RUN.update(action="buy", note=note)
        else:
            print("Gemini said hold. No trade.")
            RUN.update(action="gemini_hold", note=note)
    else:
        print(f"Score {ind['score']}/3 is below {MIN_ENTRY_SCORE}. No trade.")
        RUN.update(action="no_trade", note=f"score below {MIN_ENTRY_SCORE}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # fail loudly in the Actions log, never trade on errors
        print("ERROR:", e)
        RUN.update(action="error", note=str(e)[:120])
        write_log()
        sys.exit(1)
    write_log()
