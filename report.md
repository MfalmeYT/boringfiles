# Bot report (generated 2026-11-18 00:46 UTC)

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
| Bitcoin | 11-18 00:46 | 1440 | 3 | 0 | 24 | 4 | -15.79 | yes |
| Gold USD | 11-18 00:46 | 1440 | 2 | 0 | 9 | 11 | -4.61 |  |
| USD/JPY | 11-18 00:46 | 1379 | 4 | 1 | 19 | 26 | -0.38 | yes |
| GBP/USD | 11-18 00:46 | 1379 | 3 | 3 | 16 | 31 | -0.26 | yes |
| EUR/USD | 11-18 00:46 | 1379 | 3 | 1 | 19 | 37 | -0.01 |  |
| EUR/GBP | 11-18 00:46 | 1379 | 2 | 1 | 19 | 21 | -0.44 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x2 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 GBP/USD: OANDA candles 504: temporary gateway error (HTML page)
- x1 EUR/USD: OANDA position 503: {"errorMessage":"Unable to service request; please try again later."}
- x1 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}

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
- EUR/GBP: long -0.04%
- EUR/GBP: long +0.02%
- EUR/GBP: short -0.03%
- EUR/GBP: short -0.00%
- EUR/GBP: short +0.10%
- EUR/GBP totals: long 13 trades -0.39%, short 6 trades -0.04%

## Latest log rows
- Bitcoin 11-18 00:44 price 64651.24 holding 1.2%
- Bitcoin 11-18 00:45 price 64647.99 holding 1.2%
- Bitcoin 11-18 00:46 price 64650.36 holding 1.2%
- Gold USD 11-18 00:44 price 3816.43 no_trade score below 2
- Gold USD 11-18 00:45 price 3813.39 no_trade score below 2
- Gold USD 11-18 00:46 price 3812.68 no_trade score below 2
- USD/JPY 11-18 00:44 price 159.486 holding 0.1%
- USD/JPY 11-18 00:45 price 159.49 holding 0.1%
- USD/JPY 11-18 00:46 price 159.49 holding 0.1%
- GBP/USD 11-18 00:44 price 1.3204 holding SHORT -0.0%
- GBP/USD 11-18 00:45 price 1.32018 holding SHORT -0.0%
- GBP/USD 11-18 00:46 price 1.32018 holding SHORT -0.0%
- EUR/USD 11-18 00:44 price 1.09891 no_trade max 3 open positions reached
- EUR/USD 11-18 00:45 price 1.09854 no_trade max 3 open positions reached
- EUR/USD 11-18 00:46 price 1.09854 no_trade max 3 open positions reached
- EUR/GBP 11-18 00:44 price 0.83224 no_trade re-entry cooldown
- EUR/GBP 11-18 00:45 price 0.8321 no_trade re-entry cooldown
- EUR/GBP 11-18 00:46 price 0.8321 no_trade re-entry cooldown
