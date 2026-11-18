# Bot report (generated 2026-11-18 07:03 UTC)

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
| Bitcoin | 11-18 07:03 | 1440 | 4 | 0 | 26 | 8 | -15.95 | yes |
| Gold USD | 11-18 07:03 | 1440 | 1 | 0 | 9 | 11 | -4.61 |  |
| USD/JPY | 11-18 07:03 | 1379 | 4 | 0 | 21 | 33 | -0.12 |  |
| GBP/USD | 11-18 07:03 | 1379 | 4 | 2 | 18 | 33 | -0.16 |  |
| EUR/USD | 11-18 07:03 | 1379 | 4 | 1 | 20 | 35 | -0.08 | yes |
| EUR/GBP | 11-18 07:03 | 1379 | 3 | 0 | 20 | 20 | -0.47 |  |

## Raw log files (full history, one row per run)
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_goldusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_usdjpy.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_gbpusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurusd.csv
- https://raw.githubusercontent.com/MfalmeYT/boringfiles/main/bot_log_eurgbp.csv

## Errors in the last 24h (grouped)
- x1 GBP/USD: OANDA position 401: {"errorMessage":"Insufficient authorization to perform request."}
- x1 GBP/USD: OANDA candles 504: temporary gateway error (HTML page)
- x1 EUR/USD: OANDA position 503: {"errorMessage":"Unable to service request; please try again later."}

## Latest closed trades
- Bitcoin: long -0.37%
- Bitcoin: long -0.47%
- Bitcoin: long -0.68%
- Bitcoin: long +0.57%
- Bitcoin: long -0.72%
- Gold USD: long -0.47%
- Gold USD: long +0.05%
- Gold USD: long -0.55%
- Gold USD: long -0.56%
- Gold USD: long -0.77%
- USD/JPY: short -0.11%
- USD/JPY: short -0.12%
- USD/JPY: long -0.11%
- USD/JPY: long +0.14%
- USD/JPY: short +0.11%
- USD/JPY totals: long 12 trades -0.14%, short 9 trades +0.02%
- GBP/USD: short -0.03%
- GBP/USD: long -0.01%
- GBP/USD: short -0.11%
- GBP/USD: short -0.02%
- GBP/USD: short +0.12%
- GBP/USD totals: long 10 trades +0.12%, short 8 trades -0.28%
- EUR/USD: short -0.05%
- EUR/USD: long -0.09%
- EUR/USD: short +0.21%
- EUR/USD: long -0.10%
- EUR/USD: short -0.07%
- EUR/USD totals: long 13 trades -0.49%, short 7 trades +0.41%
- EUR/GBP: long +0.02%
- EUR/GBP: short -0.03%
- EUR/GBP: short -0.00%
- EUR/GBP: short +0.10%
- EUR/GBP: short -0.03%
- EUR/GBP totals: long 13 trades -0.39%, short 7 trades -0.08%

## Latest log rows
- Bitcoin 11-18 07:01 price 64559.88 buy conf 3: Price is below short EMAs after a recent drop; signal weak
- Bitcoin 11-18 07:02 price 64605.43 holding 0.0%
- Bitcoin 11-18 07:03 price 64635.5 holding 0.1%
- Gold USD 11-18 07:01 price 3775.2 no_trade score below 2
- Gold USD 11-18 07:02 price 3769.93 no_trade score below 2
- Gold USD 11-18 07:03 price 3769.52 no_trade score below 2
- USD/JPY 11-18 07:01 price 159.246 no_trade re-entry cooldown
- USD/JPY 11-18 07:02 price 159.246 no_trade re-entry cooldown
- USD/JPY 11-18 07:03 price 159.246 no_trade re-entry cooldown
- GBP/USD 11-18 07:01 price 1.31931 holding SHORT 0.0%
- GBP/USD 11-18 07:02 price 1.31931 holding SHORT 0.0%
- GBP/USD 11-18 07:03 price 1.31826 cover closed by broker stop/TP; P/L 3.3750
- EUR/USD 11-18 07:01 price 1.0982 holding SHORT 0.1%
- EUR/USD 11-18 07:02 price 1.0982 holding SHORT 0.1%
- EUR/USD 11-18 07:03 price 1.0982 holding SHORT 0.1%
- EUR/GBP 11-18 07:01 price 0.83294 cover closed by broker stop/TP; P/L -5.5932
- EUR/GBP 11-18 07:02 price 0.83238 no_trade re-entry cooldown
- EUR/GBP 11-18 07:03 price 0.83238 no_trade re-entry cooldown
