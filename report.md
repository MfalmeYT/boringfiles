# Bot report (generated 2026-11-19 00:12 UTC)

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
| Bitcoin | 11-19 00:12 | 1439 | 5 | 0 | 29 | 7 | -18.45 | yes |
| Gold USD | 11-19 00:12 | 1439 | 1 | 0 | 10 | 10 | -5.72 |  |
| USD/JPY | 11-19 00:12 | 1378 | 3 | 0 | 23 | 35 | -0.20 |  |
| GBP/USD | 11-19 00:12 | 1378 | 3 | 0 | 19 | 37 | +0.02 | yes |
| EUR/USD | 11-19 00:12 | 1378 | 5 | 1 | 23 | 39 | +0.13 | yes |
| EUR/GBP | 11-19 00:12 | 1378 | 4 | 1 | 23 | 22 | -0.49 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x1 EUR/USD: OANDA candles 502: temporary gateway error (HTML page)
- x1 EUR/GBP: OANDA candles 504: temporary gateway error (HTML page)

## Latest closed trades
- Bitcoin: long +0.57%
- Bitcoin: long -0.72%
- Bitcoin: long -0.72%
- Bitcoin: long -0.68%
- Bitcoin: long -1.11%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- Gold USD: long -0.56%
- Gold USD: long -0.77%
- Gold USD: long -1.11%
- USD/JPY: long -0.11%
- USD/JPY: long +0.14%
- USD/JPY: short +0.11%
- USD/JPY: short +0.01%
- USD/JPY: short -0.09%
- USD/JPY totals: long 12 trades -0.14%, short 11 trades -0.06%
- GBP/USD: long -0.01%
- GBP/USD: short -0.11%
- GBP/USD: short -0.02%
- GBP/USD: short +0.12%
- GBP/USD: short +0.18%
- GBP/USD totals: long 10 trades +0.12%, short 9 trades -0.09%
- EUR/USD: long -0.10%
- EUR/USD: short -0.07%
- EUR/USD: short +0.13%
- EUR/USD: short +0.16%
- EUR/USD: short -0.08%
- EUR/USD totals: long 13 trades -0.49%, short 10 trades +0.62%
- EUR/GBP: short +0.10%
- EUR/GBP: short -0.03%
- EUR/GBP: long -0.06%
- EUR/GBP: long +0.12%
- EUR/GBP: long -0.08%
- EUR/GBP totals: long 16 trades -0.42%, short 7 trades -0.08%

## Latest log rows
- Bitcoin 11-19 00:10 price 62700.95 holding 0.4%
- Bitcoin 11-19 00:11 price 62654.95 holding 0.3%
- Bitcoin 11-19 00:12 price 62644.76 holding 0.3%
- Gold USD 11-19 00:10 price 3739.52 no_trade max 3 open positions reached
- Gold USD 11-19 00:11 price 3739.52 no_trade max 3 open positions reached
- Gold USD 11-19 00:12 price 3739.52 no_trade max 3 open positions reached
- USD/JPY 11-19 00:10 price 159.386 no_trade max 3 open positions reached
- USD/JPY 11-19 00:11 price 159.386 no_trade max 3 open positions reached
- USD/JPY 11-19 00:12 price 159.386 no_trade max 3 open positions reached
- GBP/USD 11-19 00:10 price 1.31462 holding SHORT 0.0%
- GBP/USD 11-19 00:11 price 1.31462 holding SHORT 0.0%
- GBP/USD 11-19 00:12 price 1.31462 holding SHORT 0.0%
- EUR/USD 11-19 00:10 price 1.09716 holding -0.0%
- EUR/USD 11-19 00:11 price 1.09716 holding -0.0%
- EUR/USD 11-19 00:12 price 1.09716 holding -0.0%
- EUR/GBP 11-19 00:10 price 0.83459 no_trade re-entry cooldown
- EUR/GBP 11-19 00:11 price 0.83459 no_trade re-entry cooldown
- EUR/GBP 11-19 00:12 price 0.83459 no_trade re-entry cooldown
