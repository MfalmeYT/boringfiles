# Bot report (generated 2026-11-24 01:16 UTC)

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
| Bitcoin 15m | 11-24 01:16 | 1439 | 1 | 0 | 3 | 33 | -1.93 |  |
| USD/JPY | 11-24 01:16 | 1378 | 3 | 0 | 31 | 39 | +0.06 |  |
| GBP/USD | 11-24 01:16 | 1378 | 3 | 0 | 27 | 37 | +0.17 | yes |
| EUR/USD | 11-24 01:16 | 1378 | 3 | 0 | 30 | 37 | -0.06 | yes |
| EUR/GBP | 11-24 01:16 | 1378 | 2 | 0 | 28 | 25 | -0.36 |  |

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
- GBP/USD: short -0.17%
- GBP/USD: short +0.19%
- GBP/USD: short -0.07%
- GBP/USD: long -0.05%
- GBP/USD: short +0.18%
- GBP/USD totals: long 12 trades +0.01%, short 15 trades +0.16%
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
- 2026-11-24 00:33 UTC Oanda: balance 778.3835, equity 784.3335, free 23.6035
- 2026-11-24 01:10 UTC AlpacaCrypto: balance 934.67, equity 979.85, free 934.67

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-23 15:46,GBP/USD,short,1834,1.3046,1.30424,-0.0276,10000.0,,10000,filled,conf 2
- 2026-11-23 15:57,Bitcoin 15m,buy,17cd6d10-09f3-4007-a917-ad0e5e933acb,62697.2715,62720.23,0.0366,0.000703403,,45,filled,conf 4
- 2026-11-23 16:53,EUR/GBP,short,1842,0.83679,0.83645,-0.0406,2500.0,,2500,filled,conf 4
- 2026-11-23 17:42,Bitcoin 15m,sell,e9f33994-3504-46ff-9817-92c2c4f9b96e,61436.07,61339.2,-0.1577,0.000701644,0.000701644,,filled,STOP LOSS (-2.0%)
- 2026-11-23 23:00,EUR/GBP,cover,2154,0.83682,0.83704,0.0263,2500.0,2500.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-23 23:15,USD/JPY,short,2160,159.096,159.093,-0.0019,2500.0,,2500,filled,conf 2
- 2026-11-24 00:11,USD/JPY,cover,broker,,158.892,,,,,filled,closed by broker stop/TP; P/L 3.1310
- 2026-11-24 00:15,EUR/USD,buy,2200,1.09078,1.09076,-0.0018,5000.0,,5000,filled,conf 4

## Recent Gemini decisions
- 2026-11-23 15:46,GBP/USD,short,short,1.3046,0.00016,1.30561,1.307374,1.309087,29.4,0.001204,2,2,a 0.28% fall (take profit) or a 0.18% rise (stop loss); set from recent volatility,RSI oversold at 29.4 
- 2026-11-23 15:57,Bitcoin 15m,buy,long,62697.27,15.978,62848.174,62389.042,61845.686,55.4,600.574,3,4,+3.00% (take profit) or -2.00% (stop loss),Bullish EMA alignment and healthy RSI despite recent min
- 2026-11-23 16:53,EUR/GBP,short,short,0.83679,0.00013,0.83681,0.836873,0.837117,48.0,0.000538,3,4,a 0.19% fall (take profit) or a 0.13% rise (stop loss); set from recent volatility,Weak bearish momentu
- 2026-11-23 23:15,USD/JPY,short,short,159.096,0.015,159.0181,159.044,159.0752,54.7,0.067,2,2,a 0.13% fall (take profit) or a 0.08% rise (stop loss); set from recent volatility,Price jumped sharply abov
- 2026-11-24 00:15,EUR/USD,buy,long,1.09078,0.00015,1.090553,1.090428,1.091529,53.9,0.000469,2,4,+0.13% (take profit) or -0.09% (stop loss); set from recent volatility,Short-term momentum is bullish; bu

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-24 01:14 price 61432.36 no_trade score below 2
- Bitcoin 15m 11-24 01:15 price 61464.55 no_trade short-term trend not up
- Bitcoin 15m 11-24 01:16 price 61441.77 no_trade score below 2
- USD/JPY 11-24 01:14 price 158.938 no_trade re-entry cooldown
- USD/JPY 11-24 01:15 price 158.921 no_trade re-entry cooldown
- USD/JPY 11-24 01:16 price 158.921 no_trade re-entry cooldown
- GBP/USD 11-24 01:14 price 1.30401 holding SHORT 0.0%
- GBP/USD 11-24 01:15 price 1.30394 holding SHORT 0.0%
- GBP/USD 11-24 01:16 price 1.30394 holding SHORT 0.0%
- EUR/USD 11-24 01:14 price 1.09107 holding 0.0%
- EUR/USD 11-24 01:15 price 1.09098 holding 0.0%
- EUR/USD 11-24 01:16 price 1.09098 holding 0.0%
- EUR/GBP 11-24 01:14 price 0.8367 no_trade re-entry cooldown
- EUR/GBP 11-24 01:15 price 0.83672 no_trade re-entry cooldown
- EUR/GBP 11-24 01:16 price 0.83672 no_trade re-entry cooldown
