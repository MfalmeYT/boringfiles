# Bot report (generated 2026-11-24 05:37 UTC)

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
| Bitcoin 15m | 11-24 05:37 | 1439 | 2 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-24 05:37 | 1378 | 3 | 0 | 32 | 38 | -0.02 |  |
| GBP/USD | 11-24 05:37 | 1378 | 4 | 0 | 28 | 36 | +0.15 | yes |
| EUR/USD | 11-24 05:37 | 1378 | 3 | 0 | 30 | 37 | -0.06 | yes |
| EUR/GBP | 11-24 05:37 | 1378 | 3 | 0 | 29 | 24 | -0.39 |  |

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
- USD/JPY: short -0.08%
- USD/JPY: long +0.16%
- USD/JPY: short -0.11%
- USD/JPY: short +0.13%
- USD/JPY: short -0.07%
- USD/JPY totals: long 13 trades +0.02%, short 19 trades -0.03%
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
- EUR/GBP: long +0.09%
- EUR/GBP: short -0.02%
- EUR/GBP: short +0.12%
- EUR/GBP: short -0.00%
- EUR/GBP: long -0.02%
- EUR/GBP totals: long 19 trades -0.40%, short 10 trades +0.01%

## Account (latest hourly snapshot)
- 2026-11-24 05:06 UTC AlpacaCrypto: balance 933.52, equity 978.22, free 933.52
- 2026-11-24 05:28 UTC Oanda: balance 767.0301, equity 771.7301, free 10.3451

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-24 01:30,GBP/USD,cover,2206,1.30482,1.30473,-0.0069,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-24 01:31,Bitcoin 15m,buy,14cdb219-e99e-4f89-bccb-1d99e8056778,61445.195,61476.8,0.0514,0.000717737,,45,filled,conf 4
- 2026-11-24 02:00,EUR/GBP,buy,2208,0.83672,0.83683,0.0131,10000.0,,10000,filled,conf 4
- 2026-11-24 02:48,Bitcoin 15m,sell,e75d0eea-c278-41cd-a8a5-3e366b58d47a,60246.691,60167.563,-0.1313,0.000715942,0.000715942,,filled,STOP LOSS (-2.0%)
- 2026-11-24 03:11,USD/JPY,short,2218,158.942,158.913,-0.0182,1250.0,,1250,filled,conf 4
- 2026-11-24 05:15,USD/JPY,cover,2224,159.061,159.079,0.0113,1250.0,1250.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-24 05:15,EUR/GBP,sell,2228,0.83654,0.83644,-0.012,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-24 05:16,GBP/USD,buy,2230,1.30392,1.30396,0.0031,10000.0,,10000,filled,conf 3

## Recent Gemini decisions
- 2026-11-24 00:15,EUR/USD,buy,long,1.09078,0.00015,1.090553,1.090428,1.091529,53.9,0.000469,2,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Short-term momentum is bullish; bu
- 2026-11-24 01:31,Bitcoin 15m,buy,long,61445.19,12.58,61338.693,61334.255,61459.59,52.6,267.157,2,4,+3.00% (take profit) or -2.00% (stop loss),Fresh EMA crossover supports upside despite price slightly
- 2026-11-24 02:00,EUR/GBP,buy,long,0.83672,0.00015,0.836758,0.836701,0.836718,51.4,0.000237,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Slight bullish bias but extremely 
- 2026-11-24 03:11,USD/JPY,short,short,158.942,0.014,158.9112,158.9453,159.0097,48.5,0.0955,3,4,a 0.18% fall (take profit) or a 0.12% rise (stop loss); set from recent volatility,Favorable score and ind
- 2026-11-24 05:16,GBP/USD,buy,long,1.30392,0.00021,1.303888,1.303867,1.304251,51.0,0.000427,2,3,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Flat EMAs and mixed trend signals 

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-24 05:35 price 60615.56 no_trade score below 2
- Bitcoin 15m 11-24 05:36 price 60603.49 no_trade score below 2
- Bitcoin 15m 11-24 05:37 price 60644.16 no_trade score below 2
- USD/JPY 11-24 05:35 price 159.094 no_trade re-entry cooldown
- USD/JPY 11-24 05:36 price 159.094 no_trade re-entry cooldown
- USD/JPY 11-24 05:37 price 159.094 no_trade re-entry cooldown
- GBP/USD 11-24 05:35 price 1.30444 holding 0.0%
- GBP/USD 11-24 05:36 price 1.30444 holding 0.0%
- GBP/USD 11-24 05:37 price 1.30444 holding 0.0%
- EUR/USD 11-24 05:35 price 1.091 holding 0.0%
- EUR/USD 11-24 05:36 price 1.091 holding 0.0%
- EUR/USD 11-24 05:37 price 1.091 holding 0.0%
- EUR/GBP 11-24 05:35 price 0.83638 no_trade re-entry cooldown
- EUR/GBP 11-24 05:36 price 0.83638 no_trade re-entry cooldown
- EUR/GBP 11-24 05:37 price 0.83638 no_trade re-entry cooldown
