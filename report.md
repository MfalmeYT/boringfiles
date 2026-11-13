# Bot report (generated 2026-11-13 10:17 UTC)

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
| Bitcoin | 11-13 10:17 | 1439 | 2 | 0 | 1 | 0 | -0.86 | yes |
| Gold USD | 11-13 10:17 | 703 | 1 | 0 | 1 | 0 | -0.44 |  |
| USD/JPY | 11-13 10:17 | 1378 | 3 | 145 | 10 | 30 | -0.18 | yes |
| GBP/USD | 11-13 10:17 | 1378 | 1 | 0 | 9 | 56 | +0.12 |  |
| EUR/USD | 11-13 10:17 | 1378 | 2 | 0 | 10 | 30 | -0.20 | yes |
| EUR/GBP | 11-13 10:17 | 1378 | 2 | 132 | 11 | 9 | -0.38 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x145 USD/JPY: Order buy cancelled: INSUFFICIENT_MARGIN
- x132 EUR/GBP: Order buy cancelled: INSUFFICIENT_MARGIN

## Latest closed trades
- Bitcoin: long -0.86%
- Gold USD: long -0.44%
- USD/JPY: long -0.13%
- USD/JPY: long -0.10%
- USD/JPY: long -0.11%
- USD/JPY: long -0.07%
- USD/JPY: long -0.13%
- GBP/USD: long -0.04%
- GBP/USD: long +0.06%
- GBP/USD: long -0.03%
- GBP/USD: long -0.06%
- GBP/USD: short -0.07%
- GBP/USD totals: long 8 trades +0.19%, short 1 trades -0.07%
- EUR/USD: long -0.07%
- EUR/USD: long -0.06%
- EUR/USD: long -0.07%
- EUR/USD: long -0.10%
- EUR/USD: long -0.07%
- EUR/GBP: long -0.06%
- EUR/GBP: long -0.07%
- EUR/GBP: long -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.03%

## Latest log rows
- Bitcoin 11-13 10:15 price 69355.27 holding 0.7%
- Bitcoin 11-13 10:16 price 69244.82 holding 0.6%
- Bitcoin 11-13 10:17 price 69275.68 holding 0.6%
- Gold USD 11-13 10:15 price 3886.82 no_trade score below 2
- Gold USD 11-13 10:16 price 3886.41 no_trade score below 2
- Gold USD 11-13 10:17 price 3885.91 no_trade score below 2
- USD/JPY 11-13 10:15 price 159.892 holding SHORT -0.0%
- USD/JPY 11-13 10:16 price 159.892 holding SHORT -0.0%
- USD/JPY 11-13 10:17 price 159.892 holding SHORT -0.0%
- GBP/USD 11-13 10:15 price 1.32319 no_trade max 3 open positions reached
- GBP/USD 11-13 10:16 price 1.32319 no_trade max 3 open positions reached
- GBP/USD 11-13 10:17 price 1.32319 no_trade max 3 open positions reached
- EUR/USD 11-13 10:15 price 1.1055 holding -0.0%
- EUR/USD 11-13 10:16 price 1.1055 holding -0.0%
- EUR/USD 11-13 10:17 price 1.1055 holding -0.0%
- EUR/GBP 11-13 10:15 price 0.83548 no_trade re-entry cooldown
- EUR/GBP 11-13 10:16 price 0.83548 no_trade re-entry cooldown
- EUR/GBP 11-13 10:17 price 0.83548 no_trade re-entry cooldown
