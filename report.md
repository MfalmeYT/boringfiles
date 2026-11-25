# Bot report (generated 2026-11-25 01:31 UTC)

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
| Bitcoin 15m | 11-25 01:31 | 1440 | 0 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-25 01:31 | 1379 | 5 | 0 | 36 | 33 | -0.36 |  |
| GBP/USD | 11-25 01:31 | 1379 | 3 | 0 | 30 | 37 | +0.26 | yes |
| EUR/USD | 11-25 01:31 | 1379 | 3 | 0 | 34 | 35 | -0.15 |  |
| EUR/GBP | 11-25 01:31 | 1379 | 4 | 1 | 32 | 22 | -0.65 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc15.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x1 EUR/GBP: OANDA candles 504: temporary gateway error (HTML page)

## OANDA 401 errors, last 24h
- count: 0

## Latest closed trades
- Bitcoin 15m: long -2.45%
- Bitcoin 15m: long +3.03%
- Bitcoin 15m: long -2.51%
- Bitcoin 15m: long -2.45%
- USD/JPY: short -0.07%
- USD/JPY: long -0.09%
- USD/JPY: long -0.04%
- USD/JPY: short -0.14%
- USD/JPY: long -0.06%
- USD/JPY totals: long 16 trades -0.18%, short 20 trades -0.18%
- GBP/USD: long -0.05%
- GBP/USD: short +0.18%
- GBP/USD: short -0.02%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD totals: long 14 trades +0.11%, short 16 trades +0.15%
- EUR/USD: short +0.13%
- EUR/USD: long -0.06%
- EUR/USD: long +0.15%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD totals: long 21 trades -0.76%, short 13 trades +0.61%
- EUR/GBP: short -0.00%
- EUR/GBP: long -0.02%
- EUR/GBP: short -0.05%
- EUR/GBP: long -0.08%
- EUR/GBP: short -0.14%
- EUR/GBP totals: long 20 trades -0.48%, short 12 trades -0.17%

## Account (latest hourly snapshot)
- 2026-11-25 00:46 UTC AlpacaCrypto: balance 933.52, equity 977.19, free 933.52
- 2026-11-25 01:08 UTC Oanda: balance 743.2033, equity 741.1033, free 85.6333

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-24 16:11,USD/JPY,short,2312,159.082,159.075,-0.0044,1250.0,,1250,filled,conf 5
- 2026-11-24 18:10,EUR/USD,buy,2330,1.09734,1.09736,0.0018,1250.0,,1250,filled,conf 4
- 2026-11-24 18:43,USD/JPY,cover,broker,,159.312,,,,,filled,closed by broker stop/TP; P/L -1.8783
- 2026-11-24 18:43,EUR/GBP,short,2342,0.83614,0.83599,-0.0179,1250.0,,1250,filled,conf 5
- 2026-11-24 23:00,USD/JPY,buy,2356,159.29,159.291,0.0006,1250.0,,1250,filled,conf 4
- 2026-11-24 23:00,EUR/GBP,cover,broker,,0.83728,,,,,filled,closed by broker stop/TP; P/L -2.1359
- 2026-11-25 00:13,USD/JPY,sell,broker,,159.189,,,,,filled,closed by broker stop/TP; P/L -0.8089
- 2026-11-25 00:25,EUR/USD,sell,broker,,1.09585,,,,,filled,closed by broker stop/TP; P/L -1.8875

## Recent Gemini decisions
- 2026-11-24 15:12,GBP/USD,buy,long,1.31144,0.00017,1.310136,1.308833,1.307002,78.6,0.000871,2,2,+0.20% (take profit) or -0.13% (stop loss); set from recent volatility,RSI overbought at 78.6 indicates a
- 2026-11-24 16:11,USD/JPY,short,short,159.082,0.016,159.19,159.2055,159.1992,43.1,0.1186,3,5,a 0.22% fall (take profit) or a 0.15% rise (stop loss); set from recent volatility,Fresh EMA crossover and s
- 2026-11-24 18:10,EUR/USD,buy,long,1.09734,0.00016,1.096919,1.096436,1.094862,61.5,0.000755,3,4,+0.21% (take profit) or -0.14% (stop loss); set from recent volatility,Strong alignment with EMAs; but lo
- 2026-11-24 18:43,EUR/GBP,short,short,0.83614,0.00015,0.836328,0.83653,0.836646,38.7,0.000311,3,5,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Strong downtrend ali
- 2026-11-24 23:00,USD/JPY,buy,long,159.29,0.023,159.267,159.2485,159.225,56.4,0.0539,3,4,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Strong EMA alignment and trend; but tight

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 01:29 price 59417.69 no_trade score below 2
- Bitcoin 15m 11-25 01:30 price 59366.11 no_trade score below 2
- Bitcoin 15m 11-25 01:31 price 59305.53 no_trade score below 2
- USD/JPY 11-25 01:29 price 159.248 no_trade re-entry cooldown
- USD/JPY 11-25 01:30 price 159.299 no_trade re-entry cooldown
- USD/JPY 11-25 01:31 price 159.299 no_trade re-entry cooldown
- GBP/USD 11-25 01:29 price 1.31103 holding 0.0%
- GBP/USD 11-25 01:30 price 1.31068 holding -0.0%
- GBP/USD 11-25 01:31 price 1.31068 holding -0.0%
- EUR/USD 11-25 01:29 price 1.09572 no_trade re-entry cooldown
- EUR/USD 11-25 01:30 price 1.09563 no_trade re-entry cooldown
- EUR/USD 11-25 01:31 price 1.09563 no_trade re-entry cooldown
- EUR/GBP 11-25 01:29 price 0.83578 no_trade re-entry cooldown
- EUR/GBP 11-25 01:30 price 0.83594 no_trade re-entry cooldown
- EUR/GBP 11-25 01:31 price 0.83594 no_trade re-entry cooldown
