# Bot report (generated 2026-11-13 18:06 UTC)

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
| Bitcoin | 11-13 18:06 | 1437 | 4 | 0 | 3 | 0 | -2.02 | yes |
| Gold USD | 11-13 18:06 | 1170 | 2 | 0 | 1 | 0 | -0.44 | yes |
| USD/JPY | 11-13 18:06 | 1376 | 3 | 1 | 11 | 27 | -0.21 | yes |
| GBP/USD | 11-13 18:06 | 1376 | 3 | 0 | 11 | 45 | -0.00 |  |
| EUR/USD | 11-13 18:06 | 1376 | 3 | 0 | 12 | 33 | -0.12 |  |
| EUR/GBP | 11-13 18:06 | 1376 | 3 | 0 | 13 | 8 | -0.51 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x1 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.86%
- Bitcoin: long -0.12%
- Bitcoin: long -1.04%
- Gold USD: long -0.44%
- USD/JPY: long -0.10%
- USD/JPY: long -0.11%
- USD/JPY: long -0.07%
- USD/JPY: long -0.13%
- USD/JPY: short -0.03%
- USD/JPY totals: long 10 trades -0.18%, short 1 trades -0.03%
- GBP/USD: long -0.03%
- GBP/USD: long -0.06%
- GBP/USD: short -0.07%
- GBP/USD: short -0.07%
- GBP/USD: long -0.06%
- GBP/USD totals: long 9 trades +0.13%, short 2 trades -0.13%
- EUR/USD: long -0.07%
- EUR/USD: long -0.10%
- EUR/USD: long -0.07%
- EUR/USD: long -0.11%
- EUR/USD: short +0.18%
- EUR/USD totals: long 11 trades -0.30%, short 1 trades +0.18%
- EUR/GBP: long -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.03%
- EUR/GBP: short -0.04%
- EUR/GBP: short -0.10%
- EUR/GBP totals: long 11 trades -0.38%, short 2 trades -0.14%

## Latest log rows
- Bitcoin 11-13 18:04 price 68839.25 holding 0.1%
- Bitcoin 11-13 18:05 price 68809.82 holding 0.0%
- Bitcoin 11-13 18:06 price 68798.98 holding -0.0%
- Gold USD 11-13 18:04 price 3874.49 holding -0.6%
- Gold USD 11-13 18:05 price 3876.49 holding -0.5%
- Gold USD 11-13 18:06 price 3876.46 holding -0.5%
- USD/JPY 11-13 18:04 price  error OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- USD/JPY 11-13 18:05 price 159.929 holding SHORT -0.1%
- USD/JPY 11-13 18:06 price 159.929 holding SHORT -0.1%
- GBP/USD 11-13 18:04 price 1.32078 no_trade re-entry cooldown
- GBP/USD 11-13 18:05 price 1.32078 no_trade re-entry cooldown
- GBP/USD 11-13 18:06 price 1.32078 no_trade re-entry cooldown
- EUR/USD 11-13 18:04 price 1.10279 no_trade re-entry cooldown
- EUR/USD 11-13 18:05 price 1.10279 no_trade re-entry cooldown
- EUR/USD 11-13 18:06 price 1.10279 no_trade re-entry cooldown
- EUR/GBP 11-13 18:04 price 0.83496 no_trade re-entry cooldown
- EUR/GBP 11-13 18:05 price 0.83496 no_trade re-entry cooldown
- EUR/GBP 11-13 18:06 price 0.83496 no_trade re-entry cooldown
