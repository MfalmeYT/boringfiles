# Bot report (generated 2026-11-13 14:13 UTC)

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
| Bitcoin | 11-13 14:13 | 1439 | 3 | 0 | 2 | 0 | -0.98 | yes |
| Gold USD | 11-13 14:13 | 939 | 1 | 0 | 1 | 0 | -0.44 |  |
| USD/JPY | 11-13 14:13 | 1378 | 3 | 116 | 11 | 27 | -0.21 |  |
| GBP/USD | 11-13 14:13 | 1378 | 2 | 0 | 10 | 50 | +0.06 |  |
| EUR/USD | 11-13 14:13 | 1378 | 3 | 0 | 11 | 27 | -0.30 | yes |
| EUR/GBP | 11-13 14:13 | 1378 | 2 | 0 | 12 | 8 | -0.41 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x116 USD/JPY: Order buy cancelled: INSUFFICIENT_MARGIN

## Latest closed trades
- Bitcoin: long -0.86%
- Bitcoin: long -0.12%
- Gold USD: long -0.44%
- USD/JPY: long -0.10%
- USD/JPY: long -0.11%
- USD/JPY: long -0.07%
- USD/JPY: long -0.13%
- USD/JPY: short -0.03%
- USD/JPY totals: long 10 trades -0.18%, short 1 trades -0.03%
- GBP/USD: long +0.06%
- GBP/USD: long -0.03%
- GBP/USD: long -0.06%
- GBP/USD: short -0.07%
- GBP/USD: short -0.07%
- GBP/USD totals: long 8 trades +0.19%, short 2 trades -0.13%
- EUR/USD: long -0.06%
- EUR/USD: long -0.07%
- EUR/USD: long -0.10%
- EUR/USD: long -0.07%
- EUR/USD: long -0.11%
- EUR/GBP: long -0.07%
- EUR/GBP: long -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.03%
- EUR/GBP: short -0.04%
- EUR/GBP totals: long 11 trades -0.38%, short 1 trades -0.04%

## Latest log rows
- Bitcoin 11-13 14:11 price 69349.05 holding -0.3%
- Bitcoin 11-13 14:12 price 69221.1 holding -0.5%
- Bitcoin 11-13 14:13 price 69236.96 holding -0.4%
- Gold USD 11-13 14:11 price 3871.59 no_trade score below 2
- Gold USD 11-13 14:12 price 3871.59 no_trade score below 2
- Gold USD 11-13 14:13 price 3873.14 no_trade score below 2
- USD/JPY 11-13 14:11 price 159.916 no_trade re-entry cooldown
- USD/JPY 11-13 14:12 price 159.916 no_trade re-entry cooldown
- USD/JPY 11-13 14:13 price 159.916 no_trade re-entry cooldown
- GBP/USD 11-13 14:11 price 1.32322 no_trade re-entry cooldown
- GBP/USD 11-13 14:12 price 1.32322 no_trade re-entry cooldown
- GBP/USD 11-13 14:13 price 1.32322 no_trade re-entry cooldown
- EUR/USD 11-13 14:11 price 1.105 holding SHORT 0.0%
- EUR/USD 11-13 14:12 price 1.105 holding SHORT 0.0%
- EUR/USD 11-13 14:13 price 1.105 holding SHORT 0.0%
- EUR/GBP 11-13 14:11 price 0.8351 no_trade re-entry cooldown
- EUR/GBP 11-13 14:12 price 0.8351 no_trade re-entry cooldown
- EUR/GBP 11-13 14:13 price 0.8351 no_trade re-entry cooldown
