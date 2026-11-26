# Bot report (generated 2026-11-26 16:48 UTC)

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
| Bitcoin 15m | 11-26 16:48 | 1439 | 1 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-26 16:48 | 1378 | 3 | 0 | 43 | 33 | -0.63 |  |
| GBP/USD | 11-26 16:48 | 1378 | 5 | 0 | 38 | 32 | -0.15 |  |
| EUR/USD | 11-26 16:48 | 1378 | 3 | 0 | 40 | 38 | +0.09 |  |
| EUR/GBP | 11-26 16:48 | 1378 | 5 | 0 | 40 | 22 | -0.82 |  |

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
- 2026-11-26 16:06 UTC AlpacaCrypto: balance 889.38, equity 977.76, free 889.38
- 2026-11-26 16:29 UTC Oanda: balance 674.2016, equity 674.2016, free 674.2016

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-26 11:21,GBP/USD,sell,broker,,1.31007,,,,,filled,closed by broker stop/TP; P/L -5.9500
- 2026-11-26 11:22,EUR/USD,buy,2616,1.09724,1.09707,-0.0155,10000.0,,10000,filled,conf 4
- 2026-11-26 14:06,EUR/USD,sell,broker,,1.09874,,,,,filled,closed by broker stop/TP; P/L 16.7000
- 2026-11-26 14:06,EUR/GBP,buy,2624,0.83733,0.83742,0.0107,5000.0,,5000,filled,conf 3
- 2026-11-26 14:15,USD/JPY,sell,2630,159.186,159.183,-0.0019,5000.0,5000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-26 14:21,GBP/USD,buy,2634,1.3119,1.31188,-0.0015,5000.0,,5000,filled,conf 5
- 2026-11-26 14:44,GBP/USD,sell,broker,,1.31061,,,,,filled,closed by broker stop/TP; P/L -6.3500
- 2026-11-26 16:08,EUR/GBP,sell,broker,,0.83684,,,,,filled,closed by broker stop/TP; P/L -3.8403

## Recent Gemini decisions
- 2026-11-26 09:16,EUR/GBP,buy,long,0.83709,0.00014,0.83704,0.836927,0.836872,57.0,0.000242,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Bullish EMA alignment and RSI suppo
- 2026-11-26 10:25,GBP/USD,buy,long,1.31089,0.0002,1.310867,1.310729,1.310561,52.9,0.000602,3,4,+0.14% (take profit) or -0.09% (stop loss); set from recent volatility,Moving averages aligned upward; but
- 2026-11-26 11:22,EUR/USD,buy,long,1.09724,0.00015,1.097279,1.097114,1.096901,52.7,0.00055,3,4,+0.15% (take profit) or -0.10% (stop loss); set from recent volatility,Price is consolidated with favorabl
- 2026-11-26 14:06,EUR/GBP,buy,long,0.83733,0.00013,0.837407,0.837268,0.837099,53.0,0.000292,3,3,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Price is capped under EMA9 with re
- 2026-11-26 14:21,GBP/USD,buy,long,1.3119,0.00018,1.311105,1.310862,1.310693,63.2,0.000628,3,5,+0.14% (take profit) or -0.10% (stop loss); set from recent volatility,Strong EMA crossover and momentum f

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-26 16:46 price 60489.34 holding 1.4%
- Bitcoin 15m 11-26 16:47 price 60451.32 holding 1.3%
- Bitcoin 15m 11-26 16:48 price 60470.1 holding 1.3%
- USD/JPY 11-26 16:46 price 159.294 no_trade re-entry cooldown
- USD/JPY 11-26 16:47 price 159.294 no_trade re-entry cooldown
- USD/JPY 11-26 16:48 price 159.294 no_trade re-entry cooldown
- GBP/USD 11-26 16:46 price 1.31062 no_trade re-entry cooldown
- GBP/USD 11-26 16:47 price 1.31062 no_trade re-entry cooldown
- GBP/USD 11-26 16:48 price 1.31062 no_trade re-entry cooldown
- EUR/USD 11-26 16:46 price 1.09694 no_trade re-entry cooldown
- EUR/USD 11-26 16:47 price 1.09694 no_trade re-entry cooldown
- EUR/USD 11-26 16:48 price 1.09694 no_trade re-entry cooldown
- EUR/GBP 11-26 16:46 price 0.83698 no_trade re-entry cooldown
- EUR/GBP 11-26 16:47 price 0.83698 no_trade re-entry cooldown
- EUR/GBP 11-26 16:48 price 0.83698 no_trade re-entry cooldown
