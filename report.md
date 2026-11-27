# Bot report (generated 2026-11-27 01:44 UTC)

## Settings (read from trader.py)
- trading enabled: True; shorting enabled: True; max open positions: 3
- entry needs 2 of 3 checks (EMA 9/21/50, RSI 45-70; short = mirror) plus Gemini confidence 1-6; model gemini-3.6-flash
- Bitcoin 15m (on): alpaca, 15Min candles, stop 2.0% / target 3.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 120 min, signal exit OFF, time stop 48h, 1Hour trend filter, pause 12h after 3 losses, long only
- USD/JPY (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- GBP/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/GBP (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short

## Markets (last 24h unless noted)

| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |
|---|---|---|---|---|---|---|---|---|
| Bitcoin 15m | 11-27 01:44 | 1440 | 0 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-27 01:44 | 1379 | 2 | 0 | 44 | 32 | -0.69 |  |
| GBP/USD | 11-27 01:44 | 1379 | 4 | 0 | 39 | 31 | -0.18 |  |
| EUR/USD | 11-27 01:44 | 1379 | 3 | 0 | 40 | 38 | +0.09 | yes |
| EUR/GBP | 11-27 01:44 | 1379 | 4 | 0 | 41 | 22 | -0.86 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc15.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- none

## OANDA 401 errors, last 24h
- count: 0

## Latest closed trades
- Bitcoin 15m: long -2.45%
- Bitcoin 15m: long +3.03%
- Bitcoin 15m: long -2.51%
- Bitcoin 15m: long -2.45%
- USD/JPY: short +0.23%
- USD/JPY: short -0.06%
- USD/JPY: long -0.08%
- USD/JPY: long +0.00%
- USD/JPY: long -0.06%
- USD/JPY totals: long 21 trades -0.54%, short 23 trades -0.15%
- GBP/USD: long -0.04%
- GBP/USD: short -0.05%
- GBP/USD: long -0.06%
- GBP/USD: long -0.10%
- GBP/USD: short -0.03%
- GBP/USD totals: long 19 trades -0.24%, short 20 trades +0.06%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD: long -0.08%
- EUR/USD: long -0.04%
- EUR/USD: long +0.14%
- EUR/USD totals: long 25 trades -0.51%, short 15 trades +0.60%
- EUR/GBP: short -0.11%
- EUR/GBP: short -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP: short -0.04%
- EUR/GBP totals: long 25 trades -0.48%, short 16 trades -0.38%

## Account (latest hourly snapshot)
- 2026-11-27 00:57 UTC AlpacaCrypto: balance 889.38, equity 978, free 889.38
- 2026-11-27 01:20 UTC Oanda: balance 666.2180, equity 669.1180, free 449.8160

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-26 16:08,EUR/GBP,sell,broker,,0.83684,,,,,filled,closed by broker stop/TP; P/L -3.8403
- 2026-11-26 17:06,EUR/USD,short,2642,1.09708,1.09695,-0.0118,10000.0,,10000,filled,conf 4
- 2026-11-26 17:15,USD/JPY,buy,2648,159.31,159.318,0.005,5000.0,,5000,filled,conf 4
- 2026-11-26 23:00,USD/JPY,sell,broker,,159.211,,,,,filled,closed by broker stop/TP; P/L -3.3929
- 2026-11-26 23:04,GBP/USD,short,2657,1.31054,1.3103,-0.0183,5000.0,,5000,filled,conf 4
- 2026-11-26 23:40,GBP/USD,cover,broker,,1.31087,,,,,filled,closed by broker stop/TP; P/L -2.8500
- 2026-11-26 23:58,EUR/GBP,short,2665,0.83693,0.83691,-0.0024,5000.0,,5000,filled,conf 3
- 2026-11-27 00:53,EUR/GBP,cover,broker,,0.83724,,,,,filled,closed by broker stop/TP; P/L -2.1822

## Recent Gemini decisions
- 2026-11-26 14:21,GBP/USD,buy,long,1.3119,0.00018,1.311105,1.310862,1.310693,63.2,0.000628,3,5,+0.14% (take profit) or -0.10% (stop loss); set from recent volatility,Strong EMA crossover and momentum f
- 2026-11-26 17:06,EUR/USD,short,short,1.09708,0.00016,1.097364,1.09748,1.097305,43.5,0.000456,3,4,a 0.12% fall (take profit) or a 0.08% rise (stop loss); set from recent volatility,Strong bearish align
- 2026-11-26 17:15,USD/JPY,buy,long,159.31,0.014,159.2832,159.2623,159.2285,61.8,0.0406,3,4,+0.08% (take profit) or -0.05% (stop loss); set from recent volatility,Strong trend alignment and score; but R
- 2026-11-26 23:04,GBP/USD,short,short,1.31054,0.0002,1.310679,1.310704,1.310738,44.9,0.00027,3,4,a 0.06% fall (take profit) or a 0.04% rise (stop loss); set from recent volatility,Good trend alignment 
- 2026-11-26 23:58,EUR/GBP,short,short,0.83693,0.00012,0.837,0.837011,0.837043,46.0,0.000167,3,3,a 0.06% fall (take profit) or a 0.04% rise (stop loss); set from recent volatility,Weak momentum; flat EM

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-27 01:42 price 60604.52 holding 1.5%
- Bitcoin 15m 11-27 01:43 price 60607.75 holding 1.6%
- Bitcoin 15m 11-27 01:44 price 60600.03 holding 1.5%
- USD/JPY 11-27 01:42 price 159.297 no_trade re-entry cooldown
- USD/JPY 11-27 01:43 price 159.297 no_trade re-entry cooldown
- USD/JPY 11-27 01:44 price 159.297 no_trade re-entry cooldown
- GBP/USD 11-27 01:42 price 1.31021 no_trade re-entry cooldown
- GBP/USD 11-27 01:43 price 1.31021 no_trade re-entry cooldown
- GBP/USD 11-27 01:44 price 1.31021 no_trade re-entry cooldown
- EUR/USD 11-27 01:42 price 1.09657 holding SHORT 0.0%
- EUR/USD 11-27 01:43 price 1.09657 holding SHORT 0.0%
- EUR/USD 11-27 01:44 price 1.09657 holding SHORT 0.0%
- EUR/GBP 11-27 01:42 price 0.83694 no_trade re-entry cooldown
- EUR/GBP 11-27 01:43 price 0.83694 no_trade re-entry cooldown
- EUR/GBP 11-27 01:44 price 0.83694 no_trade re-entry cooldown
