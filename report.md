# Bot report (generated 2026-11-17 00:07 UTC)

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
| Bitcoin | 11-17 00:07 | 1431 | 5 | 1 | 22 | 5 | -14.64 |  |
| Gold USD | 11-17 00:07 | 1431 | 1 | 2 | 7 | 14 | -3.29 |  |
| USD/JPY | 11-17 00:07 | 1376 | 3 | 127 | 15 | 33 | +0.04 | yes |
| GBP/USD | 11-17 00:07 | 1374 | 1 | 83 | 13 | 38 | -0.11 | yes |
| EUR/USD | 11-17 00:07 | 1374 | 2 | 81 | 16 | 38 | -0.03 |  |
| EUR/GBP | 11-17 00:07 | 1373 | 5 | 69 | 16 | 19 | -0.50 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x84 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x53 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x48 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x44 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x24 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x21 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x18 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x15 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x14 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x13 EUR/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

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
- EUR/USD: short +0.18%
- EUR/USD: short +0.05%
- EUR/USD: short -0.09%
- EUR/USD: short +0.18%
- EUR/USD: short -0.05%
- EUR/USD totals: long 11 trades -0.30%, short 5 trades +0.27%
- EUR/GBP: short -0.04%
- EUR/GBP: short -0.10%
- EUR/GBP: short +0.03%
- EUR/GBP: long -0.04%
- EUR/GBP: long +0.02%
- EUR/GBP totals: long 13 trades -0.39%, short 3 trades -0.11%

## Latest log rows
- Bitcoin 11-17 00:05 price 64676.4 no_trade score below 2
- Bitcoin 11-17 00:06 price 64680.74 no_trade score below 2
- Bitcoin 11-17 00:07 price 64682.06 no_trade score below 2
- Gold USD 11-17 00:05 price 3847.25 no_trade score below 2
- Gold USD 11-17 00:06 price 3848.32 no_trade short-term trend not up
- Gold USD 11-17 00:07 price 3847.64 no_trade short-term trend not up
- USD/JPY 11-17 00:05 price 159.525 holding SHORT -0.0%
- USD/JPY 11-17 00:06 price 159.525 holding SHORT -0.0%
- USD/JPY 11-17 00:07 price 159.525 holding SHORT -0.0%
- GBP/USD 11-17 00:05 price 1.31844 holding SHORT 0.1%
- GBP/USD 11-17 00:06 price 1.31844 holding SHORT 0.1%
- GBP/USD 11-17 00:07 price 1.31844 holding SHORT 0.1%
- EUR/USD 11-17 00:05 price 1.0998 holding SHORT -0.0%
- EUR/USD 11-17 00:06 price 1.1004 cover closed by broker stop/TP; P/L -0.9750
- EUR/USD 11-17 00:07 price 1.0998 no_trade re-entry cooldown
- EUR/GBP 11-17 00:05 price 0.8342 holding SHORT 0.0%
- EUR/GBP 11-17 00:06 price 0.8342 holding SHORT 0.0%
- EUR/GBP 11-17 00:07 price 0.8342 holding SHORT 0.0%
