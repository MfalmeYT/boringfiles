# Bot report (generated 2026-11-16 14:54 UTC)

## Settings (read from trader.py)
- trading enabled: True; shorting enabled: True; max open positions: 3
- entry needs 2 of 3 checks (EMA 9/21/50, RSI 45-70; short = mirror) plus Gemini confidence 1-6; model gemini-3.6-flash
- Bitcoin (on): alpaca, 5Min candles, stop 2.0% / target 2.0%, size $45, min confidence 3, min hold 30 min, re-entry pause 60 min, long only
- Gold USD (on): alpaca, 15Min candles, stop 1.0% / target 1.5%, size $45, min confidence 3, min hold 90 min, re-entry pause 180 min, long only
- USD/JPY (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short
- GBP/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short
- EUR/USD (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short
- EUR/GBP (on): oanda, M15 candles, ATR stop 2.0x / target 3.0x, size 10000 units, min confidence 2, min hold 90 min, re-entry pause 180 min, long and short

## Markets (last 24h unless noted)

| market | last run UTC | runs | entries | errors | closed trades (all time) | win % | total % after fees | open |
|---|---|---|---|---|---|---|---|---|
| Bitcoin | 11-16 14:54 | 1428 | 5 | 1 | 19 | 5 | -13.05 | yes |
| Gold USD | 11-16 14:54 | 1428 | 2 | 2 | 6 | 17 | -2.73 | yes |
| USD/JPY | 11-16 14:54 | 976 | 3 | 116 | 14 | 36 | +0.07 | yes |
| GBP/USD | 11-16 14:54 | 975 | 2 | 88 | 13 | 38 | -0.11 | yes |
| EUR/USD | 11-16 14:54 | 968 | 2 | 74 | 14 | 36 | -0.16 | yes |
| EUR/GBP | 11-16 14:54 | 960 | 3 | 60 | 15 | 13 | -0.52 | yes |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x91 USD/JPY: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x61 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x56 EUR/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x40 EUR/GBP: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x18 GBP/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x13 USD/JPY: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x12 USD/JPY: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- x11 EUR/GBP: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x10 EUR/USD: OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- x9 GBP/USD: OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}

## Latest closed trades
- Bitcoin: long -0.80%
- Bitcoin: long -0.98%
- Bitcoin: long -0.38%
- Bitcoin: long -1.02%
- Bitcoin: long -0.82%
- Gold USD: long -0.73%
- Gold USD: long -0.56%
- Gold USD: long -0.58%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- USD/JPY: long -0.13%
- USD/JPY: short -0.03%
- USD/JPY: short +0.16%
- USD/JPY: short +0.18%
- USD/JPY: short -0.07%
- USD/JPY totals: long 10 trades -0.18%, short 4 trades +0.24%
- GBP/USD: short -0.07%
- GBP/USD: short -0.07%
- GBP/USD: long -0.06%
- GBP/USD: short -0.03%
- GBP/USD: short -0.08%
- GBP/USD totals: long 9 trades +0.13%, short 4 trades -0.24%
- EUR/USD: long -0.07%
- EUR/USD: long -0.11%
- EUR/USD: short +0.18%
- EUR/USD: short +0.05%
- EUR/USD: short -0.09%
- EUR/USD totals: long 11 trades -0.30%, short 3 trades +0.14%
- EUR/GBP: long -0.03%
- EUR/GBP: short -0.04%
- EUR/GBP: short -0.10%
- EUR/GBP: short +0.03%
- EUR/GBP: long -0.04%
- EUR/GBP totals: long 12 trades -0.41%, short 3 trades -0.11%

## Latest log rows
- Bitcoin 11-16 14:52 price 65033.79 holding 0.9%
- Bitcoin 11-16 14:53 price 65208.53 holding 1.2%
- Bitcoin 11-16 14:54 price 65207.1 holding 1.2%
- Gold USD 11-16 14:52 price 3871.76 holding 0.0%
- Gold USD 11-16 14:53 price 3872.87 holding 0.1%
- Gold USD 11-16 14:54 price 3870.27 holding -0.0%
- USD/JPY 11-16 14:52 price 159.604 holding SHORT -0.0%
- USD/JPY 11-16 14:53 price 159.604 holding SHORT -0.0%
- USD/JPY 11-16 14:54 price 159.604 holding SHORT -0.0%
- GBP/USD 11-16 14:52 price 1.3195 holding SHORT -0.0%
- GBP/USD 11-16 14:53 price  error OANDA candles 401: {"errorMessage":"Insufficient authorization to perform request."}
- GBP/USD 11-16 14:54 price 1.3195 holding SHORT -0.0%
- EUR/USD 11-16 14:52 price 1.10106 holding SHORT -0.0%
- EUR/USD 11-16 14:53 price  error OANDA pricing 401: {"errorMessage":"Insufficient authorization to perform request."}
- EUR/USD 11-16 14:54 price 1.10106 holding SHORT -0.0%
- EUR/GBP 11-16 14:52 price 0.83445 holding SHORT -0.0%
- EUR/GBP 11-16 14:53 price 0.83445 holding SHORT -0.0%
- EUR/GBP 11-16 14:54 price 0.83445 holding SHORT -0.0%
