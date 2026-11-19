"""Writes report.md (full snapshot), status.md (15-line version), report.json (same data for programs) and
reports/daily/<date>.md (one file per UTC day). Run after trader.py. The Bot Monitor 'Report' tab and Claude read these."""
import csv, datetime, json, os, re
import trader as T

FEES = {"alpaca": 0.25, "oanda": 0.0}
now = datetime.datetime.now(datetime.timezone.utc)
RAW = "https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/"
lines = [f"# Bot report (generated {now:%Y-%m-%d %H:%M} UTC)", "", "## Settings (read from trader.py)"]
lines.append(f"- trading enabled: {T.TRADING_ENABLED}; shorting enabled: {T.SHORTING_ENABLED}; max open positions: {T.MAX_OPEN_POSITIONS}")
lines.append(f"- entry needs {T.MIN_ENTRY_SCORE} of 3 checks (EMA {T.EMA_FAST}/{T.EMA_SLOW}/{T.EMA_TREND}, RSI {T.RSI_LOW}-{T.RSI_HIGH}; short = mirror) plus Gemini confidence 1-6; model {T.GEMINI_MODEL}")
for c in T.MARKETS.values():
    ex = c["exit"]
    e = f"ATR stop {ex['stop_mult']}x / target {ex['tp_mult']}x" if ex["mode"] == "atr" else f"stop {ex['stop']:.1%} / target {ex['tp']:.1%}"
    size = f"{c['units']} units" if "units" in c else f"${c['size_usd']}"
    lines.append(f"- {c['label']} ({'on' if c['enabled'] else 'off'}): {c['broker']}, {c['timeframe']} candles, {e}, size {size}, "
                 f"min confidence {c.get('min_confidence', T.MIN_CONFIDENCE)}, min hold {c.get('min_hold_min', T.MIN_HOLD_MIN)} min, "
                 f"re-entry pause {c.get('reentry_min', T.REENTRY_COOLDOWN_MIN)} min, signal exit {'on' if c.get('signal_exit', True) else 'OFF'}, "
                 f"{'long and short' if c.get('allow_short') else 'long only'}")

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
    """Returns (closed trades as (direction, result %, close time), open position or None)."""
    done, op = [], None
    for t, p, a, n in rows:
        try:
            p = float(p)
        except ValueError:
            continue
        if a in ("buy", "short") and not op:
            op = (t, p, 1 if a == "buy" else -1)
        elif a in ("sell", "cover") and op:
            done.append((op[2], (p / op[1] - 1) * 100 * op[2] - 2 * fee, t))
            op = None
    return done, op

def data_rows(fname, n):
    p = os.path.join("data", fname)
    if not os.path.exists(p):
        return []
    with open(p) as f:
        return [l for l in f.read().splitlines()[1:] if l][-n:]

lines += ["", "## Markets (last 24h unless noted)", "",
          "| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |", "|---|---|---|---|---|---|---|---|---|"]
errs, tail, tr_lines, mk, lastc = {}, [], [], [], []
o401, rid = 0, []
today = f"{now:%Y-%m-%d}"
for c in T.MARKETS.values():
    if not os.path.exists(c["log"]):
        continue
    rows = load(c["log"])
    if not rows:
        continue
    day = [r for r in rows if (now - r[0]).total_seconds() < 86400]
    fee = FEES.get(c["broker"], 0)
    done, op = trades(rows, fee)
    w = sum(1 for _, r, _t in done if r > 0)
    ent = sum(1 for r in day if r[2] in ("buy", "short"))
    er = [r for r in day if r[2] == "error"]
    for r in er:
        k = (c["label"], re.sub(r"\d{5,}", "#", r[3])[:100])
        errs[k] = errs.get(k, 0) + 1
        if "401" in r[3] and "OANDA" in r[3]:
            o401 += 1
            m = re.search(r"\[req (\d+)\]", r[3])
            if m:
                rid.append(m.group(1))
    wr = round(w / len(done) * 100) if done else None
    tot = sum(r for _, r, _t in done)
    lines.append(f"| {c['label']} | {rows[-1][0]:%m-%d %H:%M} | {len(day)} | {ent} | {len(er)} | {len(done)} | "
                 f"{wr if wr is not None else '-'} | {tot:+.2f} | {'yes' if op else ''} |")
    if done:
        lastc.append((done[-1][2], f"{c['label']} {'short' if done[-1][0] < 0 else 'long'} {done[-1][1]:+.2f}%"))
    for d, r, _t in done[-5:]:
        tr_lines.append(f"- {c['label']}: {'short' if d < 0 else 'long'} {r:+.2f}%")
    tail += [f"- {c['label']} {r[0]:%m-%d %H:%M} price {r[1]} {r[2]} {r[3][:90]}" for r in rows[-3:]]
    longs = [r for d, r, _t in done if d > 0]; shorts = [r for d, r, _t in done if d < 0]
    if shorts:
        tr_lines.append(f"- {c['label']} totals: long {len(longs)} trades {sum(longs):+.2f}%, short {len(shorts)} trades {sum(shorts):+.2f}%")
    td = [(d, r) for d, r, t in done if f"{t:%Y-%m-%d}" == today]
    mk.append({"market": c["label"], "enabled": c["enabled"], "last_run_utc": f"{rows[-1][0]:%Y-%m-%d %H:%M}", "runs_24h": len(day),
               "entries_24h": ent, "errors_24h": len(er), "closed_trades": len(done), "win_pct": wr, "total_pct_after_fees": round(tot, 2),
               "open": ("short" if op[2] < 0 else "long") if op else None, "closed_today": len(td),
               "result_today_pct": round(sum(r for _, r in td), 2), "entries_today": sum(1 for r in rows if r[2] in ("buy", "short") and f"{r[0]:%Y-%m-%d}" == today),
               "last_trades_pct": [round(r, 2) for _, r, _t in done[-5:]]})
