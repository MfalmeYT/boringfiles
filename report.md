# Bot report (generated 2026-11-14 20:49 UTC)

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
| Bitcoin | 11-14 20:49 | 1440 | 7 | 0 | 11 | 0 | -7.97 |  |
| Gold USD | 11-14 20:49 | 1440 | 2 | 0 | 4 | 0 | -2.31 |  |
| USD/JPY | 11-14 20:13 | 158 | 0 | 94 | 12 | 33 | -0.05 |  |
| GBP/USD | 11-14 20:33 | 153 | 0 | 88 | 12 | 42 | -0.03 |  |
| EUR/USD | 11-14 20:44 | 125 | 0 | 60 | 13 | 38 | -0.08 |  |
| EUR/GBP | 11-14 20:44 | 122 | 0 | 57 | 14 | 14 | -0.48 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x92 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x88 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x58 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x55 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x2 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x2 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 EUR/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.86%
- Bitcoin: long -0.91%
- Bitcoin: long -0.62%
- Bitcoin: long -0.80%
- Bitcoin: long -0.88%
- Gold USD: long -0.44%
- Gold USD: long -0.73%
- Gold USD: long -0.56%
- Gold USD: long -0.58%
- USD/JPY: long -0.11%
- USD/JPY: long -0.07%
- USD/JPY: long -0.13%
- USD/JPY: short -0.03%
- USD/JPY: short +0.16%
- USD/JPY totals: long 10 trades -0.18%, short 2 trades +0.13%
- GBP/USD: long -0.06%
- GBP/USD: short -0.07%
- GBP/USD: short -0.07%
- GBP/USD: long -0.06%
- GBP/USD: short -0.03%
- GBP/USD totals: long 9 trades +0.13%, short 3 trades -0.16%
- EUR/USD: long -0.10%
- EUR/USD: long -0.07%
- EUR/USD: long -0.11%
- EUR/USD: short +0.18%
- EUR/USD: short +0.05%
- EUR/USD totals: long 11 trades -0.30%, short 2 trades +0.22%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.03%
- EUR/GBP: short -0.04%
- EUR/GBP: short -0.10%
- EUR/GBP: short +0.03%
- EUR/GBP totals: long 11 trades -0.38%, short 3 trades -0.11%

## Latest log rows
- Bitcoin 11-14 20:47 price 65451.05 no_trade score below 2
- Bitcoin 11-14 20:48 price 65448.32 no_trade score below 2
- Bitcoin 11-14 20:49 price 65407.6 no_trade score below 2
- Gold USD 11-14 20:47 price 3822.5 no_trade score below 2
- Gold USD 11-14 20:48 price 3821.65 no_trade score below 2
- Gold USD 11-14 20:49 price 3822.1 no_trade score below 2
- USD/JPY 11-14 20:06 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- USD/JPY 11-14 20:07 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- USD/JPY 11-14 20:13 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- GBP/USD 11-14 20:07 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- GBP/USD 11-14 20:12 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- GBP/USD 11-14 20:33 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/USD 11-14 19:49 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/USD 11-14 19:53 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/USD 11-14 20:44 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/GBP 11-14 20:10 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/GBP 11-14 20:12 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/GBP 11-14 20:44 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
