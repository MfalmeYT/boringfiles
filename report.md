# Bot report (generated 2026-11-25 17:29 UTC)

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
| Bitcoin 15m | 11-25 17:29 | 1422 | 0 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-25 17:29 | 1361 | 5 | 0 | 40 | 32 | -0.50 |  |
| GBP/USD | 11-25 17:29 | 1361 | 2 | 0 | 33 | 36 | +0.16 |  |
| EUR/USD | 11-25 17:29 | 1361 | 4 | 0 | 37 | 38 | +0.08 |  |
| EUR/GBP | 11-25 17:29 | 1361 | 4 | 0 | 35 | 26 | -0.46 |  |

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
- USD/JPY: long -0.06%
- USD/JPY: short -0.14%
- USD/JPY: long -0.18%
- USD/JPY: long -0.04%
- USD/JPY: short +0.23%
- USD/JPY totals: long 18 trades -0.41%, short 22 trades -0.09%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD: short +0.11%
- GBP/USD: short -0.12%
- GBP/USD totals: long 15 trades +0.02%, short 18 trades +0.14%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD: short +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long +0.23%
- EUR/USD totals: long 22 trades -0.53%, short 15 trades +0.60%
- EUR/GBP: long -0.08%
- EUR/GBP: short -0.14%
- EUR/GBP: short -0.02%
- EUR/GBP: long +0.08%
- EUR/GBP: long +0.13%
- EUR/GBP totals: long 22 trades -0.26%, short 13 trades -0.20%

## Account (latest hourly snapshot)
- 2026-11-25 16:52 UTC Oanda: balance 741.3398, equity 741.3398, free 741.3398
- 2026-11-25 17:29 UTC AlpacaCrypto: balance 933.52, equity 976.35, free 933.52

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 12:22,EUR/USD,cover,broker,,1.09548,,,,,filled,closed by broker stop/TP; P/L -11.6000
- 2026-11-25 12:25,EUR/GBP,buy,2484,0.83744,0.83753,0.0107,5000.0,,5000,filled,conf 4
- 2026-11-25 14:35,EUR/GBP,sell,broker,,0.83853,,,,,filled,closed by broker stop/TP; P/L 6.4631
- 2026-11-25 15:15,USD/JPY,short,2492,159.194,159.189,-0.0031,5000.0,,5000,filled,conf 4
- 2026-11-25 15:22,EUR/USD,buy,2498,1.09397,1.09401,0.0037,5000.0,,5000,filled,conf 3
- 2026-11-25 16:42,GBP/USD,cover,broker,,1.30885,,,,,filled,closed by broker stop/TP; P/L -8.5000
- 2026-11-25 16:43,USD/JPY,cover,broker,,158.83,,,,,filled,closed by broker stop/TP; P/L 11.1889
- 2026-11-25 16:43,EUR/USD,sell,broker,,1.09652,,,,,filled,closed by broker stop/TP; P/L 12.5500

## Recent Gemini decisions
- 2026-11-25 10:38,USD/JPY,buy,long,159.272,0.016,159.3345,159.3263,159.3064,46.8,0.103,2,3,+0.19% (take profit) or -0.13% (stop loss); set from recent volatility,Price fell below all EMAs and RSI is be
- 2026-11-25 12:15,GBP/USD,short,short,1.30726,0.00018,1.306649,1.307119,1.308181,49.0,0.000854,3,4,a 0.20% fall (take profit) or a 0.13% rise (stop loss); set from recent volatility,All indicators alig
- 2026-11-25 12:25,EUR/GBP,buy,long,0.83744,0.00015,0.837379,0.837081,0.836724,60.4,0.000329,3,4,+0.12% (take profit) or -0.08% (stop loss); set from recent volatility,Bullish alignment and healthy RSI;
- 2026-11-25 15:15,USD/JPY,short,short,159.194,0.016,159.2589,159.2866,159.2964,44.6,0.1198,3,4,a 0.23% fall (take profit) or a 0.15% rise (stop loss); set from recent volatility,Strong EMA crossover al
- 2026-11-25 15:22,EUR/USD,buy,long,1.09397,0.00015,1.094337,1.094329,1.094554,46.1,0.000844,2,3,+0.23% (take profit) or -0.15% (stop loss); set from recent volatility,Price below EMA50 with flat indica

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 17:27 price 59058.75 no_trade 1Hour trend not up
- Bitcoin 15m 11-25 17:28 price 58960.48 no_trade 1Hour trend not up
- Bitcoin 15m 11-25 17:29 price 59121.22 no_trade 1Hour trend not up
- USD/JPY 11-25 17:27 price 158.851 no_trade re-entry cooldown
- USD/JPY 11-25 17:28 price 158.851 no_trade re-entry cooldown
- USD/JPY 11-25 17:29 price 158.851 no_trade re-entry cooldown
- GBP/USD 11-25 17:27 price 1.31102 no_trade re-entry cooldown
- GBP/USD 11-25 17:28 price 1.31102 no_trade re-entry cooldown
- GBP/USD 11-25 17:29 price 1.31102 no_trade re-entry cooldown
- EUR/USD 11-25 17:27 price 1.09843 no_trade re-entry cooldown
- EUR/USD 11-25 17:28 price 1.09843 no_trade re-entry cooldown
- EUR/USD 11-25 17:29 price 1.09843 no_trade re-entry cooldown
- EUR/GBP 11-25 17:27 price 0.83785 no_trade re-entry cooldown
- EUR/GBP 11-25 17:28 price 0.83785 no_trade re-entry cooldown
- EUR/GBP 11-25 17:29 price 0.83785 no_trade re-entry cooldown
