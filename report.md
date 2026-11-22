# Bot report (generated 2026-11-22 06:23 UTC)

## Settings (read from trader.py)
- trading enabled: True; shorting enabled: True; max open positions: 3
- entry needs 2 of 3 checks (EMA 9/21/50, RSI 45-70; short = mirror) plus Gemini confidence 1-6; model gemini-3.6-flash
- Bitcoin (off): alpaca, 5Min candles, stop 2.0% / target 2.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 60 min, signal exit on, long only
- Bitcoin 1h (off): alpaca, 1Hour candles, stop 4.0% / target 4.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 60 min, signal exit OFF, long only
- Bitcoin 15m (on): alpaca, 15Min candles, stop 2.0% / target 3.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 120 min, signal exit OFF, time stop 48h, 1Hour trend filter, pause 12h after 3 losses, long only
- Gold USD (on): alpaca, 15Min candles, stop 1.0% / target 1.5%, size $45, min confidence 3, min hold 90 min, re-entry pause 180 min, signal exit on, long only
- USD/JPY (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- GBP/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short
- EUR/GBP (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, signal exit on, long and short

## Markets (last 24h unless noted)

| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |
|---|---|---|---|---|---|---|---|---|
| Bitcoin | 11-19 00:24 | 0 | 0 | 0 | 29 | 7 | -18.45 | yes |
| Bitcoin 1h | 11-19 00:25 | 0 | 0 | 0 | 0 | - | +0.00 |  |
| Bitcoin 15m | 11-22 06:23 | 1440 | 1 | 0 | 1 | 0 | -2.45 |  |
| Gold USD | 11-22 06:23 | 1440 | 2 | 0 | 14 | 14 | -8.45 |  |
| USD/JPY | 11-21 23:46 | 1 | 0 | 1 | 27 | 37 | -0.04 |  |
| GBP/USD | 11-21 01:44 | 0 | 0 | 0 | 24 | 38 | +0.11 |  |
| EUR/USD | 11-21 01:44 | 0 | 0 | 0 | 27 | 37 | -0.04 |  |
| EUR/GBP | 11-21 01:44 | 0 | 0 | 0 | 25 | 24 | -0.45 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc1h.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_btc15.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x1 USD/JPY: OANDA position 401 [req #]: {"errorMessage":"Insufficient authorization to perform request."}

## OANDA 401 errors, last 24h
- count: 1; request IDs for OANDA support: 61573249626792112

## Latest closed trades
- Bitcoin: long +0.57%
- Bitcoin: long -0.72%
- Bitcoin: long -0.72%
- Bitcoin: long -0.68%
- Bitcoin: long -1.11%
- Bitcoin 15m: long -2.45%
- Gold USD: long -1.11%
- Gold USD: long -1.14%
- Gold USD: long -0.83%
- Gold USD: long +0.02%
- Gold USD: long -0.79%
- USD/JPY: short -0.09%
- USD/JPY: short -0.04%
- USD/JPY: short +0.20%
- USD/JPY: short -0.11%
- USD/JPY: short +0.11%
- USD/JPY totals: long 12 trades -0.14%, short 15 trades +0.10%
- GBP/USD: short +0.21%
- GBP/USD: short -0.08%
- GBP/USD: long -0.06%
- GBP/USD: short -0.17%
- GBP/USD: short +0.19%
- GBP/USD totals: long 11 trades +0.06%, short 13 trades +0.05%
- EUR/USD: short -0.08%
- EUR/USD: long -0.09%
- EUR/USD: long +0.10%
- EUR/USD: short -0.11%
- EUR/USD: long -0.07%
- EUR/USD totals: long 16 trades -0.55%, short 11 trades +0.51%
- EUR/GBP: long -0.06%
- EUR/GBP: long +0.12%
- EUR/GBP: long -0.08%
- EUR/GBP: long -0.05%
- EUR/GBP: long +0.09%
- EUR/GBP totals: long 18 trades -0.38%, short 7 trades -0.08%

## Account (latest hourly snapshot)
- 2026-11-22 05:54 UTC AlpacaCrypto: balance 979.34, equity 979.34, free 979.34
- 2026-11-22 06:16 UTC Oanda: balance 821.5243, equity 821.5243, free 821.5243

## Recent fills (decision price vs real fill; columns: time_utc,market,action,order_id,decision_price,fill_price,move_pct,fill_qty,position_qty,requested,status,reason)
- 2026-11-20 22:47,Gold USD,buy,43f1175e-3b7b-4e1b-9015-e41fa4b53ee2,3532.824,3550.91,0.5119,0.012424356,,45,filled,conf 4
- 2026-11-21 03:32,Gold USD,sell,53750fe8-2f6a-41c8-b093-8538a3ce855a,3521.2825,3512.01,-0.2633,0.012393295,0.012393295,,filled,SIGNAL EXIT; score 0/3 (-0.8%)
- 2026-11-21 07:16,Gold USD,buy,728e4d4e-1a84-4d9f-9c50-f37ec473d47e,3524.3,3540.5,0.4597,0.012462816,,45,filled,conf 5
- 2026-11-21 14:22,Bitcoin 15m,buy,ad109ffc-31a9-4a2a-9116-3abd40aad4fe,60384.316,60458.862,0.1235,0.000729932,,45,filled,conf 3
- 2026-11-21 22:31,Gold USD,sell,b0f86a01-0fac-4658-98a6-20bbd1cb74ad,3542.75,3524.78,-0.5072,0.012431658,0.012431658,,filled,SIGNAL EXIT; score 0/3 (0.1%)
- 2026-11-22 01:31,Gold USD,buy,4d386986-ea23-44d5-8d23-7356a8ef4e2a,3551.42,3569.5,0.5091,0.012358611,,45,filled,conf 4
- 2026-11-22 03:01,Gold USD,sell,3ebd617e-170d-4461-995c-aaaab8148b41,3541.2585,3522.77,-0.5221,0.012327714,0.012327714,,filled,SIGNAL EXIT; score 0/3 (-0.8%)
- 2026-11-22 03:05,Bitcoin 15m,sell,b9db1cf1-e7c6-461d-8283-70e1f2861050,59206.436,59224.2,0.03,0.000728107,0.000728107,,filled,STOP LOSS (-2.1%)

## Recent Gemini decisions
- 2026-11-21 13:37,Bitcoin 15m,gemini_hold,long,60268.03,14.286,59022.282,58441.793,58196.943,82.6,462.641,2,2,+3.00% (take profit) or -2.00% (stop loss),Extremely overbought RSI at 82.6 indicates high 
- 2026-11-21 13:52,Bitcoin 15m,gemini_hold,long,60613.7,18.8,59350.658,58644.45,58293.697,84.4,477.05,2,2,+3.00% (take profit) or -2.00% (stop loss),RSI at 84.4 signals an exhausted overbought spike vul
- 2026-11-21 14:07,Bitcoin 15m,gemini_hold,long,60458.48,17.47,59547.293,58796.482,58371.948,83.6,473.825,2,2,+3.00% (take profit) or -2.00% (stop loss),RSI overbought at 83.6 with momentum exhausting n
- 2026-11-21 14:22,Bitcoin 15m,buy,long,60384.32,18.214,59670.997,58918.257,58440.365,78.0,486.792,2,3,+3.00% (take profit) or -2.00% (stop loss),Strong uptrend but overbought RSI 78 indicates potential
- 2026-11-22 01:31,Gold USD,buy,long,3551.42,,3551.043,3550.628,3547.036,52.9,23.864,3,4,+1.50% (take profit) or -1.00% (stop loss),Bullish alignment and EMA support; but momentum is currently flat

## Data files
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/fills.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/decisions.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/data/account.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/status.md
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/report.json

## Latest log rows
- Bitcoin 11-19 00:22 price 62610.04 holding 0.2%
- Bitcoin 11-19 00:23 price 62606.65 holding 0.2%
- Bitcoin 11-19 00:24 price 62630.6 holding 0.3%
- Bitcoin 1h 11-19 00:25 price 62607.78 holding 0.2%
- Bitcoin 15m 11-22 06:21 price 58952.54 no_trade score below 2
- Bitcoin 15m 11-22 06:22 price 58903.12 no_trade score below 2
- Bitcoin 15m 11-22 06:23 price 58912.61 no_trade score below 2
- Gold USD 11-22 06:21 price 3531.45 no_trade score below 2
- Gold USD 11-22 06:22 price 3530.24 no_trade score below 2
- Gold USD 11-22 06:23 price 3530.24 no_trade score below 2
- USD/JPY 11-21 01:43 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- USD/JPY 11-21 01:44 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- USD/JPY 11-21 23:46 price  error OANDA position 401 [req 61573249626792112]: {"errorMessage":"Insufficient authorization to
- GBP/USD 11-21 01:42 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- GBP/USD 11-21 01:43 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- GBP/USD 11-21 01:44 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- EUR/USD 11-21 01:42 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- EUR/USD 11-21 01:43 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- EUR/USD 11-21 01:44 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- EUR/GBP 11-21 01:42 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- EUR/GBP 11-21 01:43 price  error OANDA position 503 [req 0]: {"errorMessage":"System under maintenance; please try again la
- EUR/GBP 11-21 01:44 price  error OANDA position 401 [req 61572916982061566]: {"errorMessage":"Insufficient authorization to
