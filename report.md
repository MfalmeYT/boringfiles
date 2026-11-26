# Bot report (generated 2026-11-26 13:05 UTC)

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
| Bitcoin 15m | 11-26 13:05 | 1421 | 1 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-26 13:05 | 1360 | 4 | 0 | 42 | 31 | -0.64 | yes |
| GBP/USD | 11-26 13:05 | 1360 | 4 | 0 | 37 | 32 | -0.06 |  |
| EUR/USD | 11-26 13:05 | 1360 | 4 | 0 | 39 | 36 | -0.04 | yes |
| EUR/GBP | 11-26 13:05 | 1360 | 4 | 0 | 39 | 23 | -0.76 |  |

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
- USD/JPY: long -0.18%
- USD/JPY: long -0.04%
- USD/JPY: short +0.23%
- USD/JPY: short -0.06%
- USD/JPY: long -0.08%
- USD/JPY totals: long 19 trades -0.48%, short 23 trades -0.15%
- GBP/USD: short -0.12%
- GBP/USD: long -0.06%
- GBP/USD: long -0.04%
- GBP/USD: short -0.05%
- GBP/USD: long -0.06%
- GBP/USD totals: long 18 trades -0.14%, short 19 trades +0.09%
- EUR/USD: short +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD: long -0.08%
- EUR/USD: long -0.04%
- EUR/USD totals: long 24 trades -0.65%, short 15 trades +0.60%
- EUR/GBP: long +0.13%
- EUR/GBP: long -0.11%
- EUR/GBP: short -0.11%
- EUR/GBP: short -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP totals: long 24 trades -0.42%, short 15 trades -0.34%

## Account (latest hourly snapshot)
- 2026-11-26 12:10 UTC AlpacaCrypto: balance 889.38, equity 978.2, free 889.38
- 2026-11-26 12:33 UTC Oanda: balance 667.9140, equity 670.1977, free 200.7457

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-26 07:25,GBP/USD,cover,broker,,1.31096,,,,,filled,closed by broker stop/TP; P/L -4.3500
- 2026-11-26 07:30,EUR/USD,buy,2594,1.09714,1.09744,0.0273,10000.0,,10000,filled,conf 4
- 2026-11-26 08:22,EUR/USD,sell,broker,,1.09669,,,,,filled,closed by broker stop/TP; P/L -7.5000
- 2026-11-26 09:16,EUR/GBP,buy,2602,0.83709,0.83713,0.0048,5000.0,,5000,filled,conf 4
- 2026-11-26 10:12,EUR/GBP,sell,broker,,0.83665,,,,,filled,closed by broker stop/TP; P/L -3.1778
- 2026-11-26 10:25,GBP/USD,buy,2610,1.31089,1.31126,0.0282,5000.0,,5000,filled,conf 4
- 2026-11-26 11:21,GBP/USD,sell,broker,,1.31007,,,,,filled,closed by broker stop/TP; P/L -5.9500
- 2026-11-26 11:22,EUR/USD,buy,2616,1.09724,1.09707,-0.0155,10000.0,,10000,filled,conf 4

## Recent Gemini decisions
- 2026-11-26 06:16,GBP/USD,short,short,1.31029,0.00018,1.310212,1.31047,1.310461,46.0,0.000441,3,4,a 0.10% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Favorable score 3/3;
- 2026-11-26 07:30,EUR/USD,buy,long,1.09714,0.00015,1.096528,1.096486,1.096525,62.6,0.000363,3,4,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Fresh bullish crossover with upwar
- 2026-11-26 09:16,EUR/GBP,buy,long,0.83709,0.00014,0.83704,0.836927,0.836872,57.0,0.000242,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Bullish EMA alignment and RSI suppo
- 2026-11-26 10:25,GBP/USD,buy,long,1.31089,0.0002,1.310867,1.310729,1.310561,52.9,0.000602,3,4,+0.14% (take profit) or -0.09% (stop loss); set from recent volatility,Moving averages aligned upward; but
- 2026-11-26 11:22,EUR/USD,buy,long,1.09724,0.00015,1.097279,1.097114,1.096901,52.7,0.00055,3,4,+0.15% (take profit) or -0.10% (stop loss); set from recent volatility,Price is consolidated with favorabl

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-26 13:03 price 60755.67 holding 1.8%
- Bitcoin 15m 11-26 13:04 price 60737.03 holding 1.8%
- Bitcoin 15m 11-26 13:05 price 60742.26 holding 1.8%
- USD/JPY 11-26 13:03 price 159.256 holding 0.0%
- USD/JPY 11-26 13:04 price 159.256 holding 0.0%
- USD/JPY 11-26 13:05 price 159.256 holding 0.0%
- GBP/USD 11-26 13:03 price 1.31078 no_trade re-entry cooldown
- GBP/USD 11-26 13:04 price 1.31078 no_trade re-entry cooldown
- GBP/USD 11-26 13:05 price 1.31078 no_trade re-entry cooldown
- EUR/USD 11-26 13:03 price 1.0978 holding 0.1%
- EUR/USD 11-26 13:04 price 1.0978 holding 0.1%
- EUR/USD 11-26 13:05 price 1.0978 holding 0.1%
- EUR/GBP 11-26 13:03 price 0.83752 no_trade re-entry cooldown
- EUR/GBP 11-26 13:04 price 0.83752 no_trade re-entry cooldown
- EUR/GBP 11-26 13:05 price 0.83752 no_trade re-entry cooldown
