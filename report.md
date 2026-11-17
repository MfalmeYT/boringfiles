# Bot report (generated 2026-11-17 16:56 UTC)

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
| Bitcoin | 11-17 16:56 | 1443 | 3 | 0 | 24 | 4 | -15.79 |  |
| Gold USD | 11-17 16:56 | 1443 | 2 | 0 | 8 | 12 | -3.84 | yes |
| USD/JPY | 11-17 16:56 | 1388 | 4 | 40 | 19 | 26 | -0.38 |  |
| GBP/USD | 11-17 16:56 | 1386 | 2 | 33 | 16 | 31 | -0.26 |  |
| EUR/USD | 11-17 16:56 | 1386 | 4 | 32 | 18 | 39 | +0.09 | yes |
| EUR/GBP | 11-17 16:56 | 1385 | 4 | 26 | 18 | 17 | -0.54 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x26 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x24 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x24 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x18 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x7 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x7 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x5 EUR/GBP: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x4 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}

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
- Bitcoin 11-17 16:54 price 63572.06 no_trade score below 2
- Bitcoin 11-17 16:55 price 63482.17 no_trade score below 2
- Bitcoin 11-17 16:56 price 63467.48 no_trade score below 2
- Gold USD 11-17 16:54 price 3850.85 holding -0.7%
- Gold USD 11-17 16:55 price 3853.05 holding -0.6%
- Gold USD 11-17 16:56 price 3852.16 holding -0.6%
- USD/JPY 11-17 16:54 price 159.254 no_trade re-entry cooldown
- USD/JPY 11-17 16:55 price 159.254 no_trade re-entry cooldown
- USD/JPY 11-17 16:56 price 159.254 no_trade re-entry cooldown
- GBP/USD 11-17 16:54 price 1.3219 no_trade re-entry cooldown
- GBP/USD 11-17 16:55 price 1.3219 no_trade re-entry cooldown
- GBP/USD 11-17 16:56 price 1.3219 no_trade re-entry cooldown
- EUR/USD 11-17 16:54 price 1.10149 holding 0.0%
- EUR/USD 11-17 16:55 price 1.10149 holding 0.0%
- EUR/USD 11-17 16:56 price 1.10149 holding 0.0%
- EUR/GBP 11-17 16:54 price 0.83328 holding SHORT -0.0%
- EUR/GBP 11-17 16:55 price 0.83328 holding SHORT -0.0%
- EUR/GBP 11-17 16:56 price 0.83328 holding SHORT -0.0%
