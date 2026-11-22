# Bot report (generated 2026-11-22 23:31 UTC)

## Settings (read from trader.py)
- trading enabled: True; shorting enabled: True; max open positions: 3
- entry needs 2 of 3 checks (EMA 9/21/50, RSI 45-70; short = mirror) plus Gemini confidence 1-6; model gemini-3.6-flash
- Bitcoin (off): alpaca, 5Min candles, stop 2.0% / target 2.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 60 min, signal exit on, long only
- Bitcoin 1h (off): alpaca, 1Hour candles, stop 4.0% / target 4.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 60 min, signal exit OFF, long only
- Bitcoin 15m (on): alpaca, 15Min candles, stop 2.0% / target 3.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 120 min, signal exit OFF, time stop 48h, 1Hour trend filter, pause 12h after 3 losses, long only
- Gold USD (on): alpaca, 15Min candles, stop 1.0% / target 1.5%, size $45, min confidence 3, min hold 90 min, re-entry pause 180 min, signal exit on, long only
- USD/JPY (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- GBP/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/GBP (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short

## Markets (last 24h unless noted)

| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |
|---|---|---|---|---|---|---|---|---|
| Bitcoin | 11-19 00:24 | 0 | 0 | 0 | 29 | 7 | -18.45 | yes |
| Bitcoin 1h | 11-19 00:25 | 0 | 0 | 0 | 0 | - | +0.00 |  |
| Bitcoin 15m | 11-22 23:31 | 1440 | 1 | 0 | 1 | 0 | -2.45 | yes |
| Gold USD | 11-22 23:31 | 1440 | 2 | 0 | 15 | 13 | -8.74 |  |
| USD/JPY | 11-22 23:31 | 33 | 1 | 1 | 28 | 36 | -0.12 |  |
| GBP/USD | 11-22 23:31 | 32 | 1 | 0 | 24 | 38 | +0.11 | yes |
| EUR/USD | 11-22 23:31 | 32 | 1 | 0 | 27 | 37 | -0.04 | yes |
| EUR/GBP | 11-22 23:31 | 32 | 0 | 0 | 25 | 24 | -0.45 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc1h.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc15.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x1 USD/JPY: OANDA position 401 [req #]: {"errorMessage":"Insufficient authorization to perform request."}

## OANDA 401 errors, last 24h
- count: 1; request IDs for OANDA support: 61573249626792112

## Latest closed trades
- Bitcoin: long +0.57%
- Bitcoin: long -0.72%
- Bitcoin: long -0.72%
- Bitcoin: long -0.68%
- Bitcoin: long -1.11%
- Bitcoin 15m: long -2.45%
- Gold USD: long -1.14%
- Gold USD: long -0.83%
- Gold USD: long +0.02%
- Gold USD: long -0.79%
- Gold USD: long -0.29%
- USD/JPY: short -0.04%
- USD/JPY: short +0.20%
- USD/JPY: short -0.11%
- USD/JPY: short +0.11%
- USD/JPY: short -0.08%
- USD/JPY totals: long 12 trades -0.14%, short 16 trades +0.02%
- GBP/USD: short +0.21%
- GBP/USD: short -0.08%
- GBP/USD: long -0.06%
- GBP/USD: short -0.17%
- GBP/USD: short +0.19%
- GBP/USD totals: long 11 trades +0.06%, short 13 trades +0.05%
- EUR/USD: short -0.08%
- EUR/USD: long -0.09%
- EUR/USD: long +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long -0.07%
- EUR/USD totals: long 16 trades -0.55%, short 11 trades +0.51%
- EUR/GBP: long -0.06%
- EUR/GBP: long +0.12%
- EUR/GBP: long -0.08%
- EUR/GBP: long -0.05%
- EUR/GBP: long +0.09%
- EUR/GBP totals: long 18 trades -0.38%, short 7 trades -0.08%

## Account (latest hourly snapshot)
- 2026-11-22 22:37 UTC AlpacaCrypto: balance 934.55, equity 979.04, free 934.55
- 2026-11-22 22:59 UTC Oanda: balance 821.5243, equity 821.5243, free 821.5243

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-22 03:05,Bitcoin 15m,sell,b9db1cf1-e7c6-461d-8283-70e1f2861050,59206.436,59224.2,0.03,0.000728107,0.000728107,,filled,STOP LOSS (-2.1%)
- 2026-11-22 08:36,Bitcoin 15m,buy,4e204d33-7b34-41b4-b1cb-a80b24d2bcf0,60218.875,60130.721,-0.1464,0.000734047,,45,filled,conf 4
- 2026-11-22 08:42,Gold USD,buy,33ac03bf-ea33-4ef8-84ce-20afba30e4f1,3539.78,3559.135402049,0.5468,0.012400643,,45,filled,conf 5
- 2026-11-22 19:01,Gold USD,sell,492c167d-75d8-441a-8329-e6465fd1568f,3547.28,3523.581,-0.6681,0.01236964,0.01236964,,filled,SIGNAL EXIT; score 0/3 (-0.3%)
- 2026-11-22 23:00,USD/JPY,short,1748,158.562,158.533,-0.0183,10000.0,,10000,filled,conf 4
- 2026-11-22 23:00,GBP/USD,short,1756,1.30954,1.30895,-0.0451,2500.0,,2500,filled,conf 2
- 2026-11-22 23:04,USD/JPY,cover,broker,,158.695,,,,,filled,closed by broker stop/TP; P/L -10.3110
- 2026-11-22 23:04,EUR/USD,short,1762,1.09736,1.09712,-0.0219,10000.0,,10000,filled,conf 3

## Recent Gemini decisions
- 2026-11-22 08:36,Bitcoin 15m,buy,long,60218.88,14.91,59385.111,59294.021,59420.68,72.2,283.953,2,4,+3.00% (take profit) or -2.00% (stop loss),Strong momentum and crossover offset by overbought RSI abo
- 2026-11-22 08:42,Gold USD,buy,long,3539.78,,3535.513,3535.457,3538.494,57.2,23.533,3,5,+1.50% (take profit) or -1.00% (stop loss),Fresh bullish EMA crossover with price trending up and solid RSI
- 2026-11-22 23:00,USD/JPY,short,short,158.562,0.035,158.574,158.6139,158.7357,44.2,0.0884,3,4,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Trend signals align shor
- 2026-11-22 23:00,GBP/USD,short,short,1.30954,0.00042,1.308855,1.309008,1.309559,53.7,0.000722,3,2,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Price is rising wit
- 2026-11-22 23:04,EUR/USD,short,short,1.09736,0.00017,1.096955,1.097021,1.097265,52.9,0.000619,2,3,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Price above EMA50 o

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 11-19 00:22 price 62610.04 holding 0.2%
- Bitcoin 11-19 00:23 price 62606.65 holding 0.2%
- Bitcoin 11-19 00:24 price 62630.6 holding 0.3%
- Bitcoin 1h 11-19 00:25 price 62607.78 holding 0.2%
- Bitcoin 15m 11-22 23:29 price 60932.68 holding 1.3%
- Bitcoin 15m 11-22 23:30 price 60955.29 holding 1.4%
- Bitcoin 15m 11-22 23:31 price 61098.1 holding 1.6%
- Gold USD 11-22 23:29 price 3560.7 no_trade max 3 open positions reached
- Gold USD 11-22 23:30 price 3565.45 no_trade max 3 open positions reached
- Gold USD 11-22 23:31 price 3567.55 no_trade max 3 open positions reached
- USD/JPY 11-22 23:29 price 158.667 no_trade re-entry cooldown
- USD/JPY 11-22 23:30 price 158.86 no_trade re-entry cooldown
- USD/JPY 11-22 23:31 price 158.86 no_trade re-entry cooldown
- GBP/USD 11-22 23:29 price 1.30912 holding SHORT -0.0%
- GBP/USD 11-22 23:30 price 1.30922 holding SHORT -0.0%
- GBP/USD 11-22 23:31 price 1.30922 holding SHORT -0.0%
- EUR/USD 11-22 23:29 price 1.0974 holding SHORT -0.0%
- EUR/USD 11-22 23:30 price 1.09719 holding SHORT -0.0%
- EUR/USD 11-22 23:31 price 1.09719 holding SHORT -0.0%
- EUR/GBP 11-22 23:29 price 0.83829 no_trade max 3 open positions reached
- EUR/GBP 11-22 23:30 price 0.83806 no_trade max 3 open positions reached
- EUR/GBP 11-22 23:31 price 0.83806 no_trade max 3 open positions reached
