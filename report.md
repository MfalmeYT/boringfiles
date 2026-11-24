# Bot report (generated 2026-11-24 04:46 UTC)

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
| Bitcoin 15m | 11-24 04:46 | 1439 | 2 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-24 04:46 | 1378 | 3 | 0 | 31 | 39 | +0.06 | yes |
| GBP/USD | 11-24 04:46 | 1378 | 3 | 0 | 28 | 36 | +0.15 |  |
| EUR/USD | 11-24 04:46 | 1378 | 3 | 0 | 30 | 37 | -0.06 | yes |
| EUR/GBP | 11-24 04:46 | 1378 | 3 | 0 | 28 | 25 | -0.36 | yes |

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
- USD/JPY: short +0.11%
- USD/JPY: short -0.08%
- USD/JPY: long +0.16%
- USD/JPY: short -0.11%
- USD/JPY: short +0.13%
- USD/JPY totals: long 13 trades +0.02%, short 18 trades +0.04%
- GBP/USD: short +0.19%
- GBP/USD: short -0.07%
- GBP/USD: long -0.05%
- GBP/USD: short +0.18%
- GBP/USD: short -0.02%
- GBP/USD totals: long 12 trades +0.01%, short 16 trades +0.15%
- EUR/USD: short -0.11%
- EUR/USD: long -0.07%
- EUR/USD: short -0.04%
- EUR/USD: long -0.12%
- EUR/USD: short +0.13%
- EUR/USD totals: long 17 trades -0.67%, short 13 trades +0.61%
- EUR/GBP: long -0.05%
- EUR/GBP: long +0.09%
- EUR/GBP: short -0.02%
- EUR/GBP: short +0.12%
- EUR/GBP: short -0.00%
- EUR/GBP totals: long 18 trades -0.38%, short 10 trades +0.01%

## Account (latest hourly snapshot)
- 2026-11-24 04:07 UTC AlpacaCrypto: balance 933.52, equity 978.23, free 933.52
- 2026-11-24 04:29 UTC Oanda: balance 773.4835, equity 772.2169, free 55.1289

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-23 23:15,USD/JPY,short,2160,159.096,159.093,-0.0019,2500.0,,2500,filled,conf 2
- 2026-11-24 00:11,USD/JPY,cover,broker,,158.892,,,,,filled,closed by broker stop/TP; P/L 3.1310
- 2026-11-24 00:15,EUR/USD,buy,2200,1.09078,1.09076,-0.0018,5000.0,,5000,filled,conf 4
- 2026-11-24 01:30,GBP/USD,cover,2206,1.30482,1.30473,-0.0069,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-24 01:31,Bitcoin 15m,buy,14cdb219-e99e-4f89-bccb-1d99e8056778,61445.195,61476.8,0.0514,0.000717737,,45,filled,conf 4
- 2026-11-24 02:00,EUR/GBP,buy,2208,0.83672,0.83683,0.0131,10000.0,,10000,filled,conf 4
- 2026-11-24 02:48,Bitcoin 15m,sell,e75d0eea-c278-41cd-a8a5-3e366b58d47a,60246.691,60167.563,-0.1313,0.000715942,0.000715942,,filled,STOP LOSS (-2.0%)
- 2026-11-24 03:11,USD/JPY,short,2218,158.942,158.913,-0.0182,1250.0,,1250,filled,conf 4

## Recent Gemini decisions
- 2026-11-23 23:15,USD/JPY,short,short,159.096,0.015,159.0181,159.044,159.0752,54.7,0.067,2,2,a 0.13% fall (take profit) or a 0.08% rise (stop loss); set from recent volatility,Price jumped sharply abov
- 2026-11-24 00:15,EUR/USD,buy,long,1.09078,0.00015,1.090553,1.090428,1.091529,53.9,0.000469,2,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Short-term momentum is bullish; bu
- 2026-11-24 01:31,Bitcoin 15m,buy,long,61445.19,12.58,61338.693,61334.255,61459.59,52.6,267.157,2,4,+3.00% (take profit) or -2.00% (stop loss),Fresh EMA crossover supports upside despite price slightly
- 2026-11-24 02:00,EUR/GBP,buy,long,0.83672,0.00015,0.836758,0.836701,0.836718,51.4,0.000237,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Slight bullish bias but extremely 
- 2026-11-24 03:11,USD/JPY,short,short,158.942,0.014,158.9112,158.9453,159.0097,48.5,0.0955,3,4,a 0.18% fall (take profit) or a 0.12% rise (stop loss); set from recent volatility,Favorable score and ind

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-24 04:44 price 60428.11 no_trade score below 2
- Bitcoin 15m 11-24 04:45 price 60467.31 no_trade score below 2
- Bitcoin 15m 11-24 04:46 price 60491.85 no_trade score below 2
- USD/JPY 11-24 04:44 price 158.952 holding SHORT -0.0%
- USD/JPY 11-24 04:45 price 158.979 holding SHORT -0.0%
- USD/JPY 11-24 04:46 price 158.979 holding SHORT -0.0%
- GBP/USD 11-24 04:44 price 1.30366 no_trade max 3 open positions reached
- GBP/USD 11-24 04:45 price 1.30376 no_trade max 3 open positions reached
- GBP/USD 11-24 04:46 price 1.30376 no_trade max 3 open positions reached
- EUR/USD 11-24 04:44 price 1.09087 holding 0.0%
- EUR/USD 11-24 04:45 price 1.09091 holding 0.0%
- EUR/USD 11-24 04:46 price 1.09091 holding 0.0%
- EUR/GBP 11-24 04:44 price 0.83679 holding -0.0%
- EUR/GBP 11-24 04:45 price 0.83676 holding -0.0%
- EUR/GBP 11-24 04:46 price 0.83676 holding -0.0%
