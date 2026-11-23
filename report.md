# Bot report (generated 2026-11-23 07:28 UTC)

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
| Bitcoin 15m | 11-23 07:28 | 1440 | 1 | 0 | 1 | 0 | -2.45 | yes |
| USD/JPY | 11-23 07:28 | 509 | 2 | 0 | 28 | 36 | -0.12 | yes |
| GBP/USD | 11-23 07:28 | 509 | 2 | 0 | 25 | 36 | +0.04 | yes |
| EUR/USD | 11-23 07:28 | 509 | 1 | 0 | 28 | 36 | -0.08 |  |
| EUR/GBP | 11-23 07:28 | 509 | 1 | 0 | 26 | 23 | -0.48 |  |

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
- USD/JPY: short -0.04%
- USD/JPY: short +0.20%
- USD/JPY: short -0.11%
- USD/JPY: short +0.11%
- USD/JPY: short -0.08%
- USD/JPY totals: long 12 trades -0.14%, short 16 trades +0.02%
- GBP/USD: short -0.08%
- GBP/USD: long -0.06%
- GBP/USD: short -0.17%
- GBP/USD: short +0.19%
- GBP/USD: short -0.07%
- GBP/USD totals: long 11 trades +0.06%, short 14 trades -0.02%
- EUR/USD: long -0.09%
- EUR/USD: long +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long -0.07%
- EUR/USD: short -0.04%
- EUR/USD totals: long 16 trades -0.55%, short 12 trades +0.47%
- EUR/GBP: long +0.12%
- EUR/GBP: long -0.08%
- EUR/GBP: long -0.05%
- EUR/GBP: long +0.09%
- EUR/GBP: short -0.02%
- EUR/GBP totals: long 18 trades -0.38%, short 8 trades -0.10%

## Account (latest hourly snapshot)
- 2026-11-23 06:51 UTC Oanda: balance 799.9883, equity 797.9966, free 123.0566
- 2026-11-23 07:28 UTC AlpacaCrypto: balance 890.43, equity 980.03, free 890.43

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-22 23:04,EUR/USD,short,1762,1.09736,1.09712,-0.0219,10000.0,,10000,filled,conf 3
- 2026-11-23 00:28,Gold USD,buy,c8f05e3b-5410-42f7-8d08-1b89a41d7206,3566.665,3580.95,0.4005,0.012320095,,45,filled,conf 4
- 2026-11-23 00:28,GBP/USD,cover,broker,,1.3104,,,,,filled,closed by broker stop/TP; P/L -3.6250
- 2026-11-23 00:34,EUR/USD,cover,1770,1.09782,1.09788,0.0055,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-23 00:35,EUR/GBP,short,1772,0.83794,0.83778,-0.0191,10000.0,,10000,filled,conf 4
- 2026-11-23 02:27,USD/JPY,buy,1780,158.914,158.881,-0.0208,2500.0,,2500,filled,conf 4
- 2026-11-23 07:15,EUR/GBP,cover,1786,0.83814,0.83823,0.0107,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-23 07:16,GBP/USD,buy,1788,1.31239,1.31281,0.032,10000.0,,10000,filled,conf 4

## Recent Gemini decisions
- 2026-11-22 23:04,EUR/USD,short,short,1.09736,0.00017,1.096955,1.097021,1.097265,52.9,0.000619,2,3,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Price above EMA50 o
- 2026-11-23 00:28,Gold USD,buy,long,3566.66,,3558.779,3552.364,3549.354,64.5,22.75,3,4,+1.50% (take profit) or -1.00% (stop loss),Uptrend and score 3/3; but RSI 64.5 lacks fresh crossover momentum
- 2026-11-23 00:35,EUR/GBP,short,short,0.83794,0.00014,0.838017,0.838038,0.837923,47.4,0.000292,2,4,a 0.10% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Fresh EMA crossover
- 2026-11-23 02:27,USD/JPY,buy,long,158.914,0.012,158.8811,158.8095,158.7902,58.9,0.0961,3,4,+0.18% (take profit) or -0.12% (stop loss); set from recent volatility,Strong EMA trend and perfect checks; b
- 2026-11-23 07:16,GBP/USD,buy,long,1.31239,0.0002,1.312141,1.311511,1.310832,65.3,0.000542,3,4,+0.12% (take profit) or -0.08% (stop loss); set from recent volatility,Uptrend intact but minor pullback f

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-23 07:26 price 61371.22 holding 2.1%
- Bitcoin 15m 11-23 07:27 price 61405.85 holding 2.1%
- Bitcoin 15m 11-23 07:28 price 61417.75 holding 2.1%
- USD/JPY 11-23 07:26 price 159.022 holding 0.1%
- USD/JPY 11-23 07:27 price 159.022 holding 0.1%
- USD/JPY 11-23 07:28 price 159.022 holding 0.1%
- GBP/USD 11-23 07:26 price 1.31239 holding -0.0%
- GBP/USD 11-23 07:27 price 1.31239 holding -0.0%
- GBP/USD 11-23 07:28 price 1.31239 holding -0.0%
- EUR/USD 11-23 07:26 price 1.09995 no_trade max 3 open positions reached
- EUR/USD 11-23 07:27 price 1.09995 no_trade max 3 open positions reached
- EUR/USD 11-23 07:28 price 1.09995 no_trade max 3 open positions reached
- EUR/GBP 11-23 07:26 price 0.83814 no_trade re-entry cooldown
- EUR/GBP 11-23 07:27 price 0.83814 no_trade re-entry cooldown
- EUR/GBP 11-23 07:28 price 0.83814 no_trade re-entry cooldown
