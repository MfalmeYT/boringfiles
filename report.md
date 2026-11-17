# Bot report (generated 2026-11-17 09:12 UTC)

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
| Bitcoin | 11-17 09:12 | 1440 | 5 | 0 | 23 | 4 | -15.11 |  |
| Gold USD | 11-17 09:12 | 1440 | 2 | 0 | 7 | 14 | -3.29 | yes |
| USD/JPY | 11-17 09:12 | 1385 | 3 | 87 | 17 | 29 | -0.15 |  |
| GBP/USD | 11-17 09:12 | 1383 | 2 | 57 | 14 | 36 | -0.14 | yes |
| EUR/USD | 11-17 09:12 | 1383 | 3 | 60 | 17 | 35 | -0.12 |  |
| EUR/GBP | 11-17 09:12 | 1382 | 5 | 49 | 18 | 17 | -0.54 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x55 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x40 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x36 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x34 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x17 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x15 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x14 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x11 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x9 EUR/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x8 EUR/GBP: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.82%
- Bitcoin: long -0.97%
- Bitcoin: long -0.25%
- Bitcoin: long -0.37%
- Bitcoin: long -0.47%
- Gold USD: long -0.56%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- USD/JPY: short +0.18%
- USD/JPY: short -0.07%
- USD/JPY: short -0.03%
- USD/JPY: short -0.07%
- USD/JPY: short -0.11%
- USD/JPY totals: long 10 trades -0.18%, short 7 trades +0.03%
- GBP/USD: short -0.07%
- GBP/USD: long -0.06%
- GBP/USD: short -0.03%
- GBP/USD: short -0.08%
- GBP/USD: short -0.03%
- GBP/USD totals: long 9 trades +0.13%, short 5 trades -0.27%
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
- Bitcoin 11-17 09:10 price 64224.01 no_trade score below 2
- Bitcoin 11-17 09:11 price 64181.54 no_trade score below 2
- Bitcoin 11-17 09:12 price 64181.12 no_trade score below 2
- Gold USD 11-17 09:10 price 3856.95 holding -0.5%
- Gold USD 11-17 09:11 price 3856.95 holding -0.5%
- Gold USD 11-17 09:12 price 3856.95 holding -0.5%
- USD/JPY 11-17 09:10 price 159.102 no_trade re-entry cooldown
- USD/JPY 11-17 09:11 price 159.102 no_trade re-entry cooldown
- USD/JPY 11-17 09:12 price 159.102 no_trade re-entry cooldown
- GBP/USD 11-17 09:10 price 1.31908 holding 0.0%
- GBP/USD 11-17 09:11 price 1.31908 holding 0.0%
- GBP/USD 11-17 09:12 price 1.31908 holding 0.0%
- EUR/USD 11-17 09:10 price 1.10013 no_trade re-entry cooldown
- EUR/USD 11-17 09:11 price 1.10013 no_trade re-entry cooldown
- EUR/USD 11-17 09:12 price 1.10013 no_trade re-entry cooldown
- EUR/GBP 11-17 09:10 price 0.83402 no_trade re-entry cooldown
- EUR/GBP 11-17 09:11 price 0.83402 no_trade re-entry cooldown
- EUR/GBP 11-17 09:12 price 0.83402 no_trade re-entry cooldown
