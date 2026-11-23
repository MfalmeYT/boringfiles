# Bot report (generated 2026-11-23 12:11 UTC)

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
| Bitcoin 15m | 11-23 12:11 | 1440 | 0 | 0 | 1 | 0 | -2.45 | yes |
| USD/JPY | 11-23 12:11 | 792 | 2 | 0 | 29 | 38 | +0.04 |  |
| GBP/USD | 11-23 12:11 | 792 | 3 | 0 | 26 | 35 | -0.01 | yes |
| EUR/USD | 11-23 12:11 | 792 | 2 | 0 | 29 | 34 | -0.20 |  |
| EUR/GBP | 11-23 12:11 | 792 | 2 | 0 | 26 | 23 | -0.48 | yes |

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
- USD/JPY: short +0.20%
- USD/JPY: short -0.11%
- USD/JPY: short +0.11%
- USD/JPY: short -0.08%
- USD/JPY: long +0.16%
- USD/JPY totals: long 13 trades +0.02%, short 16 trades +0.02%
- GBP/USD: long -0.06%
- GBP/USD: short -0.17%
- GBP/USD: short +0.19%
- GBP/USD: short -0.07%
- GBP/USD: long -0.05%
- GBP/USD totals: long 12 trades +0.01%, short 14 trades -0.02%
- EUR/USD: long +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long -0.07%
- EUR/USD: short -0.04%
- EUR/USD: long -0.12%
- EUR/USD totals: long 17 trades -0.67%, short 12 trades +0.47%
- EUR/GBP: long +0.12%
- EUR/GBP: long -0.08%
- EUR/GBP: long -0.05%
- EUR/GBP: long +0.09%
- EUR/GBP: short -0.02%
- EUR/GBP totals: long 18 trades -0.38%, short 8 trades -0.10%

## Account (latest hourly snapshot)
- 2026-11-23 11:24 UTC AlpacaCrypto: balance 890.43, equity 979.93, free 890.43
- 2026-11-23 11:46 UTC Oanda: balance 777.9010, equity 778.5221, free 66.8471

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-23 07:15,EUR/GBP,cover,1786,0.83814,0.83823,0.0107,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-23 07:16,GBP/USD,buy,1788,1.31239,1.31281,0.032,10000.0,,10000,filled,conf 4
- 2026-11-23 08:03,GBP/USD,sell,broker,,1.31173,,,,,filled,closed by broker stop/TP; P/L -10.8000
- 2026-11-23 08:03,EUR/USD,buy,1794,1.09974,1.09943,-0.0282,10000.0,,10000,filled,conf 4
- 2026-11-23 08:45,USD/JPY,sell,broker,,159.169,,,,,filled,closed by broker stop/TP; P/L 4.4780
- 2026-11-23 09:06,EUR/USD,sell,broker,,1.09845,,,,,filled,closed by broker stop/TP; P/L -9.8000
- 2026-11-23 10:15,EUR/GBP,short,1802,0.83682,0.83675,-0.0084,10000.0,,10000,filled,conf 4
- 2026-11-23 11:03,GBP/USD,short,1810,1.3107,1.31061,-0.0069,2500.0,,2500,filled,conf 4

## Recent Gemini decisions
- 2026-11-23 02:27,USD/JPY,buy,long,158.914,0.012,158.8811,158.8095,158.7902,58.9,0.0961,3,4,+0.18% (take profit) or -0.12% (stop loss); set from recent volatility,Strong EMA trend and perfect checks; b
- 2026-11-23 07:16,GBP/USD,buy,long,1.31239,0.0002,1.312141,1.311511,1.310832,65.3,0.000542,3,4,+0.12% (take profit) or -0.08% (stop loss); set from recent volatility,Uptrend intact but minor pullback f
- 2026-11-23 08:03,EUR/USD,buy,long,1.09974,0.00016,1.099699,1.099132,1.09847,63.1,0.000478,3,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Uptrend intact but price pulled bac
- 2026-11-23 10:15,EUR/GBP,short,short,0.83682,0.00015,0.837004,0.837327,0.837578,30.4,0.0003,3,4,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Downtrend intact but 
- 2026-11-23 11:03,GBP/USD,short,short,1.3107,0.0002,1.311488,1.311769,1.311351,39.1,0.00075,3,4,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Strong bearish alignme

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-23 12:09 price 61320 holding 2.0%
- Bitcoin 15m 11-23 12:10 price 61363.25 holding 2.0%
- Bitcoin 15m 11-23 12:11 price 61332.89 holding 2.0%
- USD/JPY 11-23 12:09 price 159.09 no_trade max 3 open positions reached
- USD/JPY 11-23 12:10 price 159.09 no_trade max 3 open positions reached
- USD/JPY 11-23 12:11 price 159.09 no_trade max 3 open positions reached
- GBP/USD 11-23 12:09 price 1.30977 holding SHORT 0.1%
- GBP/USD 11-23 12:10 price 1.30977 holding SHORT 0.1%
- GBP/USD 11-23 12:11 price 1.30977 holding SHORT 0.1%
- EUR/USD 11-23 12:09 price 1.09606 no_trade max 3 open positions reached
- EUR/USD 11-23 12:10 price 1.09606 no_trade max 3 open positions reached
- EUR/USD 11-23 12:11 price 1.09606 no_trade max 3 open positions reached
- EUR/GBP 11-23 12:09 price 0.83682 holding SHORT -0.0%
- EUR/GBP 11-23 12:10 price 0.83682 holding SHORT -0.0%
- EUR/GBP 11-23 12:11 price 0.83682 holding SHORT -0.0%
