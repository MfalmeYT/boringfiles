# Bot report (generated 2026-11-20 15:34 UTC)

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
| Bitcoin 15m | 11-20 15:34 | 1005 | 0 | 0 | 0 | - | +0.00 |  |
| Gold USD | 11-20 15:34 | 1005 | 1 | 0 | 11 | 9 | -6.86 |  |
| USD/JPY | 11-20 15:34 | 995 | 3 | 0 | 26 | 35 | -0.15 |  |
| GBP/USD | 11-20 15:34 | 995 | 3 | 0 | 23 | 35 | -0.08 |  |
| EUR/USD | 11-20 15:34 | 995 | 2 | 0 | 26 | 38 | +0.03 |  |
| EUR/GBP | 11-20 15:34 | 995 | 2 | 0 | 24 | 21 | -0.54 | yes |

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
- USD/JPY: short +0.01%
- USD/JPY: short -0.09%
- USD/JPY: short -0.04%
- USD/JPY: short +0.20%
- USD/JPY: short -0.11%
- USD/JPY totals: long 12 trades -0.14%, short 14 trades -0.01%
- GBP/USD: short +0.18%
- GBP/USD: short +0.21%
- GBP/USD: short -0.08%
- GBP/USD: long -0.06%
- GBP/USD: short -0.17%
- GBP/USD totals: long 11 trades +0.06%, short 12 trades -0.14%
- EUR/USD: short +0.16%
- EUR/USD: short -0.08%
- EUR/USD: long -0.09%
- EUR/USD: long +0.10%
- EUR/USD: short -0.11%
- EUR/USD totals: long 15 trades -0.48%, short 11 trades +0.51%
- EUR/GBP: short -0.03%
- EUR/GBP: long -0.06%
- EUR/GBP: long +0.12%
- EUR/GBP: long -0.08%
- EUR/GBP: long -0.05%
- EUR/GBP totals: long 17 trades -0.46%, short 7 trades -0.08%

## Account (latest hourly snapshot)
- 2026-11-20 15:33 UTC AlpacaCrypto: balance 982.36, equity 982.36, free 982.36
- 2026-11-20 15:33 UTC Oanda: balance 825.5521, equity 824.1095, free 549.4220

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-20 12:37,GBP/USD,short,1698,1.31001,1.31082,0.0618,10000.0,,10000,filled,conf 5
- 2026-11-20 12:37,EUR/USD,cover,broker,,1.09803,,,,,filled,closed by broker stop/TP; P/L -9.9000
- 2026-11-20 13:03,USD/JPY,short,1704,158.758,158.685,-0.046,10000.0,,10000,filled,conf 4
- 2026-11-20 13:03,GBP/USD,cover,broker,,1.31225,,,,,filled,closed by broker stop/TP; P/L -14.3000
- 2026-11-20 13:24,Gold USD,sell,6e776c1c-be92-4ef1-a78d-e07693929e07,3556.265,3536.53,-0.5549,0.01223861,0.01223861,,filled,STOP LOSS (-1.1%)
- 2026-11-20 13:25,EUR/GBP,buy,1710,0.83764,0.83795,0.037,5000.0,,5000,filled,conf 5
- 2026-11-20 15:00,USD/JPY,cover,broker,,158.929,,,,,filled,closed by broker stop/TP; P/L -15.5070
- 2026-11-20 15:10,Bitcoin 15m,sell,4d7660c6-b769-4f98-8d29-a8740a1aa770,61169.9,61034.0,-0.2222,0.000704643,0.000704643,,filled,STOP LOSS (-2.1%)

## Recent Gemini decisions
- 2026-11-20 08:42,Gold USD,buy,long,3579.12,,3562.528,3556.808,3579.32,60.5,33.141,2,4,+1.50% (take profit) or -1.00% (stop loss),Bullish momentum and crossover offset by strong price resistance at EMA
- 2026-11-20 09:40,EUR/USD,short,short,1.09687,0.00016,1.097332,1.097605,1.097658,37.1,0.000492,3,4,a 0.13% fall (take profit) or a 0.09% rise (stop loss); set from recent volatility,Strong downtrend in
- 2026-11-20 12:37,GBP/USD,short,short,1.31001,0.00019,1.310324,1.310485,1.310559,45.8,0.000751,3,5,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Fresh bearish EMA c
- 2026-11-20 13:03,USD/JPY,short,short,158.758,0.014,158.819,158.9015,159.0954,39.9,0.1217,3,4,a 0.23% fall (take profit) or a 0.15% rise (stop loss); set from recent volatility,Full bearish indicator a
- 2026-11-20 13:25,EUR/GBP,buy,long,0.83764,0.00014,0.837241,0.837136,0.837255,56.8,0.000447,3,5,+0.16% (take profit) or -0.11% (stop loss); set from recent volatility,Fresh bullish EMA crossover with p

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
- Bitcoin 15m 11-20 15:32 price 60227.55 no_trade score below 2
- Bitcoin 15m 11-20 15:33 price 60186.92 no_trade score below 2
- Bitcoin 15m 11-20 15:34 price 60105.24 no_trade score below 2
- Gold USD 11-20 15:32 price 3533.87 no_trade score below 2
- Gold USD 11-20 15:33 price 3535.86 no_trade score below 2
- Gold USD 11-20 15:34 price 3541.66 no_trade score below 2
- USD/JPY 11-20 15:32 price 158.758 no_trade re-entry cooldown
- USD/JPY 11-20 15:33 price 158.758 no_trade re-entry cooldown
- USD/JPY 11-20 15:34 price 158.758 no_trade re-entry cooldown
- GBP/USD 11-20 15:32 price 1.31101 no_trade re-entry cooldown
- GBP/USD 11-20 15:33 price 1.31101 no_trade re-entry cooldown
- GBP/USD 11-20 15:34 price 1.31101 no_trade re-entry cooldown
- EUR/USD 11-20 15:32 price 1.09827 no_trade re-entry cooldown
- EUR/USD 11-20 15:33 price 1.09827 no_trade re-entry cooldown
- EUR/USD 11-20 15:34 price 1.09827 no_trade re-entry cooldown
- EUR/GBP 11-20 15:32 price 0.83774 holding -0.0%
- EUR/GBP 11-20 15:33 price 0.83774 holding -0.0%
- EUR/GBP 11-20 15:34 price 0.83774 holding -0.0%
