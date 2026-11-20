# Bot report (generated 2026-11-20 08:44 UTC)

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
| Bitcoin 15m | 11-20 08:44 | 595 | 0 | 0 | 0 | - | +0.00 |  |
| Gold USD | 11-20 08:44 | 595 | 1 | 0 | 10 | 10 | -5.72 | yes |
| USD/JPY | 11-20 08:44 | 585 | 2 | 0 | 24 | 33 | -0.24 | yes |
| GBP/USD | 11-20 08:44 | 585 | 2 | 0 | 22 | 36 | +0.09 |  |
| EUR/USD | 11-20 08:44 | 585 | 1 | 0 | 25 | 40 | +0.14 |  |
| EUR/GBP | 11-20 08:44 | 585 | 1 | 0 | 24 | 21 | -0.54 |  |

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
- none

## OANDA 401 errors, last 24h
- count: 0

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
- USD/JPY: long +0.14%
- USD/JPY: short +0.11%
- USD/JPY: short +0.01%
- USD/JPY: short -0.09%
- USD/JPY: short -0.04%
- USD/JPY totals: long 12 trades -0.14%, short 12 trades -0.10%
- GBP/USD: short +0.12%
- GBP/USD: short +0.18%
- GBP/USD: short +0.21%
- GBP/USD: short -0.08%
- GBP/USD: long -0.06%
- GBP/USD totals: long 11 trades +0.06%, short 11 trades +0.03%
- EUR/USD: short +0.13%
- EUR/USD: short +0.16%
- EUR/USD: short -0.08%
- EUR/USD: long -0.09%
- EUR/USD: long +0.10%
- EUR/USD totals: long 15 trades -0.48%, short 10 trades +0.62%
- EUR/GBP: short -0.03%
- EUR/GBP: long -0.06%
- EUR/GBP: long +0.12%
- EUR/GBP: long -0.08%
- EUR/GBP: long -0.05%
- EUR/GBP totals: long 17 trades -0.46%, short 7 trades -0.08%

## Account (latest hourly snapshot)
- 2026-11-20 08:40 UTC AlpacaCrypto: balance 940.42, equity 984.09, free 940.42
- 2026-11-20 08:40 UTC Oanda: balance 850.0364, equity 856.6107, free 28.8782

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-20 02:58,USD/JPY,short,1670,159.226,159.239,0.0082,10000.0,,10000,filled,conf 2
- 2026-11-20 02:58,GBP/USD,cover,broker,,1.30938,,,,,filled,closed by broker stop/TP; P/L -6.0000
- 2026-11-20 04:02,EUR/USD,buy,1676,1.0976,1.09752,-0.0073,10000.0,,10000,filled,conf 5
- 2026-11-20 04:02,EUR/GBP,sell,broker,,0.83753,,,,,filled,closed by broker stop/TP; P/L -3.8375
- 2026-11-20 06:35,GBP/USD,buy,1684,1.31134,1.31156,0.0168,5000.0,,5000,filled,conf 4
- 2026-11-20 06:35,EUR/USD,sell,broker,,1.09874,,,,,filled,closed by broker stop/TP; P/L 12.2000
- 2026-11-20 08:42,Gold USD,buy,e521cada-860a-4e96-b2e9-af564ff81a5b,3579.12,3596.6,0.4884,0.012269284,,45,filled,conf 4
- 2026-11-20 08:42,GBP/USD,sell,broker,,1.31053,,,,,filled,closed by broker stop/TP; P/L -5.1500

## Recent Gemini decisions
- 2026-11-20 02:00,GBP/USD,short,short,1.3083,0.00021,1.308926,1.309224,1.310439,34.7,0.0006,3,4,a 0.14% fall (take profit) or a 0.09% rise (stop loss); set from recent volatility,Downtrend intact with 
- 2026-11-20 02:58,USD/JPY,short,short,159.226,0.016,159.3608,159.4899,159.6124,24.2,0.1085,2,2,a 0.20% fall (take profit) or a 0.14% rise (stop loss); set from recent volatility,RSI at 24.2 indicates o
- 2026-11-20 04:02,EUR/USD,buy,long,1.0976,0.00015,1.097191,1.097111,1.097348,59.4,0.000406,3,5,+0.11% (take profit) or -0.07% (stop loss); set from recent volatility,Bullish momentum with valid 3/3 ali
- 2026-11-20 06:35,GBP/USD,buy,long,1.31134,0.00022,1.310735,1.31025,1.310353,67.5,0.000502,3,4,+0.11% (take profit) or -0.08% (stop loss); set from recent volatility,Bullish momentum is strong; but hig
- 2026-11-20 08:42,Gold USD,buy,long,3579.12,,3562.528,3556.808,3579.32,60.5,33.141,2,4,+1.50% (take profit) or -1.00% (stop loss),Bullish momentum and crossover offset by strong price resistance at EMA

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
- Bitcoin 15m 11-20 08:42 price 61830.92 holding -1.0%
- Bitcoin 15m 11-20 08:43 price 61869.24 holding -1.0%
- Bitcoin 15m 11-20 08:44 price 61903.08 holding -0.9%
- Gold USD 11-20 08:42 price 3579.12 buy conf 4: Bullish momentum and crossover offset by strong price resistance at EMA50
- Gold USD 11-20 08:43 price 3580.18 holding -0.5%
- Gold USD 11-20 08:44 price 3579.55 holding -0.5%
- USD/JPY 11-20 08:42 price 159.074 holding SHORT 0.1%
- USD/JPY 11-20 08:43 price 159.074 holding SHORT 0.1%
- USD/JPY 11-20 08:44 price 159.074 holding SHORT 0.1%
- GBP/USD 11-20 08:42 price 1.31053 sell closed by broker stop/TP; P/L -5.1500
- GBP/USD 11-20 08:43 price 1.3113 no_trade re-entry cooldown
- GBP/USD 11-20 08:44 price 1.3113 no_trade re-entry cooldown
- EUR/USD 11-20 08:42 price 1.09762 no_trade no long or short setup
- EUR/USD 11-20 08:43 price 1.09762 no_trade no long or short setup
- EUR/USD 11-20 08:44 price 1.09762 no_trade no long or short setup
- EUR/GBP 11-20 08:42 price 0.83704 no_trade max 3 open positions reached
- EUR/GBP 11-20 08:43 price 0.83704 no_trade max 3 open positions reached
- EUR/GBP 11-20 08:44 price 0.83704 no_trade max 3 open positions reached
