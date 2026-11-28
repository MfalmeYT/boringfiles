# Bot report (generated 2026-11-28 03:03 UTC)

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
| Bitcoin 15m | 11-28 03:03 | 1440 | 1 | 0 | 6 | 33 | -4.29 |  |
| USD/JPY | 11-27 21:58 | 1135 | 3 | 0 | 48 | 33 | -0.68 |  |
| GBP/USD | 11-27 21:58 | 1135 | 2 | 0 | 42 | 31 | -0.13 |  |
| EUR/USD | 11-27 21:58 | 1135 | 3 | 0 | 44 | 41 | +0.39 |  |
| EUR/GBP | 11-27 21:58 | 1135 | 2 | 0 | 43 | 26 | -0.78 |  |

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
- Bitcoin 15m: long +3.03%
- Bitcoin 15m: long -2.51%
- Bitcoin 15m: long -2.45%
- Bitcoin 15m: long +2.73%
- Bitcoin 15m: long -2.64%
- USD/JPY: long -0.06%
- USD/JPY: short -0.05%
- USD/JPY: long +0.11%
- USD/JPY: long -0.06%
- USD/JPY: long +0.01%
- USD/JPY totals: long 24 trades -0.49%, short 24 trades -0.20%
- GBP/USD: long -0.10%
- GBP/USD: short -0.03%
- GBP/USD: long -0.02%
- GBP/USD: long -0.05%
- GBP/USD: short +0.12%
- GBP/USD totals: long 21 trades -0.32%, short 21 trades +0.19%
- EUR/USD: long +0.14%
- EUR/USD: short -0.07%
- EUR/USD: long +0.13%
- EUR/USD: short +0.20%
- EUR/USD: short +0.05%
- EUR/USD totals: long 26 trades -0.38%, short 18 trades +0.77%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP: short -0.04%
- EUR/GBP: short +0.07%
- EUR/GBP: short +0.01%
- EUR/GBP totals: long 25 trades -0.48%, short 18 trades -0.30%

## Account (latest hourly snapshot)
- 2026-11-28 02:31 UTC AlpacaCrypto: balance 933.51, equity 978.58, free 933.51
- 2026-11-28 02:54 UTC Oanda: balance 684.4854, equity 684.4854, free 684.4854

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-27 14:35,GBP/USD,short,2745,1.31106,1.31159,0.0404,5000.0,,5000,filled,conf 4
- 2026-11-27 14:40,Bitcoin 15m,sell,a278da25-19c0-44bb-9810-41edd5899e34,60081.511,60188.81,0.1786,0.000716567,0.000716567,,filled,STOP LOSS (-2.2%)
- 2026-11-27 16:30,EUR/USD,short,2753,1.09387,1.09363,-0.0219,2500.0,,2500,filled,conf 4
- 2026-11-27 18:37,USD/JPY,buy,2761,159.545,159.541,-0.0025,5000.0,,5000,filled,conf 4
- 2026-11-27 18:37,GBP/USD,cover,broker,,1.30943,,,,,filled,closed by broker stop/TP; P/L 10.8000
- 2026-11-27 21:30,USD/JPY,sell,2767,159.565,159.555,-0.0063,5000.0,5000.0,,filled,WEEKEND FLATTEN (0.0%)
- 2026-11-27 21:30,EUR/USD,cover,2771,1.09336,1.09352,0.0146,2500.0,2500.0,,filled,WEEKEND FLATTEN (0.0%)
- 2026-11-27 21:30,EUR/GBP,cover,2775,0.83504,0.83512,0.0096,5000.0,5000.0,,filled,WEEKEND FLATTEN (-0.0%)

## Recent Gemini decisions
- 2026-11-27 11:06,EUR/GBP,short,short,0.83516,0.00013,0.835204,0.835614,0.836138,34.6,0.000287,3,4,a 0.10% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Favorable alignment
- 2026-11-27 13:30,USD/JPY,buy,long,159.552,0.015,159.4925,159.4608,159.3989,64.5,0.0549,3,4,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Strong trend and EMAs aligned; but RSI
- 2026-11-27 14:35,GBP/USD,short,short,1.31106,0.0002,1.311774,1.312157,1.312092,39.0,0.000736,3,4,a 0.17% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Downtrend intact wit
- 2026-11-27 16:30,EUR/USD,short,short,1.09387,0.00015,1.094288,1.094946,1.095817,33.1,0.000657,3,4,a 0.18% fall (take profit) or a 0.12% rise (stop loss); set from recent volatility,Strong downtrend in
- 2026-11-27 18:37,USD/JPY,buy,long,159.545,0.013,159.5221,159.513,159.4677,57.7,0.0484,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Bullish alignment and positive momentum

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-28 03:01 price 59913.45 no_trade 1Hour trend not up
- Bitcoin 15m 11-28 03:02 price 59908.88 no_trade 1Hour trend not up
- Bitcoin 15m 11-28 03:03 price 59907.51 no_trade 1Hour trend not up
- USD/JPY 11-27 21:56 price 159.577 no_trade no new entries before weekend
- USD/JPY 11-27 21:57 price 159.577 no_trade no new entries before weekend
- USD/JPY 11-27 21:58 price 159.577 no_trade no new entries before weekend
- GBP/USD 11-27 21:56 price 1.30946 no_trade no new entries before weekend
- GBP/USD 11-27 21:57 price 1.30946 no_trade no new entries before weekend
- GBP/USD 11-27 21:58 price 1.30946 no_trade no new entries before weekend
- EUR/USD 11-27 21:56 price 1.09322 no_trade no new entries before weekend
- EUR/USD 11-27 21:57 price 1.09322 no_trade no new entries before weekend
- EUR/USD 11-27 21:58 price 1.09322 no_trade no new entries before weekend
- EUR/GBP 11-27 21:56 price 0.83486 no_trade no new entries before weekend
- EUR/GBP 11-27 21:57 price 0.83486 no_trade no new entries before weekend
- EUR/GBP 11-27 21:58 price 0.83486 no_trade no new entries before weekend
