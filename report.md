# Bot report (generated 2026-11-26 18:20 UTC)

## Settings (read from trader.py)
- trading enabled: True; shorting enabled: True; max open positions: 3
- entry needs 2 of 3 checks (EMA 9/21/50, RSI 45-70; short = mirror) plus Gemini confidence 1-6; model gemini-3.6-flash
- Bitcoin 15m (on): alpaca, 15Min candles, stop 2.0% / target 3.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 120 min, signal exit OFF, time stop 48h, 1Hour trend filter, pause 12h after 3 losses, long only
- USD/JPY (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- GBP/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/GBP (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short

## Markets (last 24h unless noted)

| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |
|---|---|---|---|---|---|---|---|---|
| Bitcoin 15m | 11-26 18:20 | 1439 | 0 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-26 18:20 | 1378 | 4 | 0 | 43 | 33 | -0.63 | yes |
| GBP/USD | 11-26 18:20 | 1378 | 5 | 0 | 38 | 32 | -0.15 |  |
| EUR/USD | 11-26 18:20 | 1378 | 4 | 0 | 40 | 38 | +0.09 | yes |
| EUR/GBP | 11-26 18:20 | 1378 | 4 | 0 | 40 | 22 | -0.82 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc15.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- none

## OANDA 401 errors, last 24h
- count: 0

## Latest closed trades
- Bitcoin 15m: long -2.45%
- Bitcoin 15m: long +3.03%
- Bitcoin 15m: long -2.51%
- Bitcoin 15m: long -2.45%
- USD/JPY: long -0.04%
- USD/JPY: short +0.23%
- USD/JPY: short -0.06%
- USD/JPY: long -0.08%
- USD/JPY: long +0.00%
- USD/JPY totals: long 20 trades -0.48%, short 23 trades -0.15%
- GBP/USD: long -0.06%
- GBP/USD: long -0.04%
- GBP/USD: short -0.05%
- GBP/USD: long -0.06%
- GBP/USD: long -0.10%
- GBP/USD totals: long 19 trades -0.24%, short 19 trades +0.09%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD: long -0.08%
- EUR/USD: long -0.04%
- EUR/USD: long +0.14%
- EUR/USD totals: long 25 trades -0.51%, short 15 trades +0.60%
- EUR/GBP: long -0.11%
- EUR/GBP: short -0.11%
- EUR/GBP: short -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP totals: long 25 trades -0.48%, short 15 trades -0.34%

## Account (latest hourly snapshot)
- 2026-11-26 17:28 UTC Oanda: balance 674.2016, equity 672.5680, free 203.1880
- 2026-11-26 18:04 UTC AlpacaCrypto: balance 889.38, equity 977.94, free 889.38

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-26 14:06,EUR/USD,sell,broker,,1.09874,,,,,filled,closed by broker stop/TP; P/L 16.7000
- 2026-11-26 14:06,EUR/GBP,buy,2624,0.83733,0.83742,0.0107,5000.0,,5000,filled,conf 3
- 2026-11-26 14:15,USD/JPY,sell,2630,159.186,159.183,-0.0019,5000.0,5000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-26 14:21,GBP/USD,buy,2634,1.3119,1.31188,-0.0015,5000.0,,5000,filled,conf 5
- 2026-11-26 14:44,GBP/USD,sell,broker,,1.31061,,,,,filled,closed by broker stop/TP; P/L -6.3500
- 2026-11-26 16:08,EUR/GBP,sell,broker,,0.83684,,,,,filled,closed by broker stop/TP; P/L -3.8403
- 2026-11-26 17:06,EUR/USD,short,2642,1.09708,1.09695,-0.0118,10000.0,,10000,filled,conf 4
- 2026-11-26 17:15,USD/JPY,buy,2648,159.31,159.318,0.005,5000.0,,5000,filled,conf 4

## Recent Gemini decisions
- 2026-11-26 11:22,EUR/USD,buy,long,1.09724,0.00015,1.097279,1.097114,1.096901,52.7,0.00055,3,4,+0.15% (take profit) or -0.10% (stop loss); set from recent volatility,Price is consolidated with favorabl
- 2026-11-26 14:06,EUR/GBP,buy,long,0.83733,0.00013,0.837407,0.837268,0.837099,53.0,0.000292,3,3,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Price is capped under EMA9 with re
- 2026-11-26 14:21,GBP/USD,buy,long,1.3119,0.00018,1.311105,1.310862,1.310693,63.2,0.000628,3,5,+0.14% (take profit) or -0.10% (stop loss); set from recent volatility,Strong EMA crossover and momentum f
- 2026-11-26 17:06,EUR/USD,short,short,1.09708,0.00016,1.097364,1.09748,1.097305,43.5,0.000456,3,4,a 0.12% fall (take profit) or a 0.08% rise (stop loss); set from recent volatility,Strong bearish align
- 2026-11-26 17:15,USD/JPY,buy,long,159.31,0.014,159.2832,159.2623,159.2285,61.8,0.0406,3,4,+0.08% (take profit) or -0.05% (stop loss); set from recent volatility,Strong trend alignment and score; but R

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-26 18:18 price 60454.4 holding 1.3%
- Bitcoin 15m 11-26 18:19 price 60452.84 holding 1.3%
- Bitcoin 15m 11-26 18:20 price 60460.95 holding 1.3%
- USD/JPY 11-26 18:18 price 159.298 holding -0.0%
- USD/JPY 11-26 18:19 price 159.298 holding -0.0%
- USD/JPY 11-26 18:20 price 159.298 holding -0.0%
- GBP/USD 11-26 18:18 price 1.3107 no_trade max 3 open positions reached
- GBP/USD 11-26 18:19 price 1.3107 no_trade max 3 open positions reached
- GBP/USD 11-26 18:20 price 1.3107 no_trade max 3 open positions reached
- EUR/USD 11-26 18:18 price 1.09694 holding SHORT 0.0%
- EUR/USD 11-26 18:19 price 1.09694 holding SHORT 0.0%
- EUR/USD 11-26 18:20 price 1.09694 holding SHORT 0.0%
- EUR/GBP 11-26 18:18 price 0.83694 no_trade re-entry cooldown
- EUR/GBP 11-26 18:19 price 0.83694 no_trade re-entry cooldown
- EUR/GBP 11-26 18:20 price 0.83694 no_trade re-entry cooldown
