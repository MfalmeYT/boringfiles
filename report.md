# Bot report (generated 2026-11-27 12:11 UTC)

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
| Bitcoin 15m | 11-27 12:11 | 1440 | 1 | 0 | 5 | 40 | -1.65 | yes |
| USD/JPY | 11-27 12:11 | 1379 | 3 | 0 | 46 | 33 | -0.63 |  |
| GBP/USD | 11-27 12:11 | 1379 | 4 | 0 | 41 | 29 | -0.25 |  |
| EUR/USD | 11-27 12:11 | 1379 | 3 | 0 | 42 | 38 | +0.15 | yes |
| EUR/GBP | 11-27 12:11 | 1379 | 4 | 0 | 42 | 24 | -0.79 | yes |

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
- USD/JPY: long -0.08%
- USD/JPY: long +0.00%
- USD/JPY: long -0.06%
- USD/JPY: short -0.05%
- USD/JPY: long +0.11%
- USD/JPY totals: long 22 trades -0.43%, short 24 trades -0.20%
- GBP/USD: long -0.06%
- GBP/USD: long -0.10%
- GBP/USD: short -0.03%
- GBP/USD: long -0.02%
- GBP/USD: long -0.05%
- GBP/USD totals: long 21 trades -0.32%, short 20 trades +0.06%
- EUR/USD: long -0.08%
- EUR/USD: long -0.04%
- EUR/USD: long +0.14%
- EUR/USD: short -0.07%
- EUR/USD: long +0.13%
- EUR/USD totals: long 26 trades -0.38%, short 16 trades +0.53%
- EUR/GBP: short -0.04%
- EUR/GBP: long -0.05%
- EUR/GBP: long -0.06%
- EUR/GBP: short -0.04%
- EUR/GBP: short +0.07%
- EUR/GBP totals: long 25 trades -0.48%, short 17 trades -0.32%

## Account (latest hourly snapshot)
- 2026-11-27 11:46 UTC AlpacaCrypto: balance 890.49, equity 979.97, free 890.49
- 2026-11-27 12:09 UTC Oanda: balance 660.6806, equity 654.4360, free 161.0200

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-27 05:33,EUR/USD,sell,broker,,1.09856,,,,,filled,closed by broker stop/TP; P/L 10.1000
- 2026-11-27 06:59,GBP/USD,buy,2707,1.3122,1.31253,0.0251,5000.0,,5000,filled,conf 4
- 2026-11-27 08:06,USD/JPY,buy,2715,159.344,159.367,0.0144,5000.0,,5000,filled,conf 4
- 2026-11-27 08:06,EUR/GBP,cover,broker,,0.83617,,,,,filled,closed by broker stop/TP; P/L 0.8445
- 2026-11-27 08:40,GBP/USD,sell,broker,,1.31151,,,,,filled,closed by broker stop/TP; P/L -5.1000
- 2026-11-27 08:40,EUR/USD,short,2721,1.09656,1.09614,-0.0383,10000.0,,10000,filled,conf 5
- 2026-11-27 09:58,USD/JPY,sell,broker,,159.517,,,,,filled,closed by broker stop/TP; P/L 4.6544
- 2026-11-27 11:06,EUR/GBP,short,2729,0.83516,0.83489,-0.0323,5000.0,,5000,filled,conf 4

## Recent Gemini decisions
- 2026-11-27 05:11,EUR/USD,buy,long,1.09714,0.00016,1.097431,1.097355,1.09722,46.3,0.000335,2,2,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Downtrending price below all EMAs d
- 2026-11-27 06:59,GBP/USD,buy,long,1.3122,0.00019,1.312365,1.312006,1.311474,54.9,0.000514,3,4,+0.12% (take profit) or -0.08% (stop loss); set from recent volatility,Bullish EMA alignment and healthy R
- 2026-11-27 08:06,USD/JPY,buy,long,159.344,0.016,159.327,159.3051,159.2837,58.4,0.0499,3,4,+0.09% (take profit) or -0.06% (stop loss); set from recent volatility,Solid trend alignment and RSI; but low 
- 2026-11-27 08:40,EUR/USD,short,short,1.09656,0.00015,1.097305,1.097452,1.097397,38.3,0.000578,3,5,a 0.16% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,Downtrend intact wi
- 2026-11-27 11:06,EUR/GBP,short,short,0.83516,0.00013,0.835204,0.835614,0.836138,34.6,0.000287,3,4,a 0.10% fall (take profit) or a 0.07% rise (stop loss); set from recent volatility,Favorable alignment

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-27 12:09 price 61601.5 holding 0.3%
- Bitcoin 15m 11-27 12:10 price 61574.28 holding 0.3%
- Bitcoin 15m 11-27 12:11 price 61541.13 holding 0.2%
- USD/JPY 11-27 12:09 price 159.39 no_trade re-entry cooldown
- USD/JPY 11-27 12:10 price 159.39 no_trade re-entry cooldown
- USD/JPY 11-27 12:11 price 159.39 no_trade re-entry cooldown
- GBP/USD 11-27 12:09 price 1.313 no_trade max 3 open positions reached
- GBP/USD 11-27 12:10 price 1.313 no_trade max 3 open positions reached
- GBP/USD 11-27 12:11 price 1.313 no_trade max 3 open positions reached
- EUR/USD 11-27 12:09 price 1.09672 holding SHORT -0.1%
- EUR/USD 11-27 12:10 price 1.09672 holding SHORT -0.1%
- EUR/USD 11-27 12:11 price 1.09672 holding SHORT -0.1%
- EUR/GBP 11-27 12:09 price 0.8353 holding SHORT -0.0%
- EUR/GBP 11-27 12:10 price 0.8353 holding SHORT -0.0%
- EUR/GBP 11-27 12:11 price 0.8353 holding SHORT -0.0%
