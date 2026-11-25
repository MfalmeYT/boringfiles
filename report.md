# Bot report (generated 2026-11-25 23:45 UTC)

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
| Bitcoin 15m | 11-25 23:45 | 1421 | 1 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-25 23:45 | 1360 | 6 | 0 | 41 | 32 | -0.56 | yes |
| GBP/USD | 11-25 23:45 | 1360 | 3 | 0 | 34 | 35 | +0.10 |  |
| EUR/USD | 11-25 23:45 | 1360 | 4 | 0 | 37 | 38 | +0.08 | yes |
| EUR/GBP | 11-25 23:45 | 1360 | 5 | 0 | 37 | 24 | -0.67 |  |

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
- USD/JPY: short -0.14%
- USD/JPY: long -0.18%
- USD/JPY: long -0.04%
- USD/JPY: short +0.23%
- USD/JPY: short -0.06%
- USD/JPY totals: long 18 trades -0.41%, short 23 trades -0.15%
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD: short +0.11%
- GBP/USD: short -0.12%
- GBP/USD: long -0.06%
- GBP/USD totals: long 16 trades -0.04%, short 18 trades +0.14%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD: short +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD totals: long 22 trades -0.53%, short 15 trades +0.60%
- EUR/GBP: short -0.02%
- EUR/GBP: long +0.08%
- EUR/GBP: long +0.13%
- EUR/GBP: long -0.11%
- EUR/GBP: short -0.11%
- EUR/GBP totals: long 23 trades -0.37%, short 14 trades -0.30%

## Account (latest hourly snapshot)
- 2026-11-25 22:47 UTC Oanda: balance 710.0685, equity 707.0685, free 487.5045
- 2026-11-25 23:23 UTC AlpacaCrypto: balance 889.38, equity 977.83, free 889.38

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 19:42,GBP/USD,buy,2514,1.31284,1.31293,0.0069,10000.0,,10000,filled,conf 4
- 2026-11-25 19:43,USD/JPY,short,2524,159.134,159.15,0.0101,1250.0,,1250,filled,conf 2
- 2026-11-25 20:45,USD/JPY,cover,broker,,159.229,,,,,filled,closed by broker stop/TP; P/L -0.6264
- 2026-11-25 20:45,GBP/USD,sell,broker,,1.31201,,,,,filled,closed by broker stop/TP; P/L -9.2000
- 2026-11-25 20:45,EUR/USD,buy,2537,1.09766,1.09774,0.0073,10000.0,,10000,filled,conf 4
- 2026-11-25 21:26,EUR/GBP,short,2543,0.83666,0.83668,0.0024,5000.0,,5000,filled,conf 4
- 2026-11-25 23:00,EUR/GBP,cover,broker,,0.83757,,,,,filled,closed by broker stop/TP; P/L -5.8951
- 2026-11-25 23:45,USD/JPY,buy,2552,159.217,159.229,0.0075,5000.0,,5000,filled,conf 4

## Recent Gemini decisions
- 2026-11-25 19:42,GBP/USD,buy,long,1.31284,0.00017,1.311905,1.310255,1.309081,73.3,0.000926,2,4,+0.21% (take profit) or -0.14% (stop loss); set from recent volatility,Strong uptrend across EMAs; but ov
- 2026-11-25 19:43,USD/JPY,short,short,159.134,0.018,159.0581,159.0731,159.1566,52.6,0.1113,3,2,a 0.21% fall (take profit) or a 0.14% rise (stop loss); set from recent volatility,Divergence between stro
- 2026-11-25 20:45,EUR/USD,buy,long,1.09766,0.00016,1.098011,1.097437,1.096344,57.0,0.000634,3,4,+0.17% (take profit) or -0.12% (stop loss); set from recent volatility,Downtrend across recent closes con
- 2026-11-25 21:26,EUR/GBP,short,short,0.83666,0.00013,0.836737,0.837003,0.837088,39.5,0.000301,3,4,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Downtrend intact wi
- 2026-11-25 23:45,USD/JPY,buy,long,159.217,0.018,159.17,159.158,159.1703,58.1,0.0684,3,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Price bouncing off lows with bullish EMAs

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 23:43 price 60295.43 holding 1.0%
- Bitcoin 15m 11-25 23:44 price 60287.1 holding 1.0%
- Bitcoin 15m 11-25 23:45 price 60307.52 holding 1.0%
- USD/JPY 11-25 23:43 price 159.144 no_trade re-entry cooldown
- USD/JPY 11-25 23:44 price 159.144 no_trade re-entry cooldown
- USD/JPY 11-25 23:45 price 159.217 buy conf 4: Price bouncing off lows with bullish EMAs; but lacks strong momentum. | 5000 units
- GBP/USD 11-25 23:43 price 1.31164 no_trade re-entry cooldown
- GBP/USD 11-25 23:44 price 1.31164 no_trade re-entry cooldown
- GBP/USD 11-25 23:45 price 1.31122 no_trade max 3 open positions reached
- EUR/USD 11-25 23:43 price 1.09762 holding -0.0%
- EUR/USD 11-25 23:44 price 1.09762 holding -0.0%
- EUR/USD 11-25 23:45 price 1.09708 holding -0.1%
- EUR/GBP 11-25 23:43 price 0.83682 no_trade re-entry cooldown
- EUR/GBP 11-25 23:44 price 0.83682 no_trade re-entry cooldown
- EUR/GBP 11-25 23:45 price 0.83667 no_trade re-entry cooldown
