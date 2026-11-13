# Bot report (generated 2026-11-13 07:03 UTC)

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
| Bitcoin | 11-13 07:03 | 1440 | 1 | 0 | 0 | - | +0.00 | yes |
| Gold USD | 11-13 07:03 | 510 | 1 | 0 | 1 | 0 | -0.44 |  |
| USD/JPY | 11-13 07:03 | 1379 | 3 | 145 | 10 | 30 | -0.18 |  |
| GBP/USD | 11-13 07:03 | 1379 | 2 | 47 | 9 | 56 | +0.12 |  |
| EUR/USD | 11-13 07:03 | 1379 | 2 | 0 | 10 | 30 | -0.20 |  |
| EUR/GBP | 11-13 07:03 | 1379 | 1 | 156 | 10 | 10 | -0.34 |  |

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

## Latest closed trades
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
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP: long -0.07%
- EUR/GBP: long -0.04%
- EUR/GBP: long -0.05%

## Latest log rows
- Bitcoin 11-13 07:01 price 69093.55 holding 0.3%
- Bitcoin 11-13 07:02 price 69184.65 holding 0.5%
- Bitcoin 11-13 07:03 price 69153.2 holding 0.4%
- Gold USD 11-13 07:01 price 3893.76 no_trade score below 2
- Gold USD 11-13 07:02 price 3894.69 no_trade score below 2
- Gold USD 11-13 07:03 price 3893.28 no_trade score below 2
- USD/JPY 11-13 07:01 price 159.78 no_trade no long or short setup
- USD/JPY 11-13 07:02 price 159.78 no_trade no long or short setup
- USD/JPY 11-13 07:03 price 159.78 no_trade no long or short setup
- GBP/USD 11-13 07:01 price 1.3235 no_trade no long or short setup
- GBP/USD 11-13 07:02 price 1.3235 no_trade no long or short setup
- GBP/USD 11-13 07:03 price 1.3235 no_trade no long or short setup
- EUR/USD 11-13 07:01 price 1.10676 no_trade re-entry cooldown
- EUR/USD 11-13 07:02 price 1.10676 no_trade re-entry cooldown
- EUR/USD 11-13 07:03 price 1.10676 no_trade re-entry cooldown
- EUR/GBP 11-13 07:01 price 0.83622 no_trade spread 0.00013 too wide vs target
- EUR/GBP 11-13 07:02 price 0.83622 no_trade spread 0.00015 too wide vs target
- EUR/GBP 11-13 07:03 price 0.83622 no_trade spread 0.00015 too wide vs target
