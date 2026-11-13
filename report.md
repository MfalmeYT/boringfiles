# Bot report (generated 2026-11-13 03:40 UTC)

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
| Bitcoin | 11-13 03:40 | 1440 | 0 | 0 | 0 | - | +0.00 |  |
| Gold USD | 11-13 03:40 | 307 | 1 | 0 | 0 | - | +0.00 | yes |
| USD/JPY | 11-13 03:40 | 1379 | 3 | 145 | 9 | 33 | -0.05 | yes |
| GBP/USD | 11-13 03:40 | 1379 | 1 | 47 | 8 | 62 | +0.19 |  |
| EUR/USD | 11-13 03:40 | 1379 | 2 | 0 | 9 | 33 | -0.12 | yes |
| EUR/GBP | 11-13 03:40 | 1379 | 2 | 157 | 10 | 10 | -0.34 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x156 EUR/GBP: Order buy cancelled: INSUFFICIENT_MARGIN
- x145 USD/JPY: Order buy cancelled: INSUFFICIENT_MARGIN
- x47 GBP/USD: Order buy cancelled: INSUFFICIENT_MARGIN
- x1 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- USD/JPY: long +0.12%
- USD/JPY: long -0.13%
- USD/JPY: long -0.10%
- USD/JPY: long -0.11%
- USD/JPY: long -0.07%
- GBP/USD: long +0.11%
- GBP/USD: long -0.04%
- GBP/USD: long +0.06%
- GBP/USD: long -0.03%
- GBP/USD: long -0.06%
- EUR/USD: long +0.08%
- EUR/USD: long -0.07%
- EUR/USD: long -0.06%
- EUR/USD: long -0.07%
- EUR/USD: long -0.10%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP: long -0.07%
- EUR/GBP: long -0.04%
- EUR/GBP: long -0.05%

## Latest log rows
- Bitcoin 11-13 03:38 price 69139.65 no_trade score below 2
- Bitcoin 11-13 03:39 price 69159.46 no_trade score below 2
- Bitcoin 11-13 03:40 price 69114.53 no_trade score below 2
- Gold USD 11-13 03:38 price 3910.88 holding 0.1%
- Gold USD 11-13 03:39 price 3913.31 holding 0.1%
- Gold USD 11-13 03:40 price 3913.39 holding 0.1%
- USD/JPY 11-13 03:38 price 159.947 holding 0.0%
- USD/JPY 11-13 03:39 price 159.947 holding 0.0%
- USD/JPY 11-13 03:40 price 159.947 holding 0.0%
- GBP/USD 11-13 03:38 price 1.32343 no_trade max 3 open positions reached
- GBP/USD 11-13 03:39 price 1.32343 no_trade max 3 open positions reached
- GBP/USD 11-13 03:40 price 1.32343 no_trade max 3 open positions reached
- EUR/USD 11-13 03:38 price 1.10609 holding -0.0%
- EUR/USD 11-13 03:39 price 1.10609 holding -0.0%
- EUR/USD 11-13 03:40 price 1.10609 holding -0.0%
- EUR/GBP 11-13 03:38 price 0.8358 no_trade max 3 open positions reached
- EUR/GBP 11-13 03:39 price 0.8358 no_trade max 3 open positions reached
- EUR/GBP 11-13 03:40 price 0.8358 no_trade max 3 open positions reached
