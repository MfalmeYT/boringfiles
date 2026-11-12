"""One-time, READ-ONLY probe of the TradeLocker demo account.
It logs in and prints what the library offers (method names, instrument names, candle format, positions).
It never places an order. Delete it after use."""
import inspect
import os
import sys

from tradelocker import TLAPI

ENV = os.environ.get("TL_ENV", "").strip() or "https://demo.tradelocker.com"
USER = os.environ.get("TL_USERNAME", "").strip()
PASS = os.environ.get("TL_PASSWORD", "").strip()
SERVER = os.environ.get("TL_SERVER", "").strip()
if not (USER and PASS and SERVER):
    print("Missing TL_USERNAME / TL_PASSWORD / TL_SERVER secret.")
    sys.exit(1)


def section(title):
    print("\n=== " + title + " ===")


def attempt(label, fn):
    try:
        return fn()
    except Exception as e:  # keep going so one failure does not hide the rest
        print(f"[{label}] FAILED: {e.__class__.__name__}: {str(e)[:300]}")
        return None


section("login")
tl = attempt("login", lambda: TLAPI(environment=ENV, username=USER, password=PASS, server=SERVER))
if tl is None:
    sys.exit(1)
print("login OK")

section("library methods")
print([m for m in dir(tl) if not m.startswith("_")])

section("method signatures")
for name in ("create_order", "close_position", "close_all_positions", "get_all_positions", "get_all_orders",
             "get_price_history", "get_latest_asking_price", "get_account_state", "get_quotes"):
    if hasattr(tl, name):
        print(name, inspect.signature(getattr(tl, name)))
    else:
        print(name, "-> not in this version")

section("instruments")
inst = attempt("instruments", tl.get_all_instruments)
ids = {}
if inst is not None:
    print("columns:", list(inst.columns), "| total:", len(inst))
    names = inst["name"].astype(str)
    for want in ("BTCUSD", "EURUSD", "GBPUSD", "USDJPY", "EURGBP", "XAUUSD"):
        row = inst[names == want]
        print(want, "->", row.iloc[0].to_dict() if len(row) else "NOT FOUND")
        if len(row):
            ids[want] = int(row.iloc[0]["tradableInstrumentId"])
    print("names containing JPY:", sorted(n for n in names if "JPY" in n)[:30])
    print("names containing EUR:", sorted(n for n in names if "EUR" in n)[:30])

section("candles (tries several resolution names)")
iid = ids.get("EURUSD") or ids.get("BTCUSD")
if iid:
    for res in ("5m", "5M", "5Min", "15m", "15M", "15Min"):
        h = attempt("history " + res, lambda r=res: tl.get_price_history(
            iid, resolution=r, start_timestamp=0, end_timestamp=0, lookback_period="1D"))
        if h is not None:
            print(res, "-> rows:", len(h), "| columns:", list(h.columns))
            print(h.tail(3).to_string())

section("latest ask")
if iid:
    print(attempt("ask", lambda: tl.get_latest_asking_price(iid)))

section("open positions (read only)")
if hasattr(tl, "get_all_positions"):
    p = attempt("positions", tl.get_all_positions)
    if p is not None:
        print("columns:", list(p.columns), "| rows:", len(p))
        print(p.head(5).to_string())

section("account state (read only)")
if hasattr(tl, "get_account_state"):
    print(attempt("account", tl.get_account_state))
print("\nDONE. No orders were placed.")
