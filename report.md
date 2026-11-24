# Bot report (generated 2026-11-24 07:24 UTC)

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
| Bitcoin 15m | 11-24 07:24 | 1439 | 2 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-24 07:24 | 1378 | 3 | 0 | 32 | 38 | -0.02 |  |
| GBP/USD | 11-24 07:24 | 1378 | 3 | 0 | 29 | 34 | +0.09 |  |
| EUR/USD | 11-24 07:24 | 1378 | 3 | 0 | 31 | 35 | -0.12 |  |
| EUR/GBP | 11-24 07:24 | 1378 | 3 | 0 | 29 | 24 | -0.39 |  |

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
- GBP/USD: short -0.07%
- GBP/USD: long -0.05%
- GBP/USD: short +0.18%
- GBP/USD: short -0.02%
- GBP/USD: long -0.06%
- GBP/USD totals: long 13 trades -0.06%, short 16 trades +0.15%
- EUR/USD: long -0.07%
- EUR/USD: short -0.04%
- EUR/USD: long -0.12%
- EUR/USD: short +0.13%
- EUR/USD: long -0.06%
- EUR/USD totals: long 18 trades -0.73%, short 13 trades +0.61%
- EUR/GBP: long +0.09%
- EUR/GBP: short -0.02%
- EUR/GBP: short +0.12%
- EUR/GBP: short -0.00%
- EUR/GBP: long -0.02%
- EUR/GBP totals: long 19 trades -0.40%, short 10 trades +0.01%

## Account (latest hourly snapshot)
- 2026-11-24 06:27 UTC Oanda: balance 767.0301, equity 772.2801, free 10.8861
- 2026-11-24 07:04 UTC AlpacaCrypto: balance 933.52, equity 978.25, free 933.52

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-24 02:00,EUR/GBP,buy,2208,0.83672,0.83683,0.0131,10000.0,,10000,filled,conf 4
- 2026-11-24 02:48,Bitcoin 15m,sell,e75d0eea-c278-41cd-a8a5-3e366b58d47a,60246.691,60167.563,-0.1313,0.000715942,0.000715942,,filled,STOP LOSS (-2.0%)
- 2026-11-24 03:11,USD/JPY,short,2218,158.942,158.913,-0.0182,1250.0,,1250,filled,conf 4
- 2026-11-24 05:15,USD/JPY,cover,2224,159.061,159.079,0.0113,1250.0,1250.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-24 05:15,EUR/GBP,sell,2228,0.83654,0.83644,-0.012,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-24 05:16,GBP/USD,buy,2230,1.30392,1.30396,0.0031,10000.0,,10000,filled,conf 3
- 2026-11-24 07:00,GBP/USD,sell,broker,,1.30311,,,,,filled,closed by broker stop/TP; P/L -8.5000
- 2026-11-24 07:00,EUR/USD,sell,2238,1.09014,1.08998,-0.0147,5000.0,5000.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)

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
- Bitcoin 15m 11-24 07:22 price 60302.57 no_trade score below 2
- Bitcoin 15m 11-24 07:23 price 60345.51 no_trade score below 2
- Bitcoin 15m 11-24 07:24 price 60364.96 no_trade score below 2
- USD/JPY 11-24 07:22 price 159.278 no_trade re-entry cooldown
- USD/JPY 11-24 07:23 price 159.278 no_trade re-entry cooldown
- USD/JPY 11-24 07:24 price 159.278 no_trade re-entry cooldown
- GBP/USD 11-24 07:22 price 1.30398 no_trade re-entry cooldown
- GBP/USD 11-24 07:23 price 1.30398 no_trade re-entry cooldown
- GBP/USD 11-24 07:24 price 1.30398 no_trade re-entry cooldown
- EUR/USD 11-24 07:22 price 1.09042 no_trade re-entry cooldown
- EUR/USD 11-24 07:23 price 1.09042 no_trade re-entry cooldown
- EUR/USD 11-24 07:24 price 1.09042 no_trade re-entry cooldown
- EUR/GBP 11-24 07:22 price 0.83624 no_trade re-entry cooldown
- EUR/GBP 11-24 07:23 price 0.83624 no_trade re-entry cooldown
- EUR/GBP 11-24 07:24 price 0.83624 no_trade re-entry cooldown