lines += ["", "## Raw log files (full history, one row per run)"] + [f"- {RAW}{c['log']}" for c in T.MARKETS.values()]
lines += ["", "## Errors in the last 24h (grouped)"] + ([f"- x{n} {m}: {t}" for (m, t), n in sorted(errs.items(), key=lambda x: -x[1])[:10]] or ["- none"])
lines += ["", "## OANDA 401 errors, last 24h", f"- count: {o401}" + (f"; request IDs for OANDA support: {', '.join(rid[-10:])}" if rid else "")]
lines += ["", "## Latest closed trades"] + (tr_lines or ["- none yet"])

# extra detail logs (data/): account snapshots, real fills, Gemini decisions
acc = {}
for l in data_rows("account.csv", 60):
    c = l.split(",")
    if len(c) >= 5:
        acc[c[1]] = f"{c[0]} UTC {c[1]}: balance {c[2]}, equity {c[3]}, free {c[4]}"
fills, decs = data_rows("fills.csv", 8), data_rows("decisions.csv", 5)
lines += ["", "## Account (latest hourly snapshot)"] + (["- " + v for v in acc.values()] or ["- none yet"])
lines += ["", "## Recent fills (decision price vs real fill; columns: " + T.FILL_HEADER + ")"] + (["- " + l[:170] for l in fills] or ["- none yet"])
lines += ["", "## Recent Gemini decisions"] + (["- " + l[:200] for l in decs] or ["- none yet"])
lines += ["", "## Data files", f"- {RAW}data/fills.csv", f"- {RAW}data/decisions.csv", f"- {RAW}data/account.csv", f"- {RAW}status.md", f"- {RAW}report.json"]
lines += ["", "## Latest log rows"] + tail
open("report.md", "w").write("\n".join(lines) + "\n")

# ---- status.md: the short version
last_run = max((m["last_run_utc"] for m in mk), default="never")
ago = None
if mk:
    ago = int((now - datetime.datetime.strptime(last_run, "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc)).total_seconds() / 60)
ct, wins = sum(m["closed_trades"] for m in mk), sum(round((m["win_pct"] or 0) * m["closed_trades"] / 100) for m in mk)
st = [f"# Status ({now:%Y-%m-%d %H:%M} UTC)",
      f"- last bot run: {last_run} UTC ({ago} min ago)" if ago is not None else "- no logs yet",
      f"- open now: {', '.join(m['market'] + ' ' + m['open'] for m in mk if m['open']) or 'none'}",
      f"- closed trades: {ct}, win {round(wins / ct * 100) if ct else '-'}%, sum of results {sum(m['total_pct_after_fees'] for m in mk):+.2f}% (sum of %, not account balance)",
      f"- errors last 24h: {sum(m['errors_24h'] for m in mk)} (OANDA 401: {o401})",
      "- per market (trades / win% / total after fees): " + "; ".join(f"{m['market']} {m['closed_trades']}/{m['win_pct'] if m['win_pct'] is not None else '-'}%/{m['total_pct_after_fees']:+.2f}%" for m in mk)]
st += [f"- {v}" for v in acc.values()]
st += ["- latest closed: " + (max(lastc)[1] if lastc else "none"), f"- full report: {RAW}report.md"]
open("status.md", "w").write("\n".join(st) + "\n")

# ---- report.json and one file per day
open("report.json", "w").write(json.dumps({"generated_utc": f"{now:%Y-%m-%d %H:%M}", "markets": mk, "oanda_401_24h": o401,
                                           "errors_24h": [{"market": m, "text": t, "count": n} for (m, t), n in errs.items()],
                                           "account": acc}, indent=1) + "\n")
os.makedirs("reports/daily", exist_ok=True)
dl = [f"# Day summary {today} (UTC, updated {now:%H:%M})", "", "| market | entries today | closed today | result today % | errors (24h) |", "|---|---|---|---|---|"]
dl += [f"| {m['market']} | {m['entries_today']} | {m['closed_today']} | {m['result_today_pct']:+.2f} | {m['errors_24h']} |" for m in mk]
open(f"reports/daily/{today}.md", "w").write("\n".join(dl) + "\n")
print("report.md, status.md, report.json written")
