# Bot report (generated 2026-11-26 02:40 UTC)

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
| Bitcoin 15m | 11-26 02:40 | 1421 | 1 | 0 | 4 | 25 | -4.38 | yes |
| USD/JPY | 11-26 02:40 | 1360 | 6 | 0 | 42 | 31 | -0.64 |  |
| GBP/USD | 11-26 02:40 | 1360 | 4 | 0 | 34 | 35 | +0.10 | yes |
| EUR/USD | 11-26 02:40 | 1360 | 4 | 0 | 38 | 37 | -0.00 |  |
| EUR/GBP | 11-26 02:40 | 1360 | 5 | 0 | 37 | 24 | -0.67 | yes |

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
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD: short +0.11%
- GBP/USD: short -0.12%
- GBP/USD: long -0.06%
- GBP/USD totals: long 16 trades -0.04%, short 18 trades +0.14%
- EUR/USD: long -0.14%
- EUR/USD: short +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD: long -0.08%
- EUR/USD totals: long 23 trades -0.60%, short 15 trades +0.60%
- EUR/GBP: short -0.02%
- EUR/GBP: long +0.08%
- EUR/GBP: long +0.13%
- EUR/GBP: long -0.11%
- EUR/GBP: short -0.11%
- EUR/GBP totals: long 23 trades -0.37%, short 14 trades -0.30%

## Account (latest hourly snapshot)
- 2026-11-26 01:44 UTC Oanda: balance 695.7882, equity 691.9382, free 364.2257
- 2026-11-26 02:20 UTC AlpacaCrypto: balance 889.38, equity 978.41, free 889.38

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 20:45,EUR/USD,buy,2537,1.09766,1.09774,0.0073,10000.0,,10000,filled,conf 4
- 2026-11-25 21:26,EUR/GBP,short,2543,0.83666,0.83668,0.0024,5000.0,,5000,filled,conf 4
- 2026-11-25 23:00,EUR/GBP,cover,broker,,0.83757,,,,,filled,closed by broker stop/TP; P/L -5.8951
- 2026-11-25 23:45,USD/JPY,buy,2552,159.217,159.229,0.0075,5000.0,,5000,filled,conf 4
- 2026-11-26 00:20,USD/JPY,sell,broker,,159.091,,,,,filled,closed by broker stop/TP; P/L -4.3803
- 2026-11-26 00:20,GBP/USD,buy,2560,1.31124,1.31144,0.0153,5000.0,,5000,filled,conf 3
- 2026-11-26 01:30,EUR/USD,sell,2566,1.09679,1.09675,-0.0036,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-26 02:02,EUR/GBP,short,2570,0.83654,0.83648,-0.0072,5000.0,,5000,filled,conf 4

## Recent Gemini decisions
- 2026-11-25 20:45,EUR/USD,buy,long,1.09766,0.00016,1.098011,1.097437,1.096344,57.0,0.000634,3,4,+0.17% (take profit) or -0.12% (stop loss); set from recent volatility,Downtrend across recent closes con
- 2026-11-25 21:26,EUR/GBP,short,short,0.83666,0.00013,0.836737,0.837003,0.837088,39.5,0.000301,3,4,a 0.11% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Downtrend intact wi
- 2026-11-25 23:45,USD/JPY,buy,long,159.217,0.018,159.17,159.158,159.1703,58.1,0.0684,3,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Price bouncing off lows with bullish EMAs
- 2026-11-26 00:20,GBP/USD,buy,long,1.31124,0.00019,1.311426,1.311355,1.310449,51.3,0.000486,3,3,+0.11% (take profit) or -0.07% (stop loss); set from recent volatility,Weak momentum and flat EMAs sugges
- 2026-11-26 02:02,EUR/GBP,short,short,0.83654,0.00012,0.836618,0.836724,0.836875,39.1,0.000195,3,4,a 0.07% fall (take profit) or a 0.05% rise (stop loss); set from recent volatility,Downtrend intact wi

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-26 02:38 price 60787.23 holding 1.9%
- Bitcoin 15m 11-26 02:39 price 60789.64 holding 1.9%
- Bitcoin 15m 11-26 02:40 price 60816.83 holding 1.9%
- USD/JPY 11-26 02:38 price 159.172 no_trade no long or short setup
- USD/JPY 11-26 02:39 price 159.172 no_trade no long or short setup
- USD/JPY 11-26 02:40 price 159.172 no_trade no long or short setup
- GBP/USD 11-26 02:38 price 1.3115 holding 0.0%
- GBP/USD 11-26 02:39 price 1.3115 holding 0.0%
- GBP/USD 11-26 02:40 price 1.3115 holding 0.0%
- EUR/USD 11-26 02:38 price 1.09686 no_trade re-entry cooldown
- EUR/USD 11-26 02:39 price 1.09686 no_trade re-entry cooldown
- EUR/USD 11-26 02:40 price 1.09686 no_trade re-entry cooldown
- EUR/GBP 11-26 02:38 price 0.83634 holding SHORT 0.0%
- EUR/GBP 11-26 02:39 price 0.83634 holding SHORT 0.0%
- EUR/GBP 11-26 02:40 price 0.83634 holding SHORT 0.0%
