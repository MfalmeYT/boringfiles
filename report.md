# Bot report (generated 2026-11-27 15:10 UTC)

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
| Bitcoin 15m | 11-27 15:10 | 1440 | 1 | 0 | 6 | 33 | -4.29 |  |
| USD/JPY | 11-27 15:10 | 1379 | 4 | 0 | 47 | 32 | -0.70 |  |
| GBP/USD | 11-27 15:10 | 1379 | 4 | 0 | 41 | 29 | -0.25 | yes |
| EUR/USD | 11-27 15:10 | 1379 | 3 | 0 | 43 | 40 | +0.35 |  |
| EUR/GBP | 11-27 15:10 | 1379 | 3 | 0 | 42 | 24 | -0.79 | yes |

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
- Bitcoin 15m: long +3.03%
- Bitcoin 15m: long -2.51%
- Bitcoin 15m: long -2.45%
- Bitcoin 15m: long +2.73%
- Bitcoin 15m: long -2.64%
- USD/JPY: long +0.00%
- USD/JPY: long -0.06%
- USD/JPY: short -0.05%
- USD/JPY: long +0.11%
- USD/JPY: long -0.06%
- USD/JPY totals: long 23 trades -0.50%, short 24 trades -0.20%
- GBP/USD: long -0.06%
- GBP/USD: long -0.10%
- GBP/USD: short -0.03%
- GBP/USD: long -0.02%
- GBP/USD: long -0.05%
- GBP/USD totals: long 21 trades -0.32%, short 20 trades +0.06%
- EUR/USD: long -0.04%
- EUR/USD: long +0.14%
- EUR/USD: short -0.07%
- EUR/USD: long +0.13%
- EUR/USD: short +0.20%
- EUR/USD totals: long 26 trades -0.38%, short 17 trades +0.73%
- EUR/GBP: short -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP: short -0.04%
- EUR/GBP: short +0.07%
- EUR/GBP totals: long 25 trades -0.48%, short 17 trades -0.32%

## Account (latest hourly snapshot)
- 2026-11-27 14:43 UTC AlpacaCrypto: balance 933.51, equity 978.24, free 933.51
- 2026-11-27 15:06 UTC Oanda: balance 674.4969, equity 676.2413, free 74.8888

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-27 08:40,EUR/USD,short,2721,1.09656,1.09614,-0.0383,10000.0,,10000,filled,conf 5
- 2026-11-27 09:58,USD/JPY,sell,broker,,159.517,,,,,filled,closed by broker stop/TP; P/L 4.6544
- 2026-11-27 11:06,EUR/GBP,short,2729,0.83516,0.83489,-0.0323,5000.0,,5000,filled,conf 4
- 2026-11-27 13:30,USD/JPY,buy,2737,159.552,159.559,0.0044,5000.0,,5000,filled,conf 4
- 2026-11-27 13:30,EUR/USD,cover,broker,,1.09441,,,,,filled,closed by broker stop/TP; P/L 17.3000
- 2026-11-27 14:35,USD/JPY,sell,broker,,159.449,,,,,filled,closed by broker stop/TP; P/L -3.4837
- 2026-11-27 14:35,GBP/USD,short,2745,1.31106,1.31159,0.0404,5000.0,,5000,filled,conf 4
- 2026-11-27 14:40,Bitcoin 15m,sell,a278da25-19c0-44bb-9810-41edd5899e34,60081.511,60188.81,0.1786,0.000716567,0.000716567,,filled,STOP LOSS (-2.2%)

## Recent Gemini decisions
- 2026-11-27 08:06,USD/JPY,buy,long,159.344,0.016,159.327,159.3051,159.2837,58.4,0.0499,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Solid trend alignment and RSI; but low 
- 2026-11-27 08:40,EUR/USD,short,short,1.09656,0.00015,1.097305,1.097452,1.097397,38.3,0.000578,3,5,a 0.16% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Downtrend intact wi
- 2026-11-27 11:06,EUR/GBP,short,short,0.83516,0.00013,0.835204,0.835614,0.836138,34.6,0.000287,3,4,a 0.10% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Favorable alignment
- 2026-11-27 13:30,USD/JPY,buy,long,159.552,0.015,159.4925,159.4608,159.3989,64.5,0.0549,3,4,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Strong trend and EMAs aligned; but RSI
- 2026-11-27 14:35,GBP/USD,short,short,1.31106,0.0002,1.311774,1.312157,1.312092,39.0,0.000736,3,4,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Downtrend intact wit

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-27 15:08 price 59025.94 no_trade score below 2
- Bitcoin 15m 11-27 15:09 price 59066.72 no_trade score below 2
- Bitcoin 15m 11-27 15:10 price 59084.04 no_trade score below 2
- USD/JPY 11-27 15:08 price 159.477 no_trade re-entry cooldown
- USD/JPY 11-27 15:09 price 159.477 no_trade re-entry cooldown
- USD/JPY 11-27 15:10 price 159.477 no_trade re-entry cooldown
- GBP/USD 11-27 15:08 price 1.31137 holding SHORT 0.0%
- GBP/USD 11-27 15:09 price 1.31137 holding SHORT 0.0%
- GBP/USD 11-27 15:10 price 1.31137 holding SHORT 0.0%
- EUR/USD 11-27 15:08 price 1.09498 no_trade re-entry cooldown
- EUR/USD 11-27 15:09 price 1.09498 no_trade re-entry cooldown
- EUR/USD 11-27 15:10 price 1.09498 no_trade re-entry cooldown
- EUR/GBP 11-27 15:08 price 0.83498 holding SHORT -0.0%
- EUR/GBP 11-27 15:09 price 0.83498 holding SHORT -0.0%
- EUR/GBP 11-27 15:10 price 0.83498 holding SHORT -0.0%
