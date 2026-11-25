# Bot report (generated 2026-11-25 07:38 UTC)

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
| Bitcoin 15m | 11-25 07:38 | 1440 | 0 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-25 07:38 | 1379 | 6 | 0 | 38 | 32 | -0.69 |  |
| GBP/USD | 11-25 07:38 | 1379 | 3 | 0 | 31 | 35 | +0.17 | yes |
| EUR/USD | 11-25 07:38 | 1379 | 4 | 0 | 35 | 37 | -0.05 |  |
| EUR/GBP | 11-25 07:38 | 1379 | 5 | 1 | 33 | 21 | -0.67 | yes |

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
- USD/JPY: long -0.04%
- USD/JPY: short -0.14%
- USD/JPY: long -0.06%
- USD/JPY: short -0.14%
- USD/JPY: long -0.18%
- USD/JPY totals: long 17 trades -0.37%, short 21 trades -0.32%
- GBP/USD: short +0.18%
- GBP/USD: short -0.02%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD totals: long 15 trades +0.02%, short 16 trades +0.15%
- EUR/USD: long -0.06%
- EUR/USD: long +0.15%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD: short +0.10%
- EUR/USD totals: long 21 trades -0.76%, short 14 trades +0.71%
- EUR/GBP: long -0.02%
- EUR/GBP: short -0.05%
- EUR/GBP: long -0.08%
- EUR/GBP: short -0.14%
- EUR/GBP: short -0.02%
- EUR/GBP totals: long 20 trades -0.48%, short 13 trades -0.20%

## Account (latest hourly snapshot)
- 2026-11-25 06:40 UTC AlpacaCrypto: balance 933.52, equity 976.95, free 933.52
- 2026-11-25 07:02 UTC Oanda: balance 729.5227, equity 732.5573, free 132.2948

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 03:25,EUR/USD,short,2384,1.09523,1.09532,0.0082,5000.0,,5000,filled,conf 4
- 2026-11-25 03:30,EUR/GBP,cover,2390,0.83625,0.83634,0.0108,1250.0,1250.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-25 04:26,USD/JPY,cover,broker,,159.353,,,,,filled,closed by broker stop/TP; P/L -9.9514
- 2026-11-25 06:00,GBP/USD,short,2396,1.3085,1.30831,-0.0145,5000.0,,5000,filled,conf 2
- 2026-11-25 06:02,EUR/USD,cover,broker,,1.0941,,,,,filled,closed by broker stop/TP; P/L 6.1000
- 2026-11-25 06:31,EUR/GBP,buy,2404,0.83608,0.83619,0.0132,5000.0,,5000,filled,conf 3
- 2026-11-25 07:26,USD/JPY,buy,2412,159.298,159.167,-0.0822,2500.0,,2500,filled,conf 2
- 2026-11-25 07:38,USD/JPY,sell,broker,,159.007,,,,,filled,closed by broker stop/TP; P/L -2.5406

## Recent Gemini decisions
- 2026-11-25 03:13,USD/JPY,short,short,159.124,0.013,159.2356,159.2504,159.2376,36.9,0.0784,3,4,a 0.15% fall (take profit) or a 0.10% rise (stop loss); set from recent volatility,Strong bearish alignmen
- 2026-11-25 03:25,EUR/USD,short,short,1.09523,0.00016,1.095768,1.096004,1.095899,35.6,0.000407,3,4,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Strong downtrend al
- 2026-11-25 06:00,GBP/USD,short,short,1.3085,0.00017,1.308992,1.30963,1.309994,26.6,0.000457,2,2,a 0.10% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,RSI at 26.6 indicates
- 2026-11-25 06:31,EUR/GBP,buy,long,0.83608,0.00015,0.836161,0.836144,0.836194,47.1,0.0002,2,3,+0.07% (take profit) or -0.05% (stop loss); set from recent volatility,Price is capped by EMAs despite neut
- 2026-11-25 07:26,USD/JPY,buy,long,159.298,0.014,159.3531,159.3363,159.3003,47.1,0.0789,2,2,+0.15% (take profit) or -0.10% (stop loss); set from recent volatility,Downtrend intact; price below all EMAs

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 07:36 price 58943.54 no_trade score below 2
- Bitcoin 15m 11-25 07:37 price 58628.89 no_trade score below 2
- Bitcoin 15m 11-25 07:38 price 58571.4 no_trade score below 2
- USD/JPY 11-25 07:36 price 159.126 holding -0.0%
- USD/JPY 11-25 07:37 price 159.126 holding -0.0%
- USD/JPY 11-25 07:38 price 159.007 sell closed by broker stop/TP; P/L -2.5406
- GBP/USD 11-25 07:36 price 1.30757 holding SHORT 0.1%
- GBP/USD 11-25 07:37 price 1.30757 holding SHORT 0.1%
- GBP/USD 11-25 07:38 price 1.30757 holding SHORT 0.1%
- EUR/USD 11-25 07:36 price 1.09348 no_trade re-entry cooldown
- EUR/USD 11-25 07:37 price 1.09348 no_trade re-entry cooldown
- EUR/USD 11-25 07:38 price 1.09348 no_trade re-entry cooldown
- EUR/GBP 11-25 07:36 price 0.8363 holding 0.0%
- EUR/GBP 11-25 07:37 price 0.8363 holding 0.0%
- EUR/GBP 11-25 07:38 price 0.8363 holding 0.0%
