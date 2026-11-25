# Bot report (generated 2026-11-25 20:14 UTC)

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
| Bitcoin 15m | 11-25 20:14 | 1421 | 1 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-25 20:14 | 1360 | 6 | 0 | 40 | 32 | -0.50 | yes |
| GBP/USD | 11-25 20:14 | 1360 | 3 | 0 | 33 | 36 | +0.16 | yes |
| EUR/USD | 11-25 20:14 | 1360 | 3 | 0 | 37 | 38 | +0.08 |  |
| EUR/GBP | 11-25 20:14 | 1360 | 4 | 0 | 36 | 25 | -0.56 |  |

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
- USD/JPY: long -0.06%
- USD/JPY: short -0.14%
- USD/JPY: long -0.18%
- USD/JPY: long -0.04%
- USD/JPY: short +0.23%
- USD/JPY totals: long 18 trades -0.41%, short 22 trades -0.09%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD: short +0.11%
- GBP/USD: short -0.12%
- GBP/USD totals: long 15 trades +0.02%, short 18 trades +0.14%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD: short +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD totals: long 22 trades -0.53%, short 15 trades +0.60%
- EUR/GBP: short -0.14%
- EUR/GBP: short -0.02%
- EUR/GBP: long +0.08%
- EUR/GBP: long +0.13%
- EUR/GBP: long -0.11%
- EUR/GBP totals: long 23 trades -0.37%, short 13 trades -0.20%

## Account (latest hourly snapshot)
- 2026-11-25 19:27 UTC AlpacaCrypto: balance 889.38, equity 977.51, free 889.38
- 2026-11-25 19:50 UTC Oanda: balance 727.8164, equity 722.7965, free 3.9815

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 16:42,GBP/USD,cover,broker,,1.30885,,,,,filled,closed by broker stop/TP; P/L -8.5000
- 2026-11-25 16:43,USD/JPY,cover,broker,,158.83,,,,,filled,closed by broker stop/TP; P/L 11.1889
- 2026-11-25 16:43,EUR/USD,sell,broker,,1.09652,,,,,filled,closed by broker stop/TP; P/L 12.5500
- 2026-11-25 17:35,EUR/GBP,buy,2508,0.83762,0.83775,0.0155,10000.0,,10000,filled,conf 3
- 2026-11-25 17:41,Bitcoin 15m,buy,1c8df5c3-ac97-4a5e-b0f3-2cd28821391c,59628.35,59681.97,0.0899,0.000739579,,45,filled,conf 5
- 2026-11-25 18:26,EUR/GBP,sell,broker,,0.83673,,,,,filled,closed by broker stop/TP; P/L -13.5234
- 2026-11-25 19:42,GBP/USD,buy,2514,1.31284,1.31293,0.0069,10000.0,,10000,filled,conf 4
- 2026-11-25 19:43,USD/JPY,short,2524,159.134,159.15,0.0101,1250.0,,1250,filled,conf 2

## Recent Gemini decisions
- 2026-11-25 15:22,EUR/USD,buy,long,1.09397,0.00015,1.094337,1.094329,1.094554,46.1,0.000844,2,3,+0.23% (take profit) or -0.15% (stop loss); set from recent volatility,Price below EMA50 with flat indica
- 2026-11-25 17:35,EUR/GBP,buy,long,0.83762,0.00015,0.837766,0.837668,0.837287,50.5,0.000497,3,3,+0.18% (take profit) or -0.12% (stop loss); set from recent volatility,Flat price action with fast EMA be
- 2026-11-25 17:41,Bitcoin 15m,buy,long,59628.35,10.965,58802.47,58590.301,58705.413,64.0,534.842,3,5,+3.00% (take profit) or -2.00% (stop loss),Bullish trend confirmed by EMA crossover; strong RSI; and
- 2026-11-25 19:42,GBP/USD,buy,long,1.31284,0.00017,1.311905,1.310255,1.309081,73.3,0.000926,2,4,+0.21% (take profit) or -0.14% (stop loss); set from recent volatility,Strong uptrend across EMAs; but ov
- 2026-11-25 19:43,USD/JPY,short,short,159.134,0.018,159.0581,159.0731,159.1566,52.6,0.1113,3,2,a 0.21% fall (take profit) or a 0.14% rise (stop loss); set from recent volatility,Divergence between stro

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 20:12 price 59875.52 holding 0.3%
- Bitcoin 15m 11-25 20:13 price 59966.41 holding 0.5%
- Bitcoin 15m 11-25 20:14 price 60002.87 holding 0.5%
- USD/JPY 11-25 20:12 price 159.201 holding SHORT -0.0%
- USD/JPY 11-25 20:13 price 159.201 holding SHORT -0.0%
- USD/JPY 11-25 20:14 price 159.201 holding SHORT -0.0%
- GBP/USD 11-25 20:12 price 1.3122 holding -0.1%
- GBP/USD 11-25 20:13 price 1.3122 holding -0.1%
- GBP/USD 11-25 20:14 price 1.3122 holding -0.1%
- EUR/USD 11-25 20:12 price 1.09794 no_trade max 3 open positions reached
- EUR/USD 11-25 20:13 price 1.09794 no_trade max 3 open positions reached
- EUR/USD 11-25 20:14 price 1.09794 no_trade max 3 open positions reached
- EUR/GBP 11-25 20:12 price 0.83672 no_trade re-entry cooldown
- EUR/GBP 11-25 20:13 price 0.83672 no_trade re-entry cooldown
- EUR/GBP 11-25 20:14 price 0.83672 no_trade re-entry cooldown
