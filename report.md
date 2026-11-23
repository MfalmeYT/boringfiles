# Bot report (generated 2026-11-23 13:35 UTC)

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
| Bitcoin 15m | 11-23 13:35 | 1440 | 0 | 0 | 1 | 0 | -2.45 | yes |
| USD/JPY | 11-23 13:35 | 876 | 3 | 0 | 29 | 38 | +0.04 | yes |
| GBP/USD | 11-23 13:35 | 876 | 3 | 0 | 27 | 37 | +0.17 |  |
| EUR/USD | 11-23 13:35 | 876 | 2 | 0 | 29 | 34 | -0.20 |  |
| EUR/GBP | 11-23 13:35 | 876 | 2 | 0 | 26 | 23 | -0.48 | yes |

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
- GBP/USD: short -0.17%
- GBP/USD: short +0.19%
- GBP/USD: short -0.07%
- GBP/USD: long -0.05%
- GBP/USD: short +0.18%
- GBP/USD totals: long 12 trades +0.01%, short 15 trades +0.16%
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
- 2026-11-23 12:45 UTC Oanda: balance 777.9010, equity 779.0946, free 68.0184
- 2026-11-23 13:22 UTC AlpacaCrypto: balance 890.43, equity 979.42, free 890.43

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-23 08:03,GBP/USD,sell,broker,,1.31173,,,,,filled,closed by broker stop/TP; P/L -10.8000
- 2026-11-23 08:03,EUR/USD,buy,1794,1.09974,1.09943,-0.0282,10000.0,,10000,filled,conf 4
- 2026-11-23 08:45,USD/JPY,sell,broker,,159.169,,,,,filled,closed by broker stop/TP; P/L 4.4780
- 2026-11-23 09:06,EUR/USD,sell,broker,,1.09845,,,,,filled,closed by broker stop/TP; P/L -9.8000
- 2026-11-23 10:15,EUR/GBP,short,1802,0.83682,0.83675,-0.0084,10000.0,,10000,filled,conf 4
- 2026-11-23 11:03,GBP/USD,short,1810,1.3107,1.31061,-0.0069,2500.0,,2500,filled,conf 4
- 2026-11-23 12:46,USD/JPY,short,1820,158.96,158.992,0.0201,2500.0,,2500,filled,conf 5
- 2026-11-23 12:46,GBP/USD,cover,broker,,1.30833,,,,,filled,closed by broker stop/TP; P/L 5.7000

## Recent Gemini decisions
- 2026-11-23 07:16,GBP/USD,buy,long,1.31239,0.0002,1.312141,1.311511,1.310832,65.3,0.000542,3,4,+0.12% (take profit) or -0.08% (stop loss); set from recent volatility,Uptrend intact but minor pullback f
- 2026-11-23 08:03,EUR/USD,buy,long,1.09974,0.00016,1.099699,1.099132,1.09847,63.1,0.000478,3,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Uptrend intact but price pulled bac
- 2026-11-23 10:15,EUR/GBP,short,short,0.83682,0.00015,0.837004,0.837327,0.837578,30.4,0.0003,3,4,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Downtrend intact but 
- 2026-11-23 11:03,GBP/USD,short,short,1.3107,0.0002,1.311488,1.311769,1.311351,39.1,0.00075,3,4,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Strong bearish alignme
- 2026-11-23 12:46,USD/JPY,short,short,158.96,0.013,159.0435,159.0539,158.9934,39.8,0.0712,3,5,a 0.13% fall (take profit) or a 0.09% rise (stop loss); set from recent volatility,Strong bearish momentum 

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-23 13:33 price 61095.83 holding 1.6%
- Bitcoin 15m 11-23 13:34 price 61075.6 holding 1.6%
- Bitcoin 15m 11-23 13:35 price 61091.42 holding 1.6%
- USD/JPY 11-23 13:33 price 159.051 holding SHORT -0.0%
- USD/JPY 11-23 13:34 price 159.051 holding SHORT -0.0%
- USD/JPY 11-23 13:35 price 159.051 holding SHORT -0.0%
- GBP/USD 11-23 13:33 price 1.30754 no_trade re-entry cooldown
- GBP/USD 11-23 13:34 price 1.30754 no_trade re-entry cooldown
- GBP/USD 11-23 13:35 price 1.30754 no_trade re-entry cooldown
- EUR/USD 11-23 13:33 price 1.09428 no_trade max 3 open positions reached
- EUR/USD 11-23 13:34 price 1.09428 no_trade max 3 open positions reached
- EUR/USD 11-23 13:35 price 1.09428 no_trade max 3 open positions reached
- EUR/GBP 11-23 13:33 price 0.83692 holding SHORT -0.0%
- EUR/GBP 11-23 13:34 price 0.83692 holding SHORT -0.0%
- EUR/GBP 11-23 13:35 price 0.83692 holding SHORT -0.0%
