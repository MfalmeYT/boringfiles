"""Paper-trading BTC bot: Alpaca (data + paper orders) + EMA crossover + Gemini confirmation.
Runs once per call. Schedule it with GitHub Actions (see bot.yml).

Rules:
- Buy: fast EMA crossed above slow EMA within the last few candles AND Gemini confirms.
- Sell: 2% stop loss, 2% take profit, or fast EMA falls below slow EMA.
- Risk rules live in code, not in the LLM.
"""
import json
import os
import sys

import requests

ALPACA_KEY = os.environ["ALPACA_KEY"]
ALPACA_SECRET = os.environ["ALPACA_SECRET"]
GEMINI_KEY = os.environ["GEMINI_KEY"]
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")  # check Google's current model names

TRADE_USD = 100          # fixed size per buy (paper money)
STOP_LOSS_PCT = 0.02     # sell everything if the position is down 2% from entry
TAKE_PROFIT_PCT = 0.02   # sell everything if the position is up 2% from entry
EMA_FAST = 9
EMA_SLOW = 21
CROSS_LOOKBACK = 3       # a crossover within the last 3 candles counts as a fresh signal

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


def get_position():
    r = requests.get(f"{PAPER}/positions/BTCUSD", headers=HEADERS, timeout=20)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()


def gemini_confirms_buy(bars, fast_val, slow_val):
    prompt = (
        "You are a cautious BTC trading assistant on a paper account.\n"
        f"Last 30 five-minute candles (oldest first): {json.dumps(bars[-30:])}\n"
        f"EMA{EMA_FAST} = {fast_val:.2f}, EMA{EMA_SLOW} = {slow_val:.2f}. "
        f"The fast EMA just crossed above the slow EMA (bullish signal).\n"
        "Should we open a long position now? Say hold if the move looks weak, choppy, or already overextended.\n"
        'Reply with JSON only: {"action": "buy" | "hold", "reason": "<one sentence>"}.'
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


def place_order(side, **kwargs):
    body = {"symbol": "BTC/USD", "side": side, "type": "market", "time_in_force": "gtc", **kwargs}
    r = requests.post(f"{PAPER}/orders", headers=HEADERS, json=body, timeout=20)
    r.raise_for_status()
    return r.json()


def main():
    bars = get_bars()
    closes = [b["c"] for b in bars]
    price = closes[-1]
    fast = ema(closes, EMA_FAST)
    slow = ema(closes, EMA_SLOW)
    bullish = fast[-1] > slow[-1]
    recent_cross = any(
        fast[i - 1] <= slow[i - 1] and fast[i] > slow[i]
        for i in range(len(closes) - CROSS_LOOKBACK, len(closes))
    )
    position = get_position()
    print(
        f"price={price:.2f} ema{EMA_FAST}={fast[-1]:.2f} ema{EMA_SLOW}={slow[-1]:.2f} "
        f"bullish={bullish} fresh_cross={recent_cross} position={'yes' if position else 'no'}"
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
        elif not bullish:
            reason = f"EMA BEARISH EXIT ({change:.1%})"
        if reason:
            order = place_order("sell", qty=position["qty"])
            print(f"{reason}. SELL order:", order["id"])
        else:
            print(f"Holding ({change:.1%}).")
        return

    # Flat: need a fresh bullish EMA cross, then Gemini must agree.
    if bullish and recent_cross:
        decision = gemini_confirms_buy(bars, fast[-1], slow[-1])
        print("Gemini:", decision)
        if str(decision.get("action", "hold")).lower() == "buy":
            order = place_order("buy", notional=str(TRADE_USD))
            print("BUY order:", order["id"])
        else:
            print("Gemini said hold. No trade.")
    else:
        print("No signal. No trade.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # fail loudly in the Actions log, never trade on errors
        print("ERROR:", e)
        sys.exit(1)
