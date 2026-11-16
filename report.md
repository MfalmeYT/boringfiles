# Bot report (generated 2026-11-16 21:10 UTC)

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
| Bitcoin | 11-16 21:10 | 1430 | 5 | 1 | 21 | 5 | -14.27 | yes |
| Gold USD | 11-16 21:10 | 1430 | 1 | 2 | 7 | 14 | -3.29 |  |
| USD/JPY | 11-16 21:10 | 1329 | 4 | 124 | 15 | 33 | +0.04 | yes |
| GBP/USD | 11-16 21:10 | 1327 | 2 | 85 | 13 | 38 | -0.11 | yes |
| EUR/USD | 11-16 21:10 | 1327 | 2 | 81 | 15 | 40 | +0.02 |  |
| EUR/GBP | 11-16 21:10 | 1324 | 5 | 67 | 16 | 19 | -0.50 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x85 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x53 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x51 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x40 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x21 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x21 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x17 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x15 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x14 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x13 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.38%
- Bitcoin: long -1.02%
- Bitcoin: long -0.82%
- Bitcoin: long -0.97%
- Bitcoin: long -0.25%
- Gold USD: long -0.56%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- USD/JPY: short -0.03%
- USD/JPY: short +0.16%
- USD/JPY: short +0.18%
- USD/JPY: short -0.07%
- USD/JPY: short -0.03%
- USD/JPY totals: long 10 trades -0.18%, short 5 trades +0.21%
- GBP/USD: short -0.07%
- GBP/USD: short -0.07%
- GBP/USD: long -0.06%
- GBP/USD: short -0.03%
- GBP/USD: short -0.08%
- GBP/USD totals: long 9 trades +0.13%, short 4 trades -0.24%
- EUR/USD: long -0.11%
- EUR/USD: short +0.18%
- EUR/USD: short +0.05%
- EUR/USD: short -0.09%
- EUR/USD: short +0.18%
- EUR/USD totals: long 11 trades -0.30%, short 4 trades +0.32%
- EUR/GBP: short -0.04%
- EUR/GBP: short -0.10%
- EUR/GBP: short +0.03%
- EUR/GBP: long -0.04%
- EUR/GBP: long +0.02%
- EUR/GBP totals: long 13 trades -0.39%, short 3 trades -0.11%

## Latest log rows
- Bitcoin 11-16 21:08 price 64937.4 holding -0.2%
- Bitcoin 11-16 21:09 price 64958.11 holding -0.1%
- Bitcoin 11-16 21:10 price 64946.8 holding -0.1%
- Gold USD 11-16 21:08 price 3841.01 no_trade score below 2
- Gold USD 11-16 21:09 price 3840.76 no_trade score below 2
- Gold USD 11-16 21:10 price 3840.76 no_trade score below 2
- USD/JPY 11-16 21:08 price 159.482 holding SHORT -0.0%
- USD/JPY 11-16 21:09 price 159.482 holding SHORT -0.0%
- USD/JPY 11-16 21:10 price 159.482 holding SHORT -0.0%
- GBP/USD 11-16 21:08 price 1.318 holding SHORT 0.1%
- GBP/USD 11-16 21:09 price 1.318 holding SHORT 0.1%
- GBP/USD 11-16 21:10 price 1.318 holding SHORT 0.1%
- EUR/USD 11-16 21:08 price 1.09959 no_trade re-entry cooldown
- EUR/USD 11-16 21:09 price 1.09959 no_trade re-entry cooldown
- EUR/USD 11-16 21:10 price 1.09959 no_trade re-entry cooldown
- EUR/GBP 11-16 21:08 price 0.8343 holding SHORT 0.0%
- EUR/GBP 11-16 21:09 price 0.8343 holding SHORT 0.0%
- EUR/GBP 11-16 21:10 price 0.8343 holding SHORT 0.0%
