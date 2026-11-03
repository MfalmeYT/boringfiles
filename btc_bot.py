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

import requests

ALPACA_KEY = os.environ["ALPACA_KEY"]
ALPACA_SECRET = os.environ["ALPACA_SECRET"]
GEMINI_KEY = os.environ["GEMINI_KEY"]
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")

TRADE_USD = 100          # fixed size per buy (paper money)
STOP_LOSS_PCT = 0.02     # sell everything if the position is down 2% from entry
TAKE_PROFIT_PCT = 0.02   # sell everything if the position is up 2% from entry

EMA_FAST = 9
EMA_SLOW = 21
EMA_TREND = 50
RSI_PERIOD = 14
RSI_LOW, RSI_HIGH = 45, 70
CROSS_LOOKBACK = 3       # a crossover within the last 3 candles counts as "fresh"
MIN_CONFIDENCE = 3       # Gemini confidence (1-6) needed to buy; lower = more trades
MIN_ENTRY_SCORE = 2      # need at least 2 of 3 points to ask Gemini; Gemini makes the final call
EXIT_SCORE = 0           # sell on score alone only if all 3 checks fail (stop loss / take profit still apply)

LOG_FILE = "bot_log.csv"
RUN = {"action": "none", "note": ""}   # filled in during the run, written to the log at the end

PAPER = "https://paper-api.alpaca.markets/v2"
DATA = "https://data.alpaca.markets/v1beta3/crypto/us/bars"
HEADERS = {"APCA-API-KEY-ID": ALPACA_KEY, "APCA-API-SECRET-KEY": ALPACA_SECRET}


def get_bars():
    r = requests.get(
        DATA,
        headers=HEADERS,
        params={"symbols": "BTC/USD", "timeframe": "5Min", "limit": 100},
        timeout=20,
    )
    r.raise_for_status()
    bars = r.json()["bars"]["BTC/USD"]
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
    prompt = (
        "You are a BTC trading assistant on a paper account used for testing a strategy.\n"
        f"Last 30 five-minute candles (oldest first): {json.dumps(bars[-30:])}\n"
        f"Indicator summary: {json.dumps(summary)}\n"
        f"The rules-based system flagged a possible long entry (score {ind['score']}/3). "
        "Position rules: the trade exits automatically at +2% (take profit) or -2% (stop loss). "
        "Estimate how likely this trade is to hit +2% before -2% from the current price, as a confidence "
        "score from 1 (very unlikely) to 6 (very likely). A 3 or 4 means roughly a coin flip. "
        "Do not default to low scores out of caution; mixed indicators are normal and expected here. "
        "Reserve scores of 1-2 for clear problems, such as a sharp ongoing drop or an exhausted spike.\n"
        'Reply with JSON only: {"confidence": <integer 1-6>, "reason": "<one sentence>"}.'
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
    r = requests.post(
        url,
        params={"key": GEMINI_KEY},
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseMimeType": "application/json"},
        },
        timeout=30,
    )
    r.raise_for_status()
    text = r.json()["candidates"][0]["content"]["parts"][0]["text"]
    return json.loads(text)


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
    r.raise_for_status()
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
        decision = gemini_confirms_buy(bars, ind)
        print("Gemini:", decision)
        try:
            conf = int(decision.get("confidence", 0))
        except (TypeError, ValueError):
            conf = 0
        note = f"conf {conf}: {decision.get('reason', '')}"
        if conf >= MIN_CONFIDENCE:
            order = place_order("buy", notional=str(TRADE_USD))
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
