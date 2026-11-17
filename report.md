# Bot report (generated 2026-11-17 12:19 UTC)

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
| Bitcoin | 11-17 12:19 | 1440 | 4 | 0 | 23 | 4 | -15.11 |  |
| Gold USD | 11-17 12:19 | 1440 | 1 | 0 | 8 | 12 | -3.84 |  |
| USD/JPY | 11-17 12:19 | 1385 | 4 | 70 | 17 | 29 | -0.15 | yes |
| GBP/USD | 11-17 12:19 | 1383 | 1 | 48 | 15 | 33 | -0.15 |  |
| EUR/USD | 11-17 12:19 | 1383 | 4 | 50 | 17 | 35 | -0.12 | yes |
| EUR/GBP | 11-17 12:19 | 1382 | 5 | 40 | 18 | 17 | -0.54 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x45 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x33 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x32 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x27 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x13 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x11 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x11 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x10 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x7 EUR/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x7 EUR/GBP: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.82%
- Bitcoin: long -0.97%
- Bitcoin: long -0.25%
- Bitcoin: long -0.37%
- Bitcoin: long -0.47%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- Gold USD: long -0.56%
- USD/JPY: short +0.18%
- USD/JPY: short -0.07%
- USD/JPY: short -0.03%
- USD/JPY: short -0.07%
- USD/JPY: short -0.11%
- USD/JPY totals: long 10 trades -0.18%, short 7 trades +0.03%
- GBP/USD: long -0.06%
- GBP/USD: short -0.03%
- GBP/USD: short -0.08%
- GBP/USD: short -0.03%
- GBP/USD: long -0.01%
- GBP/USD totals: long 10 trades +0.12%, short 5 trades -0.27%
- EUR/USD: short +0.05%
- EUR/USD: short -0.09%
- EUR/USD: short +0.18%
- EUR/USD: short -0.05%
- EUR/USD: long -0.09%
- EUR/USD totals: long 12 trades -0.39%, short 5 trades +0.27%
- EUR/GBP: short +0.03%
- EUR/GBP: long -0.04%
- EUR/GBP: long +0.02%
- EUR/GBP: short -0.03%
- EUR/GBP: short -0.00%
- EUR/GBP totals: long 13 trades -0.39%, short 5 trades -0.14%

## Latest log rows
- Bitcoin 11-17 12:17 price 64806.19 no_trade max 3 open positions reached
- Bitcoin 11-17 12:18 price 64804.22 no_trade max 3 open positions reached
- Bitcoin 11-17 12:19 price 64819.07 no_trade max 3 open positions reached
- Gold USD 11-17 12:17 price 3850.63 no_trade score below 2
- Gold USD 11-17 12:18 price 3852.18 no_trade score below 2
- Gold USD 11-17 12:19 price 3852.18 no_trade score below 2
- USD/JPY 11-17 12:17 price 159.242 holding SHORT -0.1%
- USD/JPY 11-17 12:18 price 159.242 holding SHORT -0.1%
- USD/JPY 11-17 12:19 price 159.242 holding SHORT -0.1%
- GBP/USD 11-17 12:17 price 1.31932 no_trade re-entry cooldown
- GBP/USD 11-17 12:18 price 1.31932 no_trade re-entry cooldown
- GBP/USD 11-17 12:19 price 1.31932 no_trade re-entry cooldown
- EUR/USD 11-17 12:17 price 1.09922 holding SHORT -0.0%
- EUR/USD 11-17 12:18 price 1.09922 holding SHORT -0.0%
- EUR/USD 11-17 12:19 price 1.09922 holding SHORT -0.0%
- EUR/GBP 11-17 12:17 price 0.83318 holding SHORT 0.0%
- EUR/GBP 11-17 12:18 price 0.83318 holding SHORT 0.0%
- EUR/GBP 11-17 12:19 price 0.83318 holding SHORT 0.0%
