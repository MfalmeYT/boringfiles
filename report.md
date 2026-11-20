# Bot report (generated 2026-11-20 21:43 UTC)

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
| Bitcoin 15m | 11-20 21:43 | 1374 | 0 | 0 | 0 | - | +0.00 |  |
| Gold USD | 11-20 21:43 | 1374 | 1 | 0 | 11 | 9 | -6.86 |  |
| USD/JPY | 11-20 21:43 | 1364 | 4 | 0 | 27 | 37 | -0.04 |  |
| GBP/USD | 11-20 21:43 | 1364 | 4 | 0 | 24 | 38 | +0.11 |  |
| EUR/USD | 11-20 21:43 | 1364 | 3 | 0 | 27 | 37 | -0.04 |  |
| EUR/GBP | 11-20 21:43 | 1364 | 2 | 0 | 25 | 24 | -0.45 |  |

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
- Gold USD: long -0.55%
- Gold USD: long -0.56%
- Gold USD: long -0.77%
- Gold USD: long -1.11%
- Gold USD: long -1.14%
- USD/JPY: short -0.09%
- USD/JPY: short -0.04%
- USD/JPY: short +0.20%
- USD/JPY: short -0.11%
- USD/JPY: short +0.11%
- USD/JPY totals: long 12 trades -0.14%, short 15 trades +0.10%
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
- 2026-11-20 21:27 UTC AlpacaCrypto: balance 982.36, equity 982.36, free 982.36
- 2026-11-20 21:27 UTC Oanda: balance 809.6521, equity 821.6672, free 134.1135

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-20 15:10,Bitcoin 15m,sell,4d7660c6-b769-4f98-8d29-a8740a1aa770,61169.9,61034.0,-0.2222,0.000704643,0.000704643,,filled,STOP LOSS (-2.1%)
- 2026-11-20 15:37,EUR/USD,buy,1716,1.09827,1.09906,0.0719,10000.0,,10000,filled,conf 4
- 2026-11-20 16:15,GBP/USD,short,1724,1.31018,1.31011,-0.0053,2500.0,,2500,filled,conf 4
- 2026-11-20 17:44,EUR/USD,sell,broker,,1.09747,,,,,filled,closed by broker stop/TP; P/L -15.9000
- 2026-11-20 18:00,USD/JPY,short,1732,158.772,158.747,-0.0157,5000.0,,5000,filled,conf 4
- 2026-11-20 21:30,USD/JPY,cover,1738,158.592,158.614,0.0139,5000.0,5000.0,,filled,WEEKEND FLATTEN (0.1%)
- 2026-11-20 21:30,GBP/USD,cover,1742,1.30774,1.30785,0.0084,2500.0,2500.0,,filled,WEEKEND FLATTEN (0.2%)
- 2026-11-20 21:30,EUR/GBP,sell,1746,0.83837,0.83827,-0.0119,5000.0,5000.0,,filled,WEEKEND FLATTEN (0.1%)

## Recent Gemini decisions
- 2026-11-20 13:03,USD/JPY,short,short,158.758,0.014,158.819,158.9015,159.0954,39.9,0.1217,3,4,a 0.23% fall (take profit) or a 0.15% rise (stop loss); set from recent volatility,Full bearish indicator a
- 2026-11-20 13:25,EUR/GBP,buy,long,0.83764,0.00014,0.837241,0.837136,0.837255,56.8,0.000447,3,5,+0.16% (take profit) or -0.11% (stop loss); set from recent volatility,Fresh bullish EMA crossover with p
- 2026-11-20 15:37,EUR/USD,buy,long,1.09827,0.00015,1.098373,1.098024,1.097752,53.5,0.000785,3,4,+0.21% (take profit) or -0.14% (stop loss); set from recent volatility,Bullish alignment and RSI support 
- 2026-11-20 16:15,GBP/USD,short,short,1.31018,0.00018,1.31089,1.310945,1.310759,44.5,0.000989,3,4,a 0.23% fall (take profit) or a 0.15% rise (stop loss); set from recent volatility,Fresh bear crossover
- 2026-11-20 18:00,USD/JPY,short,short,158.772,0.013,158.7438,158.768,158.8975,49.0,0.1164,3,4,a 0.22% fall (take profit) or a 0.15% rise (stop loss); set from recent volatility,Weak downtrend alignment

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
- Bitcoin 15m 11-20 21:41 price 58900.73 no_trade score below 2
- Bitcoin 15m 11-20 21:42 price 59012.75 no_trade score below 2
- Bitcoin 15m 11-20 21:43 price 59205.34 no_trade score below 2
- Gold USD 11-20 21:41 price 3519.5 no_trade score below 2
- Gold USD 11-20 21:42 price 3519.67 no_trade score below 2
- Gold USD 11-20 21:43 price 3520.5 no_trade score below 2
- USD/JPY 11-20 21:41 price 158.592 no_trade no new entries before weekend
- USD/JPY 11-20 21:42 price 158.592 no_trade no new entries before weekend
- USD/JPY 11-20 21:43 price 158.592 no_trade no new entries before weekend
- GBP/USD 11-20 21:41 price 1.30774 no_trade no new entries before weekend
- GBP/USD 11-20 21:42 price 1.30774 no_trade no new entries before weekend
- GBP/USD 11-20 21:43 price 1.30774 no_trade no new entries before weekend
- EUR/USD 11-20 21:41 price 1.09633 no_trade no new entries before weekend
- EUR/USD 11-20 21:42 price 1.09633 no_trade no new entries before weekend
- EUR/USD 11-20 21:43 price 1.09633 no_trade no new entries before weekend
- EUR/GBP 11-20 21:41 price 0.83837 no_trade no new entries before weekend
- EUR/GBP 11-20 21:42 price 0.83837 no_trade no new entries before weekend
- EUR/GBP 11-20 21:43 price 0.83837 no_trade no new entries before weekend
