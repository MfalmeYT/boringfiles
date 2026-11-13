# Bot report (generated 2026-11-13 20:44 UTC)

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
| Bitcoin | 11-13 20:44 | 1437 | 4 | 0 | 4 | 0 | -2.43 |  |
| Gold USD | 11-13 20:44 | 1328 | 2 | 0 | 2 | 0 | -1.17 |  |
| USD/JPY | 11-13 20:44 | 1376 | 2 | 14 | 12 | 33 | -0.05 |  |
| GBP/USD | 11-13 20:44 | 1376 | 4 | 6 | 11 | 45 | -0.00 | yes |
| EUR/USD | 11-13 20:44 | 1376 | 4 | 4 | 12 | 33 | -0.12 | yes |
| EUR/GBP | 11-13 20:44 | 1376 | 4 | 7 | 13 | 8 | -0.51 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x8 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x3 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x3 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x3 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x2 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.86%
- Bitcoin: long -0.12%
- Bitcoin: long -1.04%
- Bitcoin: long -0.41%
- Gold USD: long -0.44%
- Gold USD: long -0.73%
- USD/JPY: long -0.11%
- USD/JPY: long -0.07%
- USD/JPY: long -0.13%
- USD/JPY: short -0.03%
- USD/JPY: short +0.16%
- USD/JPY totals: long 10 trades -0.18%, short 2 trades +0.13%
- GBP/USD: long -0.03%
- GBP/USD: long -0.06%
- GBP/USD: short -0.07%
- GBP/USD: short -0.07%
- GBP/USD: long -0.06%
- GBP/USD totals: long 9 trades +0.13%, short 2 trades -0.13%
- EUR/USD: long -0.07%
- EUR/USD: long -0.10%
- EUR/USD: long -0.07%
- EUR/USD: long -0.11%
- EUR/USD: short +0.18%
- EUR/USD totals: long 11 trades -0.30%, short 1 trades +0.18%
- EUR/GBP: long -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.03%
- EUR/GBP: short -0.04%
- EUR/GBP: short -0.10%
- EUR/GBP totals: long 11 trades -0.38%, short 2 trades -0.14%

## Latest log rows
- Bitcoin 11-13 20:42 price 68851.9 no_trade score below 2
- Bitcoin 11-13 20:43 price 68840.2 no_trade score below 2
- Bitcoin 11-13 20:44 price 68844.24 no_trade score below 2
- Gold USD 11-13 20:42 price 3872.22 no_trade score below 2
- Gold USD 11-13 20:43 price 3872.55 no_trade score below 2
- Gold USD 11-13 20:44 price 3873.04 no_trade score below 2
- USD/JPY 11-13 20:42 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- USD/JPY 11-13 20:43 price  error OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- USD/JPY 11-13 20:44 price 159.774 no_trade re-entry cooldown
- GBP/USD 11-13 20:42 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- GBP/USD 11-13 20:43 price 1.32114 holding SHORT -0.0%
- GBP/USD 11-13 20:44 price  error OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/USD 11-13 20:42 price 1.10226 holding SHORT 0.0%
- EUR/USD 11-13 20:43 price 1.10226 holding SHORT 0.0%
- EUR/USD 11-13 20:44 price 1.10226 holding SHORT 0.0%
- EUR/GBP 11-13 20:42 price 0.83434 holding SHORT 0.0%
- EUR/GBP 11-13 20:43 price 0.83434 holding SHORT 0.0%
- EUR/GBP 11-13 20:44 price 0.83434 holding SHORT 0.0%
