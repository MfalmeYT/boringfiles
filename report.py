"""Writes report.md: a compact snapshot of the bot (settings, per-market results, errors, latest rows).
Run after trader.py. The Bot Monitor 'Report' tab and Claude both read this one file."""
import csv, datetime, glob, os, re
import trader as T

FEES = {"alpaca": 0.25, "oanda": 0.0}
now = datetime.datetime.now(datetime.timezone.utc)
lines = [f"# Bot report (generated {now:%Y-%m-%d %H:%M} UTC)", "", "## Settings (read from trader.py)"]
lines.append(f"- trading enabled: {T.TRADING_ENABLED}; shorting enabled: {T.SHORTING_ENABLED}; max open positions: {T.MAX_OPEN_POSITIONS}")
lines.append(f"- entry needs {T.MIN_ENTRY_SCORE} of 3 checks (EMA {T.EMA_FAST}/{T.EMA_SLOW}/{T.EMA_TREND}, RSI {T.RSI_LOW}-{T.RSI_HIGH}; short = mirror) plus Gemini confidence 1-6; model {T.GEMINI_MODEL}")
for c in T.MARKETS.values():
    ex = c["exit"]
    e = f"ATR stop {ex['stop_mult']}x / target {ex['tp_mult']}x" if ex["mode"] == "atr" else f"stop {ex['stop']:.1%} / target {ex['tp']:.1%}"
    size = f"{c['units']} units" if "units" in c else f"${c['size_usd']}"
    lines.append(f"- {c['label']} ({'on' if c['enabled'] else 'off'}): {c['broker']}, {c['timeframe']} candles, {e}, size {size}, "
                 f"min confidence {c.get('min_confidence', T.MIN_CONFIDENCE)}, min hold {c.get('min_hold_min', T.MIN_HOLD_MIN)} min, "
                 f"re-entry pause {c.get('reentry_min', T.REENTRY_COOLDOWN_MIN)} min, {'long and short' if c.get('allow_short') else 'long only'}")

def load(path):
    out = []
    with open(path) as f:
        for row in csv.reader(f):
            if len(row) >= 6 and row[0] != "time_utc":
                try:
                    out.append((datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc),
                                row[1], row[5].strip(), ",".join(row[6:])))
                except ValueError:
                    pass
    return out

def trades(rows, fee):
    done, op = [], None
    for t, p, a, n in rows:
        try:
            p = float(p)
        except ValueError:
            continue
        if a in ("buy", "short") and not op:
            op = (t, p, 1 if a == "buy" else -1)
        elif a in ("sell", "cover") and op:
            done.append((op[2], (p / op[1] - 1) * 100 * op[2] - 2 * fee))
            op = None
    return done, op

lines += ["", "## Markets (last 24h unless noted)", "",
          "| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |", "|---|---|---|---|---|---|---|---|---|"]
errs, tail, tr_lines = {}, [], []
for c in T.MARKETS.values():
    if not os.path.exists(c["log"]):
        continue
    rows = load(c["log"])
    if not rows:
        continue
    day = [r for r in rows if (now - r[0]).total_seconds() < 86400]
    fee = FEES.get(c["broker"], 0)
    done, op = trades(rows, fee)
    w = sum(1 for _, r in done if r > 0)
    ent = sum(1 for r in day if r[2] in ("buy", "short"))
    er = [r for r in day if r[2] == "error"]
    for r in er:
        k = (c["label"], re.sub(r"\d{5,}", "#", r[3])[:100])
        errs[k] = errs.get(k, 0) + 1
    lines.append(f"| {c['label']} | {rows[-1][0]:%m-%d %H:%M} | {len(day)} | {ent} | {len(er)} | {len(done)} | "
                 f"{round(w / len(done) * 100) if done else '-'} | {sum(r for _, r in done):+.2f} | {'yes' if op else ''} |")
    for d, r in done[-5:]:
        tr_lines.append(f"- {c['label']}: {'short' if d < 0 else 'long'} {r:+.2f}%")
    tail += [f"- {c['label']} {r[0]:%m-%d %H:%M} price {r[1]} {r[2]} {r[3][:90]}" for r in rows[-3:]]
    longs = [r for d, r in done if d > 0]; shorts = [r for d, r in done if d < 0]
    if shorts:
        tr_lines.append(f"- {c['label']} totals: long {len(longs)} trades {sum(longs):+.2f}%, short {len(shorts)} trades {sum(shorts):+.2f}%")
lines += ["", "## Raw log files (full history, one row per run)"] + [f"- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/{c['log']}" for c in T.MARKETS.values()]
lines += ["", "## Errors in the last 24h (grouped)"] + ([f"- x{n} {m}: {t}" for (m, t), n in sorted(errs.items(), key=lambda x: -x[1])[:10]] or ["- none"])
lines += ["", "## Latest closed trades"] + (tr_lines or ["- none yet"])
lines += ["", "## Latest log rows"] + tail
open("report.md", "w").write("\n".join(lines) + "\n")
print("report.md written")
