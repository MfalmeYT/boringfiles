# Bot report (generated 2026-11-16 04:25 UTC)

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
| Bitcoin | 11-16 04:25 | 1435 | 4 | 0 | 17 | 6 | -11.21 |  |
| Gold USD | 11-16 04:25 | 1435 | 1 | 0 | 5 | 0 | -2.78 | yes |
| USD/JPY | 11-16 04:25 | 397 | 1 | 106 | 12 | 33 | -0.05 | yes |
| GBP/USD | 11-16 04:25 | 390 | 1 | 93 | 12 | 42 | -0.03 | yes |
| EUR/USD | 11-16 04:25 | 384 | 1 | 79 | 13 | 38 | -0.08 | yes |
| EUR/GBP | 11-16 04:25 | 367 | 0 | 62 | 14 | 14 | -0.48 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x99 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x82 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x74 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x52 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x7 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 EUR/GBP: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x3 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.09%
- Bitcoin: long +0.10%
- Bitcoin: long -0.80%
- Bitcoin: long -0.98%
- Bitcoin: long -0.38%
- Gold USD: long -0.44%
- Gold USD: long -0.73%
- Gold USD: long -0.56%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
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
- Bitcoin 11-16 04:23 price 64974.15 no_trade score below 2
- Bitcoin 11-16 04:24 price 65010.66 no_trade short-term trend not up
- Bitcoin 11-16 04:25 price 65055.54 no_trade short-term trend not up
- Gold USD 11-16 04:23 price 3856.04 holding 0.1%
- Gold USD 11-16 04:24 price 3856.04 holding 0.1%
- Gold USD 11-16 04:25 price 3856.04 holding 0.1%
- USD/JPY 11-16 04:23 price 159.628 holding SHORT 0.1%
- USD/JPY 11-16 04:24 price 159.628 holding SHORT 0.1%
- USD/JPY 11-16 04:25 price 159.628 holding SHORT 0.1%
- GBP/USD 11-16 04:23 price 1.32052 holding SHORT 0.0%
- GBP/USD 11-16 04:24 price 1.32052 holding SHORT 0.0%
- GBP/USD 11-16 04:25 price 1.32052 holding SHORT 0.0%
- EUR/USD 11-16 04:23 price 1.1016 holding SHORT 0.1%
- EUR/USD 11-16 04:24 price 1.1016 holding SHORT 0.1%
- EUR/USD 11-16 04:25 price 1.1016 holding SHORT 0.1%
- EUR/GBP 11-16 04:23 price 0.83425 no_trade max 3 open positions reached
- EUR/GBP 11-16 04:24 price 0.83425 no_trade max 3 open positions reached
- EUR/GBP 11-16 04:25 price 0.83425 no_trade max 3 open positions reached
