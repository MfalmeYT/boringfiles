# Bot report (generated 2026-11-24 02:34 UTC)

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
| Bitcoin 15m | 11-24 02:34 | 1439 | 2 | 0 | 3 | 33 | -1.93 | yes |
| USD/JPY | 11-24 02:34 | 1378 | 2 | 0 | 31 | 39 | +0.06 |  |
| GBP/USD | 11-24 02:34 | 1378 | 3 | 0 | 28 | 36 | +0.15 |  |
| EUR/USD | 11-24 02:34 | 1378 | 3 | 0 | 30 | 37 | -0.06 | yes |
| EUR/GBP | 11-24 02:34 | 1378 | 3 | 0 | 28 | 25 | -0.36 | yes |

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
- 2026-11-24 02:09 UTC AlpacaCrypto: balance 890.55, equity 978.77, free 890.55
- 2026-11-24 02:31 UTC Oanda: balance 773.4835, equity 775.3985, free 120.4505

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-23 17:42,Bitcoin 15m,sell,e9f33994-3504-46ff-9817-92c2c4f9b96e,61436.07,61339.2,-0.1577,0.000701644,0.000701644,,filled,STOP LOSS (-2.0%)
- 2026-11-23 23:00,EUR/GBP,cover,2154,0.83682,0.83704,0.0263,2500.0,2500.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-23 23:15,USD/JPY,short,2160,159.096,159.093,-0.0019,2500.0,,2500,filled,conf 2
- 2026-11-24 00:11,USD/JPY,cover,broker,,158.892,,,,,filled,closed by broker stop/TP; P/L 3.1310
- 2026-11-24 00:15,EUR/USD,buy,2200,1.09078,1.09076,-0.0018,5000.0,,5000,filled,conf 4
- 2026-11-24 01:30,GBP/USD,cover,2206,1.30482,1.30473,-0.0069,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-24 01:31,Bitcoin 15m,buy,14cdb219-e99e-4f89-bccb-1d99e8056778,61445.195,61476.8,0.0514,0.000717737,,45,filled,conf 4
- 2026-11-24 02:00,EUR/GBP,buy,2208,0.83672,0.83683,0.0131,10000.0,,10000,filled,conf 4

## Recent Gemini decisions
- 2026-11-23 16:53,EUR/GBP,short,short,0.83679,0.00013,0.83681,0.836873,0.837117,48.0,0.000538,3,4,a 0.19% fall (take profit) or a 0.13% rise (stop loss); set from recent volatility,Weak bearish momentu
- 2026-11-23 23:15,USD/JPY,short,short,159.096,0.015,159.0181,159.044,159.0752,54.7,0.067,2,2,a 0.13% fall (take profit) or a 0.08% rise (stop loss); set from recent volatility,Price jumped sharply abov
- 2026-11-24 00:15,EUR/USD,buy,long,1.09078,0.00015,1.090553,1.090428,1.091529,53.9,0.000469,2,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Short-term momentum is bullish; bu
- 2026-11-24 01:31,Bitcoin 15m,buy,long,61445.19,12.58,61338.693,61334.255,61459.59,52.6,267.157,2,4,+3.00% (take profit) or -2.00% (stop loss),Fresh EMA crossover supports upside despite price slightly
- 2026-11-24 02:00,EUR/GBP,buy,long,0.83672,0.00015,0.836758,0.836701,0.836718,51.4,0.000237,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Slight bullish bias but extremely 

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-24 02:32 price 60600.95 holding -1.4%
- Bitcoin 15m 11-24 02:33 price 60612.69 holding -1.4%
- Bitcoin 15m 11-24 02:34 price 60573.73 holding -1.5%
- USD/JPY 11-24 02:32 price 158.908 no_trade re-entry cooldown
- USD/JPY 11-24 02:33 price 158.908 no_trade re-entry cooldown
- USD/JPY 11-24 02:34 price 158.908 no_trade re-entry cooldown
- GBP/USD 11-24 02:32 price 1.30444 no_trade re-entry cooldown
- GBP/USD 11-24 02:33 price 1.30444 no_trade re-entry cooldown
- GBP/USD 11-24 02:34 price 1.30444 no_trade re-entry cooldown
- EUR/USD 11-24 02:32 price 1.0915 holding 0.1%
- EUR/USD 11-24 02:33 price 1.0915 holding 0.1%
- EUR/USD 11-24 02:34 price 1.0915 holding 0.1%
- EUR/GBP 11-24 02:32 price 0.83678 holding -0.0%
- EUR/GBP 11-24 02:33 price 0.83678 holding -0.0%
- EUR/GBP 11-24 02:34 price 0.83678 holding -0.0%
