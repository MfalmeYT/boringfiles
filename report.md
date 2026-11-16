# Bot report (generated 2026-11-16 06:36 UTC)

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
| Bitcoin | 11-16 06:36 | 1435 | 4 | 0 | 17 | 6 | -11.21 |  |
| Gold USD | 11-16 06:36 | 1435 | 1 | 0 | 6 | 17 | -2.73 |  |
| USD/JPY | 11-16 06:36 | 520 | 1 | 105 | 13 | 38 | +0.13 |  |
| GBP/USD | 11-16 06:36 | 513 | 1 | 89 | 12 | 42 | -0.03 | yes |
| EUR/USD | 11-16 06:36 | 506 | 1 | 76 | 13 | 38 | -0.08 | yes |
| EUR/GBP | 11-16 06:36 | 494 | 1 | 63 | 14 | 14 | -0.48 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x96 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x77 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x69 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x51 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x7 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x6 EUR/GBP: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x6 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.09%
- Bitcoin: long +0.10%
- Bitcoin: long -0.80%
- Bitcoin: long -0.98%
- Bitcoin: long -0.38%
- Gold USD: long -0.73%
- Gold USD: long -0.56%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- USD/JPY: long -0.07%
- USD/JPY: long -0.13%
- USD/JPY: short -0.03%
- USD/JPY: short +0.16%
- USD/JPY: short +0.18%
- USD/JPY totals: long 10 trades -0.18%, short 3 trades +0.31%
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
- Bitcoin 11-16 06:34 price 64541.55 no_trade score below 2
- Bitcoin 11-16 06:35 price 64560.57 no_trade score below 2
- Bitcoin 11-16 06:36 price 64562.22 no_trade score below 2
- Gold USD 11-16 06:34 price 3834.82 no_trade score below 2
- Gold USD 11-16 06:35 price 3834.82 no_trade score below 2
- Gold USD 11-16 06:36 price 3834.82 no_trade score below 2
- USD/JPY 11-16 06:34 price 159.486 no_trade re-entry cooldown
- USD/JPY 11-16 06:35 price 159.486 no_trade re-entry cooldown
- USD/JPY 11-16 06:36 price  error OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- GBP/USD 11-16 06:34 price 1.32068 holding SHORT 0.0%
- GBP/USD 11-16 06:35 price 1.32068 holding SHORT 0.0%
- GBP/USD 11-16 06:36 price 1.32068 holding SHORT 0.0%
- EUR/USD 11-16 06:34 price 1.10166 holding SHORT 0.1%
- EUR/USD 11-16 06:35 price 1.10166 holding SHORT 0.1%
- EUR/USD 11-16 06:36 price 1.10166 holding SHORT 0.1%
- EUR/GBP 11-16 06:34 price 0.83419 holding -0.0%
- EUR/GBP 11-16 06:35 price 0.83419 holding -0.0%
- EUR/GBP 11-16 06:36 price 0.83419 holding -0.0%
