# Bot report (generated 2026-11-27 06:22 UTC)

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
| Bitcoin 15m | 11-27 06:22 | 1440 | 1 | 0 | 5 | 40 | -1.65 | yes |
| USD/JPY | 11-27 06:22 | 1379 | 2 | 0 | 45 | 31 | -0.74 |  |
| GBP/USD | 11-27 06:22 | 1379 | 4 | 0 | 40 | 30 | -0.20 |  |
| EUR/USD | 11-27 06:22 | 1379 | 4 | 0 | 42 | 38 | +0.15 |  |
| EUR/GBP | 11-27 06:22 | 1379 | 4 | 0 | 41 | 22 | -0.86 | yes |

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
- Bitcoin 15m: long +2.73%
- USD/JPY: short -0.06%
- USD/JPY: long -0.08%
- USD/JPY: long +0.00%
- USD/JPY: long -0.06%
- USD/JPY: short -0.05%
- USD/JPY totals: long 21 trades -0.54%, short 24 trades -0.20%
- GBP/USD: short -0.05%
- GBP/USD: long -0.06%
- GBP/USD: long -0.10%
- GBP/USD: short -0.03%
- GBP/USD: long -0.02%
- GBP/USD totals: long 20 trades -0.26%, short 20 trades +0.06%
- EUR/USD: long -0.08%
- EUR/USD: long -0.04%
- EUR/USD: long +0.14%
- EUR/USD: short -0.07%
- EUR/USD: long +0.13%
- EUR/USD totals: long 26 trades -0.38%, short 16 trades +0.53%
- EUR/GBP: short -0.11%
- EUR/GBP: short -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP: short -0.04%
- EUR/GBP totals: long 25 trades -0.48%, short 16 trades -0.38%

## Account (latest hourly snapshot)
- 2026-11-27 05:52 UTC AlpacaCrypto: balance 890.49, equity 979.15, free 890.49
- 2026-11-27 06:15 UTC Oanda: balance 660.2817, equity 660.5934, free 591.9828

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-27 02:27,Bitcoin 15m,sell,8cfc853a-5d2c-474f-b130-37642ffdeb29,61553.715,61466.2,-0.1422,0.00073773,0.00073773,,filled,TAKE PROFIT (3.1%)
- 2026-11-27 02:40,GBP/USD,buy,2681,1.31188,1.3125,0.0473,5000.0,,5000,filled,conf 5
- 2026-11-27 03:56,EUR/GBP,short,2691,0.83672,0.83669,-0.0036,1250.0,,1250,filled,conf 4
- 2026-11-27 03:59,GBP/USD,sell,broker,,1.3116,,,,,filled,closed by broker stop/TP; P/L -4.5000
- 2026-11-27 04:27,Bitcoin 15m,buy,b8aa8a90-2e5e-4d52-b8db-ae39a41932e3,61394.425,61413.74,0.0315,0.000718363,,45,filled,conf 4
- 2026-11-27 05:00,USD/JPY,cover,broker,,159.297,,,,,filled,closed by broker stop/TP; P/L -2.5363
- 2026-11-27 05:11,EUR/USD,buy,2699,1.09714,1.09755,0.0374,10000.0,,10000,filled,conf 2
- 2026-11-27 05:33,EUR/USD,sell,broker,,1.09856,,,,,filled,closed by broker stop/TP; P/L 10.1000

## Recent Gemini decisions
- 2026-11-27 02:00,USD/JPY,short,short,159.222,0.017,159.281,159.2848,159.2706,38.1,0.0386,3,5,a 0.07% fall (take profit) or a 0.05% rise (stop loss); set from recent volatility,Strong downtrend; fresh 
- 2026-11-27 02:40,GBP/USD,buy,long,1.31188,0.0002,1.311036,1.310765,1.310704,67.6,0.000448,3,5,+0.10% (take profit) or -0.07% (stop loss); set from recent volatility,Strong bullish momentum with fresh 
- 2026-11-27 03:56,EUR/GBP,short,short,0.83672,0.00012,0.836714,0.836807,0.836918,44.8,0.000172,3,4,a 0.06% fall (take profit) or a 0.04% rise (stop loss); set from recent volatility,Bearish trend align
- 2026-11-27 04:27,Bitcoin 15m,buy,long,61394.43,24.98,61307.498,61078.77,60849.155,64.7,222.793,3,4,+3.00% (take profit) or -2.00% (stop loss),Strong EMA alignment offset by recent price consolidation 
- 2026-11-27 05:11,EUR/USD,buy,long,1.09714,0.00016,1.097431,1.097355,1.09722,46.3,0.000335,2,2,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Downtrending price below all EMAs d

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-27 06:20 price 61844.54 holding 0.7%
- Bitcoin 15m 11-27 06:21 price 61667.14 holding 0.4%
- Bitcoin 15m 11-27 06:22 price 61677.26 holding 0.4%
- USD/JPY 11-27 06:20 price 159.326 no_trade re-entry cooldown
- USD/JPY 11-27 06:21 price 159.326 no_trade re-entry cooldown
- USD/JPY 11-27 06:22 price 159.326 no_trade re-entry cooldown
- GBP/USD 11-27 06:20 price 1.31256 no_trade re-entry cooldown
- GBP/USD 11-27 06:21 price 1.31256 no_trade re-entry cooldown
- GBP/USD 11-27 06:22 price 1.31256 no_trade re-entry cooldown
- EUR/USD 11-27 06:20 price 1.09784 no_trade re-entry cooldown
- EUR/USD 11-27 06:21 price 1.09784 no_trade re-entry cooldown
- EUR/USD 11-27 06:22 price 1.09784 no_trade re-entry cooldown
- EUR/GBP 11-27 06:20 price 0.83642 holding SHORT 0.0%
- EUR/GBP 11-27 06:21 price 0.83642 holding SHORT 0.0%
- EUR/GBP 11-27 06:22 price 0.83642 holding SHORT 0.0%
