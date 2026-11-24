# Bot report (generated 2026-11-24 09:05 UTC)

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
| Bitcoin 15m | 11-24 09:05 | 1439 | 2 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-24 09:05 | 1378 | 4 | 0 | 33 | 36 | -0.11 |  |
| GBP/USD | 11-24 09:05 | 1378 | 3 | 0 | 29 | 34 | +0.09 |  |
| EUR/USD | 11-24 09:05 | 1378 | 2 | 0 | 31 | 35 | -0.12 |  |
| EUR/GBP | 11-24 09:05 | 1378 | 4 | 0 | 29 | 24 | -0.39 | yes |

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
- USD/JPY: long +0.16%
- USD/JPY: short -0.11%
- USD/JPY: short +0.13%
- USD/JPY: short -0.07%
- USD/JPY: long -0.09%
- USD/JPY totals: long 14 trades -0.08%, short 19 trades -0.03%
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
- 2026-11-24 08:25 UTC Oanda: balance 754.6301, equity 753.1573, free 116.7473
- 2026-11-24 09:02 UTC AlpacaCrypto: balance 933.52, equity 977.74, free 933.52

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-24 05:15,USD/JPY,cover,2224,159.061,159.079,0.0113,1250.0,1250.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-24 05:15,EUR/GBP,sell,2228,0.83654,0.83644,-0.012,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-24 05:16,GBP/USD,buy,2230,1.30392,1.30396,0.0031,10000.0,,10000,filled,conf 3
- 2026-11-24 07:00,GBP/USD,sell,broker,,1.30311,,,,,filled,closed by broker stop/TP; P/L -8.5000
- 2026-11-24 07:00,EUR/USD,sell,2238,1.09014,1.08998,-0.0147,5000.0,5000.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-24 08:15,USD/JPY,buy,2240,159.371,159.375,0.0025,10000.0,,10000,filled,conf 4
- 2026-11-24 08:15,EUR/GBP,short,2248,0.83665,0.8366,-0.006,2500.0,,2500,filled,conf 2
- 2026-11-24 08:41,USD/JPY,sell,broker,,159.22,,,,,filled,closed by broker stop/TP; P/L -9.8319

## Recent Gemini decisions
- 2026-11-24 02:00,EUR/GBP,buy,long,0.83672,0.00015,0.836758,0.836701,0.836718,51.4,0.000237,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Slight bullish bias but extremely 
- 2026-11-24 03:11,USD/JPY,short,short,158.942,0.014,158.9112,158.9453,159.0097,48.5,0.0955,3,4,a 0.18% fall (take profit) or a 0.12% rise (stop loss); set from recent volatility,Favorable score and ind
- 2026-11-24 05:16,GBP/USD,buy,long,1.30392,0.00021,1.303888,1.303867,1.304251,51.0,0.000427,2,3,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Flat EMAs and mixed trend signals 
- 2026-11-24 08:15,USD/JPY,buy,long,159.371,0.014,159.3016,159.1943,159.11,67.0,0.0783,3,4,+0.15% (take profit) or -0.10% (stop loss); set from recent volatility,Strong uptrend alignment; but high RSI n
- 2026-11-24 08:15,EUR/GBP,short,short,0.83665,0.00013,0.836468,0.836532,0.83663,53.8,0.000223,2,2,a 0.08% fall (take profit) or a 0.05% rise (stop loss); set from recent volatility,Price rose above all

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-24 09:03 price 59918.75 no_trade score below 2
- Bitcoin 15m 11-24 09:04 price 59912.09 no_trade score below 2
- Bitcoin 15m 11-24 09:05 price 59937.89 no_trade score below 2
- USD/JPY 11-24 09:03 price 159.354 no_trade re-entry cooldown
- USD/JPY 11-24 09:04 price 159.354 no_trade re-entry cooldown
- USD/JPY 11-24 09:05 price 159.354 no_trade re-entry cooldown
- GBP/USD 11-24 09:03 price 1.30532 no_trade re-entry cooldown
- GBP/USD 11-24 09:04 price 1.30532 no_trade re-entry cooldown
- GBP/USD 11-24 09:05 price 1.30532 no_trade re-entry cooldown
- EUR/USD 11-24 09:03 price 1.09168 no_trade re-entry cooldown
- EUR/USD 11-24 09:04 price 1.09168 no_trade re-entry cooldown
- EUR/USD 11-24 09:05 price 1.09168 no_trade re-entry cooldown
- EUR/GBP 11-24 09:03 price 0.83633 holding SHORT 0.0%
- EUR/GBP 11-24 09:04 price 0.83633 holding SHORT 0.0%
- EUR/GBP 11-24 09:05 price 0.83633 holding SHORT 0.0%
