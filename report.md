# Bot report (generated 2026-11-24 15:50 UTC)

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
| Bitcoin 15m | 11-24 15:50 | 1440 | 2 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-24 15:50 | 1379 | 4 | 0 | 34 | 35 | -0.15 |  |
| GBP/USD | 11-24 15:50 | 1379 | 3 | 0 | 30 | 37 | +0.26 | yes |
| EUR/USD | 11-24 15:50 | 1379 | 3 | 0 | 33 | 36 | -0.02 |  |
| EUR/GBP | 11-24 15:50 | 1379 | 4 | 0 | 31 | 23 | -0.51 |  |

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
- USD/JPY: short -0.11%
- USD/JPY: short +0.13%
- USD/JPY: short -0.07%
- USD/JPY: long -0.09%
- USD/JPY: long -0.04%
- USD/JPY totals: long 15 trades -0.12%, short 19 trades -0.03%
- GBP/USD: long -0.05%
- GBP/USD: short +0.18%
- GBP/USD: short -0.02%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD totals: long 14 trades +0.11%, short 16 trades +0.15%
- EUR/USD: long -0.12%
- EUR/USD: short +0.13%
- EUR/USD: long -0.06%
- EUR/USD: long +0.15%
- EUR/USD: long -0.04%
- EUR/USD totals: long 20 trades -0.62%, short 13 trades +0.61%
- EUR/GBP: short +0.12%
- EUR/GBP: short -0.00%
- EUR/GBP: long -0.02%
- EUR/GBP: short -0.05%
- EUR/GBP: long -0.08%
- EUR/GBP totals: long 20 trades -0.48%, short 11 trades -0.04%

## Account (latest hourly snapshot)
- 2026-11-24 14:56 UTC AlpacaCrypto: balance 933.52, equity 977.78, free 933.52
- 2026-11-24 15:18 UTC Oanda: balance 749.9139, equity 744.2139, free 88.9339

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-24 11:42,EUR/USD,sell,broker,,1.09509,,,,,filled,closed by broker stop/TP; P/L 19.3000
- 2026-11-24 11:57,GBP/USD,sell,broker,,1.30892,,,,,filled,closed by broker stop/TP; P/L 11.4000
- 2026-11-24 13:11,USD/JPY,sell,2280,159.159,159.117,-0.0264,2500.0,2500.0,,filled,SIGNAL EXIT; score 0/3 (-0.0%)
- 2026-11-24 13:20,EUR/GBP,buy,2282,0.83713,0.83709,-0.0048,10000.0,,10000,filled,conf 4
- 2026-11-24 14:42,EUR/USD,buy,2286,1.09697,1.09798,0.0921,10000.0,,10000,filled,conf 4
- 2026-11-24 15:05,EUR/GBP,sell,broker,,0.83648,,,,,filled,closed by broker stop/TP; P/L -8.0793
- 2026-11-24 15:10,EUR/USD,sell,broker,,1.09651,,,,,filled,closed by broker stop/TP; P/L -14.7000
- 2026-11-24 15:12,GBP/USD,buy,2302,1.31144,1.31097,-0.0358,10000.0,,10000,filled,conf 2

## Recent Gemini decisions
- 2026-11-24 10:00,EUR/USD,buy,long,1.09346,0.00016,1.091848,1.09137,1.091276,77.4,0.000636,2,2,+0.17% (take profit) or -0.12% (stop loss); set from recent volatility,Severe RSI overbought condition fol
- 2026-11-24 11:41,USD/JPY,buy,long,159.226,0.015,159.3263,159.3048,159.2112,46.5,0.0981,3,2,+0.18% (take profit) or -0.12% (stop loss); set from recent volatility,Price fell below fast EMAs with RSI we
- 2026-11-24 13:20,EUR/GBP,buy,long,0.83713,0.00014,0.837037,0.836894,0.836761,56.7,0.00031,3,4,+0.11% (take profit) or -0.07% (stop loss); set from recent volatility,Full bullish EMA alignment and heal
- 2026-11-24 14:42,EUR/USD,buy,long,1.09697,0.00016,1.096201,1.095043,1.093426,79.3,0.000724,2,4,+0.20% (take profit) or -0.13% (stop loss); set from recent volatility,Uptrend intact; but overbought RSI
- 2026-11-24 15:12,GBP/USD,buy,long,1.31144,0.00017,1.310136,1.308833,1.307002,78.6,0.000871,2,2,+0.20% (take profit) or -0.13% (stop loss); set from recent volatility,RSI overbought at 78.6 indicates a

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-24 15:48 price 59760.98 no_trade score below 2
- Bitcoin 15m 11-24 15:49 price 59682.76 no_trade score below 2
- Bitcoin 15m 11-24 15:50 price 59746.56 no_trade score below 2
- USD/JPY 11-24 15:48 price 159.23 no_trade re-entry cooldown
- USD/JPY 11-24 15:49 price 159.23 no_trade re-entry cooldown
- USD/JPY 11-24 15:50 price 159.23 no_trade re-entry cooldown
- GBP/USD 11-24 15:48 price 1.31025 holding -0.1%
- GBP/USD 11-24 15:49 price 1.31025 holding -0.1%
- GBP/USD 11-24 15:50 price 1.31025 holding -0.1%
- EUR/USD 11-24 15:48 price 1.09619 no_trade re-entry cooldown
- EUR/USD 11-24 15:49 price 1.09619 no_trade re-entry cooldown
- EUR/USD 11-24 15:50 price 1.09619 no_trade re-entry cooldown
- EUR/GBP 11-24 15:48 price 0.83664 no_trade re-entry cooldown
- EUR/GBP 11-24 15:49 price 0.83664 no_trade re-entry cooldown
- EUR/GBP 11-24 15:50 price 0.83664 no_trade re-entry cooldown
