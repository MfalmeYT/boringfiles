# Bot report (generated 2026-11-17 23:05 UTC)

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
| Bitcoin | 11-17 23:05 | 1440 | 3 | 0 | 24 | 4 | -15.79 | yes |
| Gold USD | 11-17 23:05 | 1440 | 2 | 0 | 9 | 11 | -4.61 |  |
| USD/JPY | 11-17 23:05 | 1379 | 4 | 10 | 19 | 26 | -0.38 | yes |
| GBP/USD | 11-17 23:05 | 1379 | 2 | 9 | 16 | 31 | -0.26 |  |
| EUR/USD | 11-17 23:05 | 1379 | 4 | 8 | 19 | 37 | -0.01 |  |
| EUR/GBP | 11-17 23:05 | 1379 | 2 | 6 | 18 | 17 | -0.54 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x7 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x6 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x3 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x2 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 GBP/USD: OANDA candles 504: temporary gateway error (HTML page)
- x1 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 EUR/USD: OANDA position 503: {"errorMessage":"Unable to service request; please try again later."}

## Latest closed trades
- Bitcoin: long -0.97%
- Bitcoin: long -0.25%
- Bitcoin: long -0.37%
- Bitcoin: long -0.47%
- Bitcoin: long -0.68%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- Gold USD: long -0.56%
- Gold USD: long -0.77%
- USD/JPY: short -0.03%
- USD/JPY: short -0.07%
- USD/JPY: short -0.11%
- USD/JPY: short -0.12%
- USD/JPY: long -0.11%
- USD/JPY totals: long 11 trades -0.29%, short 8 trades -0.09%
- GBP/USD: short -0.03%
- GBP/USD: short -0.08%
- GBP/USD: short -0.03%
- GBP/USD: long -0.01%
- GBP/USD: short -0.11%
- GBP/USD totals: long 10 trades +0.12%, short 6 trades -0.38%
- EUR/USD: short +0.18%
- EUR/USD: short -0.05%
- EUR/USD: long -0.09%
- EUR/USD: short +0.21%
- EUR/USD: long -0.10%
- EUR/USD totals: long 13 trades -0.49%, short 6 trades +0.48%
- EUR/GBP: short +0.03%
- EUR/GBP: long -0.04%
- EUR/GBP: long +0.02%
- EUR/GBP: short -0.03%
- EUR/GBP: short -0.00%
- EUR/GBP totals: long 13 trades -0.39%, short 5 trades -0.14%

## Latest log rows
- Bitcoin 11-17 23:03 price 64815.62 holding 1.5%
- Bitcoin 11-17 23:04 price 64801.06 holding 1.4%
- Bitcoin 11-17 23:05 price 64857.44 holding 1.5%
- Gold USD 11-17 23:03 price 3842.09 no_trade score below 2
- Gold USD 11-17 23:04 price 3840.71 no_trade score below 2
- Gold USD 11-17 23:05 price 3841.43 no_trade score below 2
- USD/JPY 11-17 23:03 price 159.437 holding 0.0%
- USD/JPY 11-17 23:04 price 159.437 holding 0.0%
- USD/JPY 11-17 23:05 price 159.437 holding 0.0%
- GBP/USD 11-17 23:03 price 1.32078 no_trade max 3 open positions reached
- GBP/USD 11-17 23:04 price 1.32078 no_trade max 3 open positions reached
- GBP/USD 11-17 23:05 price 1.32078 no_trade max 3 open positions reached
- EUR/USD 11-17 23:03 price 1.09991 no_trade re-entry cooldown
- EUR/USD 11-17 23:04 price 1.09991 no_trade re-entry cooldown
- EUR/USD 11-17 23:05 price 1.09991 no_trade re-entry cooldown
- EUR/GBP 11-17 23:03 price 0.83276 holding SHORT 0.1%
- EUR/GBP 11-17 23:04 price 0.83276 holding SHORT 0.1%
- EUR/GBP 11-17 23:05 price 0.83276 holding SHORT 0.1%
