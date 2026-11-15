# Bot report (generated 2026-11-15 23:14 UTC)

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
| Bitcoin | 11-15 23:14 | 1440 | 6 | 0 | 16 | 6 | -10.83 | yes |
| Gold USD | 11-15 23:14 | 1440 | 2 | 0 | 5 | 0 | -2.78 | yes |
| USD/JPY | 11-15 23:14 | 100 | 1 | 85 | 12 | 33 | -0.05 | yes |
| GBP/USD | 11-15 23:14 | 97 | 0 | 82 | 12 | 42 | -0.03 |  |
| EUR/USD | 11-15 23:14 | 97 | 0 | 82 | 13 | 38 | -0.08 |  |
| EUR/GBP | 11-15 23:14 | 77 | 0 | 62 | 14 | 14 | -0.48 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x85 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x82 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x82 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x62 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -1.10%
- Bitcoin: long -0.09%
- Bitcoin: long +0.10%
- Bitcoin: long -0.80%
- Bitcoin: long -0.98%
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
- Bitcoin 11-15 23:12 price 65124.91 holding 0.5%
- Bitcoin 11-15 23:13 price 65052.29 holding 0.4%
- Bitcoin 11-15 23:14 price 65072.9 holding 0.5%
- Gold USD 11-15 23:12 price 3872.76 holding 0.6%
- Gold USD 11-15 23:13 price 3871.33 holding 0.5%
- Gold USD 11-15 23:14 price 3871.08 holding 0.5%
- USD/JPY 11-15 23:12 price 159.719 holding SHORT -0.0%
- USD/JPY 11-15 23:13 price 159.719 holding SHORT -0.0%
- USD/JPY 11-15 23:14 price 159.719 holding SHORT -0.0%
- GBP/USD 11-15 23:12 price 1.3217 no_trade max 3 open positions reached
- GBP/USD 11-15 23:13 price 1.3217 no_trade max 3 open positions reached
- GBP/USD 11-15 23:14 price 1.3217 no_trade max 3 open positions reached
- EUR/USD 11-15 23:12 price 1.1026 no_trade max 3 open positions reached
- EUR/USD 11-15 23:13 price 1.1026 no_trade max 3 open positions reached
- EUR/USD 11-15 23:14 price 1.1026 no_trade max 3 open positions reached
- EUR/GBP 11-15 23:12 price 0.83414 no_trade max 3 open positions reached
- EUR/GBP 11-15 23:13 price 0.83414 no_trade max 3 open positions reached
- EUR/GBP 11-15 23:14 price 0.83414 no_trade max 3 open positions reached
