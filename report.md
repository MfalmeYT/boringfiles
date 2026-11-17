# Bot report (generated 2026-11-17 18:38 UTC)

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
| Bitcoin | 11-17 18:38 | 1444 | 3 | 0 | 24 | 4 | -15.79 |  |
| Gold USD | 11-17 18:38 | 1444 | 2 | 0 | 8 | 12 | -3.84 | yes |
| USD/JPY | 11-17 18:38 | 1389 | 4 | 32 | 19 | 26 | -0.38 |  |
| GBP/USD | 11-17 18:38 | 1387 | 2 | 26 | 16 | 31 | -0.26 |  |
| EUR/USD | 11-17 18:38 | 1387 | 4 | 22 | 18 | 39 | +0.09 | yes |
| EUR/GBP | 11-17 18:38 | 1386 | 3 | 19 | 18 | 17 | -0.54 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x21 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x20 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x18 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x14 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x6 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 EUR/GBP: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x3 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x3 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x2 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.97%
- Bitcoin: long -0.25%
- Bitcoin: long -0.37%
- Bitcoin: long -0.47%
- Bitcoin: long -0.68%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- Gold USD: long -0.56%
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
- EUR/USD: short -0.09%
- EUR/USD: short +0.18%
- EUR/USD: short -0.05%
- EUR/USD: long -0.09%
- EUR/USD: short +0.21%
- EUR/USD totals: long 12 trades -0.39%, short 6 trades +0.48%
- EUR/GBP: short +0.03%
- EUR/GBP: long -0.04%
- EUR/GBP: long +0.02%
- EUR/GBP: short -0.03%
- EUR/GBP: short -0.00%
- EUR/GBP totals: long 13 trades -0.39%, short 5 trades -0.14%

## Latest log rows
- Bitcoin 11-17 18:36 price 63744.46 no_trade score below 2
- Bitcoin 11-17 18:37 price 63783.7 no_trade score below 2
- Bitcoin 11-17 18:38 price 63788.5 no_trade score below 2
- Gold USD 11-17 18:36 price 3849.53 holding -0.7%
- Gold USD 11-17 18:37 price 3849.53 holding -0.7%
- Gold USD 11-17 18:38 price 3850.07 holding -0.7%
- USD/JPY 11-17 18:36 price 159.304 no_trade re-entry cooldown
- USD/JPY 11-17 18:37 price 159.304 no_trade re-entry cooldown
- USD/JPY 11-17 18:38 price 159.304 no_trade re-entry cooldown
- GBP/USD 11-17 18:36 price 1.32234 no_trade max 3 open positions reached
- GBP/USD 11-17 18:37 price 1.32234 no_trade max 3 open positions reached
- GBP/USD 11-17 18:38 price 1.32234 no_trade max 3 open positions reached
- EUR/USD 11-17 18:36 price 1.1015 holding 0.0%
- EUR/USD 11-17 18:37 price 1.1015 holding 0.0%
- EUR/USD 11-17 18:38 price 1.1015 holding 0.0%
- EUR/GBP 11-17 18:36 price 0.833 holding SHORT 0.0%
- EUR/GBP 11-17 18:37 price 0.833 holding SHORT 0.0%
- EUR/GBP 11-17 18:38 price 0.833 holding SHORT 0.0%
