# Bot report (generated 2026-11-25 12:17 UTC)

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
| Bitcoin 15m | 11-25 12:17 | 1440 | 0 | 0 | 4 | 25 | -4.38 |  |
| USD/JPY | 11-25 12:17 | 1379 | 5 | 0 | 39 | 31 | -0.73 |  |
| GBP/USD | 11-25 12:17 | 1379 | 3 | 0 | 32 | 38 | +0.28 | yes |
| EUR/USD | 11-25 12:17 | 1379 | 4 | 0 | 35 | 37 | -0.05 | yes |
| EUR/GBP | 11-25 12:17 | 1379 | 4 | 1 | 34 | 24 | -0.59 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc15.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x1 EUR/GBP: OANDA candles 504: temporary gateway error (HTML page)

## OANDA 401 errors, last 24h
- count: 0

## Latest closed trades
- Bitcoin 15m: long -2.45%
- Bitcoin 15m: long +3.03%
- Bitcoin 15m: long -2.51%
- Bitcoin 15m: long -2.45%
- USD/JPY: short -0.14%
- USD/JPY: long -0.06%
- USD/JPY: short -0.14%
- USD/JPY: long -0.18%
- USD/JPY: long -0.04%
- USD/JPY totals: long 18 trades -0.41%, short 21 trades -0.32%
- GBP/USD: short -0.02%
- GBP/USD: long -0.06%
- GBP/USD: long +0.17%
- GBP/USD: long -0.09%
- GBP/USD: short +0.11%
- GBP/USD totals: long 15 trades +0.02%, short 17 trades +0.26%
- EUR/USD: long -0.06%
- EUR/USD: long +0.15%
- EUR/USD: long -0.04%
- EUR/USD: long -0.14%
- EUR/USD: short +0.10%
- EUR/USD totals: long 21 trades -0.76%, short 14 trades +0.71%
- EUR/GBP: short -0.05%
- EUR/GBP: long -0.08%
- EUR/GBP: short -0.14%
- EUR/GBP: short -0.02%
- EUR/GBP: long +0.08%
- EUR/GBP totals: long 21 trades -0.39%, short 13 trades -0.20%

## Account (latest hourly snapshot)
- 2026-11-25 11:35 UTC AlpacaCrypto: balance 933.52, equity 976.9, free 933.52
- 2026-11-25 11:57 UTC Oanda: balance 737.2645, equity 742.2570, free 23.4990

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-25 07:26,USD/JPY,buy,2412,159.298,159.167,-0.0822,2500.0,,2500,filled,conf 2
- 2026-11-25 07:38,USD/JPY,sell,broker,,159.007,,,,,filled,closed by broker stop/TP; P/L -2.5406
- 2026-11-25 08:00,GBP/USD,cover,broker,,1.30703,,,,,filled,closed by broker stop/TP; P/L 6.4000
- 2026-11-25 09:02,EUR/USD,short,2420,1.0943,1.09432,0.0018,10000.0,,10000,filled,conf 4
- 2026-11-25 09:25,EUR/GBP,sell,broker,,0.83679,,,,,filled,closed by broker stop/TP; P/L 3.8824
- 2026-11-25 10:38,USD/JPY,buy,2426,159.272,159.296,0.0151,10000.0,,10000,filled,conf 3
- 2026-11-25 12:15,USD/JPY,sell,2472,159.211,159.201,-0.0063,10000.0,10000.0,,filled,SIGNAL EXIT; score 0/3 (-0.1%)
- 2026-11-25 12:15,GBP/USD,short,2476,1.30726,1.30715,-0.0084,5000.0,,5000,filled,conf 4

## Recent Gemini decisions
- 2026-11-25 06:31,EUR/GBP,buy,long,0.83608,0.00015,0.836161,0.836144,0.836194,47.1,0.0002,2,3,+0.07% (take profit) or -0.05% (stop loss); set from recent volatility,Price is capped by EMAs despite neut
- 2026-11-25 07:26,USD/JPY,buy,long,159.298,0.014,159.3531,159.3363,159.3003,47.1,0.0789,2,2,+0.15% (take profit) or -0.10% (stop loss); set from recent volatility,Downtrend intact; price below all EMAs
- 2026-11-25 09:02,EUR/USD,short,short,1.0943,0.00016,1.093952,1.094202,1.094787,48.8,0.000582,3,4,a 0.16% fall (take profit) or a 0.11% rise (stop loss); set from recent volatility,All checks align; bu
- 2026-11-25 10:38,USD/JPY,buy,long,159.272,0.016,159.3345,159.3263,159.3064,46.8,0.103,2,3,+0.19% (take profit) or -0.13% (stop loss); set from recent volatility,Price fell below all EMAs and RSI is be
- 2026-11-25 12:15,GBP/USD,short,short,1.30726,0.00018,1.306649,1.307119,1.308181,49.0,0.000854,3,4,a 0.20% fall (take profit) or a 0.13% rise (stop loss); set from recent volatility,All indicators alig

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 15m 11-25 12:15 price 58480.34 no_trade score below 2
- Bitcoin 15m 11-25 12:16 price 58491.59 no_trade score below 2
- Bitcoin 15m 11-25 12:17 price 58475.65 no_trade score below 2
- USD/JPY 11-25 12:15 price 159.211 sell SIGNAL EXIT; score 0/3 (-0.1%)
- USD/JPY 11-25 12:16 price 159.211 no_trade re-entry cooldown
- USD/JPY 11-25 12:17 price 159.211 no_trade re-entry cooldown
- GBP/USD 11-25 12:15 price 1.30726 short conf 4: All indicators align for short; but strong momentum candle opposes entry | 5000 un
- GBP/USD 11-25 12:16 price 1.30726 holding SHORT -0.0%
- GBP/USD 11-25 12:17 price 1.30726 holding SHORT -0.0%
- EUR/USD 11-25 12:15 price 1.09475 holding SHORT -0.0%
- EUR/USD 11-25 12:16 price 1.09475 holding SHORT -0.0%
- EUR/USD 11-25 12:17 price 1.09475 holding SHORT -0.0%
- EUR/GBP 11-25 12:15 price 0.83744 no_trade re-entry cooldown
- EUR/GBP 11-25 12:16 price 0.83744 no_trade re-entry cooldown
- EUR/GBP 11-25 12:17 price 0.83744 no_trade re-entry cooldown
