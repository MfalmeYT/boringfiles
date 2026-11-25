# Bot report (generated 2026-11-25 05:43 UTC)

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
| Bitcoin 15m | 11-25 05:43 | 1440 | 0 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-25 05:43 | 1379 | 5 | 0 | 37 | 32 | -0.50 |  |
| GBP/USD | 11-25 05:43 | 1379 | 2 | 0 | 31 | 35 | +0.17 |  |
| EUR/USD | 11-25 05:43 | 1379 | 4 | 0 | 34 | 35 | -0.15 | yes |
| EUR/GBP | 11-25 05:43 | 1379 | 4 | 1 | 33 | 21 | -0.67 |  |

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
- USD/JPY: long -0.09%
- USD/JPY: long -0.04%
- USD/JPY: short -0.14%
- USD/JPY: long -0.06%
- USD/JPY: short -0.14%
- USD/JPY totals: long 16 trades -0.18%, short 21 trades -0.32%
- GBP/USD: short +0.18%
- GBP/USD: short -0.02%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD totals: long 15 trades +0.02%, short 16 trades +0.15%
- EUR/USD: short +0.13%
- EUR/USD: long -0.06%
- EUR/USD: long +0.15%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD totals: long 21 trades -0.76%, short 13 trades +0.61%
- EUR/GBP: long -0.02%
- EUR/GBP: short -0.05%
- EUR/GBP: long -0.08%
- EUR/GBP: short -0.14%
- EUR/GBP: short -0.02%
- EUR/GBP totals: long 20 trades -0.48%, short 13 trades -0.20%

## Account (latest hourly snapshot)
- 2026-11-25 05:04 UTC Oanda: balance 723.4227, equity 727.5727, free 618.1397
- 2026-11-25 05:41 UTC AlpacaCrypto: balance 933.52, equity 976.96, free 933.52

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 00:13,USD/JPY,sell,broker,,159.189,,,,,filled,closed by broker stop/TP; P/L -0.8089
- 2026-11-25 00:25,EUR/USD,sell,broker,,1.09585,,,,,filled,closed by broker stop/TP; P/L -1.8875
- 2026-11-25 02:00,EUR/GBP,short,2370,0.83608,0.83602,-0.0072,1250.0,,1250,filled,conf 3
- 2026-11-25 03:00,GBP/USD,sell,2376,1.31023,1.31004,-0.0145,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-25 03:13,USD/JPY,short,2378,159.124,159.196,0.0452,10000.0,,10000,filled,conf 4
- 2026-11-25 03:25,EUR/USD,short,2384,1.09523,1.09532,0.0082,5000.0,,5000,filled,conf 4
- 2026-11-25 03:30,EUR/GBP,cover,2390,0.83625,0.83634,0.0108,1250.0,1250.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-25 04:26,USD/JPY,cover,broker,,159.353,,,,,filled,closed by broker stop/TP; P/L -9.9514

## Recent Gemini decisions
- 2026-11-24 18:43,EUR/GBP,short,short,0.83614,0.00015,0.836328,0.83653,0.836646,38.7,0.000311,3,5,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Strong downtrend ali
- 2026-11-24 23:00,USD/JPY,buy,long,159.29,0.023,159.267,159.2485,159.225,56.4,0.0539,3,4,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Strong EMA alignment and trend; but tight
- 2026-11-25 02:00,EUR/GBP,short,short,0.83608,0.00012,0.836023,0.836076,0.836243,49.0,0.000211,3,3,a 0.08% fall (take profit) or a 0.05% rise (stop loss); set from recent volatility,Flat price action a
- 2026-11-25 03:13,USD/JPY,short,short,159.124,0.013,159.2356,159.2504,159.2376,36.9,0.0784,3,4,a 0.15% fall (take profit) or a 0.10% rise (stop loss); set from recent volatility,Strong bearish alignmen
- 2026-11-25 03:25,EUR/USD,short,short,1.09523,0.00016,1.095768,1.096004,1.095899,35.6,0.000407,3,4,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Strong downtrend al

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 05:41 price 58953.46 no_trade score below 2
- Bitcoin 15m 11-25 05:42 price 58936.93 no_trade score below 2
- Bitcoin 15m 11-25 05:43 price 58940.12 no_trade score below 2
- USD/JPY 11-25 05:41 price 159.472 no_trade re-entry cooldown
- USD/JPY 11-25 05:42 price 159.472 no_trade re-entry cooldown
- USD/JPY 11-25 05:43 price 159.472 no_trade re-entry cooldown
- GBP/USD 11-25 05:41 price 1.3089 no_trade re-entry cooldown
- GBP/USD 11-25 05:42 price 1.3089 no_trade re-entry cooldown
- GBP/USD 11-25 05:43 price 1.3089 no_trade re-entry cooldown
- EUR/USD 11-25 05:41 price 1.09452 holding SHORT 0.1%
- EUR/USD 11-25 05:42 price 1.09452 holding SHORT 0.1%
- EUR/USD 11-25 05:43 price 1.09452 holding SHORT 0.1%
- EUR/GBP 11-25 05:41 price 0.83622 no_trade re-entry cooldown
- EUR/GBP 11-25 05:42 price 0.83622 no_trade re-entry cooldown
- EUR/GBP 11-25 05:43 price 0.83622 no_trade re-entry cooldown
