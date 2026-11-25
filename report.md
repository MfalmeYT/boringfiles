# Bot report (generated 2026-11-25 09:36 UTC)

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
| Bitcoin 15m | 11-25 09:36 | 1440 | 0 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-25 09:36 | 1379 | 5 | 0 | 38 | 32 | -0.69 |  |
| GBP/USD | 11-25 09:36 | 1379 | 3 | 0 | 32 | 38 | +0.28 |  |
| EUR/USD | 11-25 09:36 | 1379 | 5 | 0 | 35 | 37 | -0.05 | yes |
| EUR/GBP | 11-25 09:36 | 1379 | 4 | 1 | 34 | 24 | -0.59 |  |

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
- GBP/USD: short -0.02%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD: short +0.11%
- GBP/USD totals: long 15 trades +0.02%, short 17 trades +0.26%
- EUR/USD: long -0.06%
- EUR/USD: long +0.15%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD: short +0.10%
- EUR/USD totals: long 21 trades -0.76%, short 14 trades +0.71%
- EUR/GBP: short -0.05%
- EUR/GBP: long -0.08%
- EUR/GBP: short -0.14%
- EUR/GBP: short -0.02%
- EUR/GBP: long +0.08%
- EUR/GBP totals: long 21 trades -0.39%, short 13 trades -0.20%

## Account (latest hourly snapshot)
- 2026-11-25 08:38 UTC AlpacaCrypto: balance 933.52, equity 976.92, free 933.52
- 2026-11-25 09:00 UTC Oanda: balance 733.3821, equity 736.1287, free 462.5187

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 06:00,GBP/USD,short,2396,1.3085,1.30831,-0.0145,5000.0,,5000,filled,conf 2
- 2026-11-25 06:02,EUR/USD,cover,broker,,1.0941,,,,,filled,closed by broker stop/TP; P/L 6.1000
- 2026-11-25 06:31,EUR/GBP,buy,2404,0.83608,0.83619,0.0132,5000.0,,5000,filled,conf 3
- 2026-11-25 07:26,USD/JPY,buy,2412,159.298,159.167,-0.0822,2500.0,,2500,filled,conf 2
- 2026-11-25 07:38,USD/JPY,sell,broker,,159.007,,,,,filled,closed by broker stop/TP; P/L -2.5406
- 2026-11-25 08:00,GBP/USD,cover,broker,,1.30703,,,,,filled,closed by broker stop/TP; P/L 6.4000
- 2026-11-25 09:02,EUR/USD,short,2420,1.0943,1.09432,0.0018,10000.0,,10000,filled,conf 4
- 2026-11-25 09:25,EUR/GBP,sell,broker,,0.83679,,,,,filled,closed by broker stop/TP; P/L 3.8824

## Recent Gemini decisions
- 2026-11-25 03:25,EUR/USD,short,short,1.09523,0.00016,1.095768,1.096004,1.095899,35.6,0.000407,3,4,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Strong downtrend al
- 2026-11-25 06:00,GBP/USD,short,short,1.3085,0.00017,1.308992,1.30963,1.309994,26.6,0.000457,2,2,a 0.10% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,RSI at 26.6 indicates
- 2026-11-25 06:31,EUR/GBP,buy,long,0.83608,0.00015,0.836161,0.836144,0.836194,47.1,0.0002,2,3,+0.07% (take profit) or -0.05% (stop loss); set from recent volatility,Price is capped by EMAs despite neut
- 2026-11-25 07:26,USD/JPY,buy,long,159.298,0.014,159.3531,159.3363,159.3003,47.1,0.0789,2,2,+0.15% (take profit) or -0.10% (stop loss); set from recent volatility,Downtrend intact; price below all EMAs
- 2026-11-25 09:02,EUR/USD,short,short,1.0943,0.00016,1.093952,1.094202,1.094787,48.8,0.000582,3,4,a 0.16% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,All checks align; bu

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 09:34 price 58852.4 no_trade score below 2
- Bitcoin 15m 11-25 09:35 price 58826.5 no_trade score below 2
- Bitcoin 15m 11-25 09:36 price 58805.18 no_trade score below 2
- USD/JPY 11-25 09:34 price 159.31 no_trade re-entry cooldown
- USD/JPY 11-25 09:35 price 159.31 no_trade re-entry cooldown
- USD/JPY 11-25 09:36 price 159.31 no_trade re-entry cooldown
- GBP/USD 11-25 09:34 price 1.30652 no_trade re-entry cooldown
- GBP/USD 11-25 09:35 price 1.30652 no_trade re-entry cooldown
- GBP/USD 11-25 09:36 price 1.30652 no_trade re-entry cooldown
- EUR/USD 11-25 09:34 price 1.09339 holding SHORT 0.1%
- EUR/USD 11-25 09:35 price 1.09339 holding SHORT 0.1%
- EUR/USD 11-25 09:36 price 1.09339 holding SHORT 0.1%
- EUR/GBP 11-25 09:34 price 0.8369 no_trade re-entry cooldown
- EUR/GBP 11-25 09:35 price 0.8369 no_trade re-entry cooldown
- EUR/GBP 11-25 09:36 price 0.8369 no_trade re-entry cooldown
