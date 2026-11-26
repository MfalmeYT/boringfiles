# Bot report (generated 2026-11-26 23:32 UTC)

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
| Bitcoin 15m | 11-26 23:32 | 1440 | 0 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-26 23:32 | 1379 | 3 | 0 | 44 | 32 | -0.69 |  |
| GBP/USD | 11-26 23:32 | 1379 | 5 | 0 | 38 | 32 | -0.15 | yes |
| EUR/USD | 11-26 23:32 | 1379 | 3 | 0 | 40 | 38 | +0.09 | yes |
| EUR/GBP | 11-26 23:32 | 1379 | 3 | 0 | 40 | 22 | -0.82 |  |

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
- GBP/USD: long -0.06%
- GBP/USD: long -0.04%
- GBP/USD: short -0.05%
- GBP/USD: long -0.06%
- GBP/USD: long -0.10%
- GBP/USD totals: long 19 trades -0.24%, short 19 trades +0.09%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD: long -0.08%
- EUR/USD: long -0.04%
- EUR/USD: long +0.14%
- EUR/USD totals: long 25 trades -0.51%, short 15 trades +0.60%
- EUR/GBP: long -0.11%
- EUR/GBP: short -0.11%
- EUR/GBP: short -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP totals: long 25 trades -0.48%, short 15 trades -0.34%

## Account (latest hourly snapshot)
- 2026-11-26 22:59 UTC AlpacaCrypto: balance 889.38, equity 977.95, free 889.38
- 2026-11-26 23:22 UTC Oanda: balance 671.2502, equity 666.4502, free 119.3952

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-26 14:15,USD/JPY,sell,2630,159.186,159.183,-0.0019,5000.0,5000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-26 14:21,GBP/USD,buy,2634,1.3119,1.31188,-0.0015,5000.0,,5000,filled,conf 5
- 2026-11-26 14:44,GBP/USD,sell,broker,,1.31061,,,,,filled,closed by broker stop/TP; P/L -6.3500
- 2026-11-26 16:08,EUR/GBP,sell,broker,,0.83684,,,,,filled,closed by broker stop/TP; P/L -3.8403
- 2026-11-26 17:06,EUR/USD,short,2642,1.09708,1.09695,-0.0118,10000.0,,10000,filled,conf 4
- 2026-11-26 17:15,USD/JPY,buy,2648,159.31,159.318,0.005,5000.0,,5000,filled,conf 4
- 2026-11-26 23:00,USD/JPY,sell,broker,,159.211,,,,,filled,closed by broker stop/TP; P/L -3.3929
- 2026-11-26 23:04,GBP/USD,short,2657,1.31054,1.3103,-0.0183,5000.0,,5000,filled,conf 4

## Recent Gemini decisions
- 2026-11-26 14:06,EUR/GBP,buy,long,0.83733,0.00013,0.837407,0.837268,0.837099,53.0,0.000292,3,3,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Price is capped under EMA9 with re
- 2026-11-26 14:21,GBP/USD,buy,long,1.3119,0.00018,1.311105,1.310862,1.310693,63.2,0.000628,3,5,+0.14% (take profit) or -0.10% (stop loss); set from recent volatility,Strong EMA crossover and momentum f
- 2026-11-26 17:06,EUR/USD,short,short,1.09708,0.00016,1.097364,1.09748,1.097305,43.5,0.000456,3,4,a 0.12% fall (take profit) or a 0.08% rise (stop loss); set from recent volatility,Strong bearish align
- 2026-11-26 17:15,USD/JPY,buy,long,159.31,0.014,159.2832,159.2623,159.2285,61.8,0.0406,3,4,+0.08% (take profit) or -0.05% (stop loss); set from recent volatility,Strong trend alignment and score; but R
- 2026-11-26 23:04,GBP/USD,short,short,1.31054,0.0002,1.310679,1.310704,1.310738,44.9,0.00027,3,4,a 0.06% fall (take profit) or a 0.04% rise (stop loss); set from recent volatility,Good trend alignment 

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-26 23:30 price 60383.83 holding 1.2%
- Bitcoin 15m 11-26 23:31 price 60413.18 holding 1.2%
- Bitcoin 15m 11-26 23:32 price 60426.9 holding 1.2%
- USD/JPY 11-26 23:30 price 159.27 no_trade re-entry cooldown
- USD/JPY 11-26 23:31 price 159.27 no_trade re-entry cooldown
- USD/JPY 11-26 23:32 price 159.27 no_trade re-entry cooldown
- GBP/USD 11-26 23:30 price 1.31062 holding SHORT -0.0%
- GBP/USD 11-26 23:31 price 1.31062 holding SHORT -0.0%
- GBP/USD 11-26 23:32 price 1.31062 holding SHORT -0.0%
- EUR/USD 11-26 23:30 price 1.09704 holding SHORT -0.0%
- EUR/USD 11-26 23:31 price 1.09704 holding SHORT -0.0%
- EUR/USD 11-26 23:32 price 1.09704 holding SHORT -0.0%
- EUR/GBP 11-26 23:30 price 0.83702 no_trade max 3 open positions reached
- EUR/GBP 11-26 23:31 price 0.83702 no_trade max 3 open positions reached
- EUR/GBP 11-26 23:32 price 0.83702 no_trade max 3 open positions reached
