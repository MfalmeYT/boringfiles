# Bot report (generated 2026-11-17 03:44 UTC)

## Settings (read from trader.py)
- trading enabled: True; shorting enabled: True; max open positions: 3
- entry needs 2 of 3 checks (EMA 9/21/50, RSI 45-70; short = mirror) plus Gemini confidence 1-6; model gemini-3.6-flash
- Bitcoin (on): alpaca, 5Min candles, stop 2.0% / target 2.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 60 min, long only
- Gold USD (on): alpaca, 15Min candles, stop 1.0% / target 1.5%, size $45, min confidence 3, min hold 90 min, re-entry pause 180 min, long only
- USD/JPY (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short
- GBP/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short
- EUR/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short
- EUR/GBP (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short

## Markets (last 24h unless noted)

| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |
|---|---|---|---|---|---|---|---|---|
| Bitcoin | 11-17 03:44 | 1436 | 6 | 1 | 22 | 5 | -14.64 | yes |
| Gold USD | 11-17 03:44 | 1436 | 2 | 2 | 7 | 14 | -3.29 | yes |
| USD/JPY | 11-17 03:44 | 1381 | 3 | 110 | 16 | 31 | -0.04 |  |
| GBP/USD | 11-17 03:44 | 1379 | 1 | 72 | 14 | 36 | -0.14 |  |
| EUR/USD | 11-17 03:44 | 1379 | 3 | 75 | 16 | 38 | -0.03 | yes |
| EUR/GBP | 11-17 03:44 | 1378 | 5 | 63 | 17 | 18 | -0.53 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x71 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x50 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x44 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x42 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x20 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x18 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x17 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x15 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x11 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x11 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -1.02%
- Bitcoin: long -0.82%
- Bitcoin: long -0.97%
- Bitcoin: long -0.25%
- Bitcoin: long -0.37%
- Gold USD: long -0.56%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- USD/JPY: short +0.16%
- USD/JPY: short +0.18%
- USD/JPY: short -0.07%
- USD/JPY: short -0.03%
- USD/JPY: short -0.07%
- USD/JPY totals: long 10 trades -0.18%, short 6 trades +0.14%
- GBP/USD: short -0.07%
- GBP/USD: long -0.06%
- GBP/USD: short -0.03%
- GBP/USD: short -0.08%
- GBP/USD: short -0.03%
- GBP/USD totals: long 9 trades +0.13%, short 5 trades -0.27%
- EUR/USD: short +0.18%
- EUR/USD: short +0.05%
- EUR/USD: short -0.09%
- EUR/USD: short +0.18%
- EUR/USD: short -0.05%
- EUR/USD totals: long 11 trades -0.30%, short 5 trades +0.27%
- EUR/GBP: short -0.10%
- EUR/GBP: short +0.03%
- EUR/GBP: long -0.04%
- EUR/GBP: long +0.02%
- EUR/GBP: short -0.03%
- EUR/GBP totals: long 13 trades -0.39%, short 4 trades -0.14%

## Latest log rows
- Bitcoin 11-17 03:42 price 64913 holding 0.3%
- Bitcoin 11-17 03:43 price 64987.76 holding 0.4%
- Bitcoin 11-17 03:44 price 65012.5 holding 0.4%
- Gold USD 11-17 03:42 price 3860.6 holding -0.4%
- Gold USD 11-17 03:43 price 3858.18 holding -0.5%
- Gold USD 11-17 03:44 price 3858.18 holding -0.5%
- USD/JPY 11-17 03:42 price 159.366 no_trade re-entry cooldown
- USD/JPY 11-17 03:43 price 159.366 no_trade re-entry cooldown
- USD/JPY 11-17 03:44 price 159.366 no_trade re-entry cooldown
- GBP/USD 11-17 03:42 price 1.3194 no_trade re-entry cooldown
- GBP/USD 11-17 03:43 price 1.3194 no_trade re-entry cooldown
- GBP/USD 11-17 03:44 price 1.3194 no_trade re-entry cooldown
- EUR/USD 11-17 03:42 price 1.10066 holding -0.0%
- EUR/USD 11-17 03:43 price 1.10066 holding -0.0%
- EUR/USD 11-17 03:44 price 1.10066 holding -0.0%
- EUR/GBP 11-17 03:42 price 0.83424 no_trade re-entry cooldown
- EUR/GBP 11-17 03:43 price 0.83424 no_trade re-entry cooldown
- EUR/GBP 11-17 03:44 price 0.83424 no_trade re-entry cooldown
