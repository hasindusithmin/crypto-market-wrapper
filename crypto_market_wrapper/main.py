import requests
from pandas import DataFrame

def GET_SYMBOLS():
    URL = 'https://www.binance.com/api/v3/exchangeInfo' 
    RES = requests.get(URL)
    DATA = RES.json()
    SYMBOLS =  [SYMBOL['symbol'] for SYMBOL in DATA['symbols']]
    return DataFrame({'SYMBOLS':SYMBOLS})

def GET_RECENT_TRADES_LIST(SYMBOL):
    URL = f'https://www.binance.com/api/v3/trades?symbol={SYMBOL.upper()}' 
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    RECENT_TRADES_LIST = RES.json()
    TIME = [RECENT_TRADE['time'] for RECENT_TRADE in RECENT_TRADES_LIST]
    PRICE = [float(RECENT_TRADE['price']) for RECENT_TRADE in RECENT_TRADES_LIST]
    QTY = [float(RECENT_TRADE['qty']) for RECENT_TRADE in RECENT_TRADES_LIST]
    QUOTE_QTY = [float(RECENT_TRADE['quoteQty']) for RECENT_TRADE in RECENT_TRADES_LIST]
    IS_BUYER_MAKER = [RECENT_TRADE['isBuyerMaker'] for RECENT_TRADE in RECENT_TRADES_LIST]
    IS_BEST_MATCH = [RECENT_TRADE['isBestMatch'] for RECENT_TRADE in RECENT_TRADES_LIST]
    return DataFrame({
        "TIME":TIME,
        "PRICE":PRICE,
        "QTY":QTY,
        "QUOTE_QTY":QUOTE_QTY,
        "IS_BUYER_MAKER":IS_BUYER_MAKER,
        "IS_BEST_MATCH":IS_BEST_MATCH
    })

def GET_AGGREGATE_TRADES_LIST(SYMBOL):
    URL = f'https://www.binance.com/api/v3/aggTrades?symbol={SYMBOL.upper()}' 
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    AGGREGATE_TRADES_LIST = RES.json()
    AGGREGATE_TRADE_ID = [AGGREGATE_TRADE['a'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    TIMESTAMP = [AGGREGATE_TRADE['T'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    PRICE = [AGGREGATE_TRADE['p'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    QUANTITY = [AGGREGATE_TRADE['q'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    FIRST_TRADE_ID = [AGGREGATE_TRADE['f'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    LAST_TRADE_ID = [AGGREGATE_TRADE['l'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    WAS_THE_BUYER_THE_MAKER = [AGGREGATE_TRADE['m'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    return DataFrame({
        "AGGREGATE_TRADE_ID":AGGREGATE_TRADE_ID,
        "TIMESTAMP":TIMESTAMP,
        "PRICE":PRICE,
        "QUANTITY":QUANTITY,
        "FIRST_TRADE_ID":FIRST_TRADE_ID,
        "LAST_TRADE_ID":LAST_TRADE_ID,
        "WAS_THE_BUYER_THE_MAKER":WAS_THE_BUYER_THE_MAKER
    })

def GET_CANDLESTICK_DATA(SYMBOL,INTERVAL,LIMIT=500):
    if not INTERVAL in ['1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']:
        print('It has been determined that the specified interval is invalid. Please note that the valid intervals are as follows:')
        print("'1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M'. Please select one of these intervals for use.")
    URL = f'https://www.binance.com/api/v3/klines?symbol={SYMBOL.upper()}&interval={INTERVAL}' 
    if LIMIT == 1000:
        URL = f'https://www.binance.com/api/v3/klines?symbol={SYMBOL.upper()}&interval={INTERVAL}&limit=1000' 
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    # OPEN_TIME,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,VOLUME,CLOSE_TIME
    CANDLESTICK_DATA = RES.json()
    OPEN_TIME = [CANDLESTICK[0] for CANDLESTICK in CANDLESTICK_DATA]
    OPEN_PRICE = [float(CANDLESTICK[1]) for CANDLESTICK in CANDLESTICK_DATA]
    HIGH_PRICE = [float(CANDLESTICK[2]) for CANDLESTICK in CANDLESTICK_DATA]
    LOW_PRICE = [float(CANDLESTICK[3]) for CANDLESTICK in CANDLESTICK_DATA]
    CLOSE_PRICE = [float(CANDLESTICK[4]) for CANDLESTICK in CANDLESTICK_DATA]
    VOLUME = [float(CANDLESTICK[5]) for CANDLESTICK in CANDLESTICK_DATA]
    CLOSE_TIME = [CANDLESTICK[6] for CANDLESTICK in CANDLESTICK_DATA]
    return DataFrame({
        'OPEN_TIME':OPEN_TIME,
        'OPEN_PRICE':OPEN_PRICE,
        'HIGH_PRICE':HIGH_PRICE,
        'LOW_PRICE':LOW_PRICE,
        'CLOSE_PRICE':CLOSE_PRICE,
        'VOLUME':VOLUME,
        'CLOSE_TIME':CLOSE_TIME,
    })

def GET_UIKLINES(SYMBOL,INTERVAL,LIMIT=500):
    if not INTERVAL in ['1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M']:
        txt = '''
        It has been determined that the specified interval is invalid. Please note that the valid intervals are as follows:\n
        '1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M'. Please select one of these intervals for use.
        '''
        return txt
    URL = f'https://www.binance.com/api/v3/klines?symbol={SYMBOL.upper()}&interval={INTERVAL}' 
    if LIMIT == 1000:
        URL = f'https://www.binance.com/api/v3/klines?symbol={SYMBOL.upper()}&interval={INTERVAL}&limit=1000' 
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    # OPEN_TIME,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,VOLUME,CLOSE_TIME
    CANDLESTICK_DATA = RES.json()
    OPEN_TIME = [CANDLESTICK[0] for CANDLESTICK in CANDLESTICK_DATA]
    OPEN_PRICE = [float(CANDLESTICK[1]) for CANDLESTICK in CANDLESTICK_DATA]
    HIGH_PRICE = [float(CANDLESTICK[2]) for CANDLESTICK in CANDLESTICK_DATA]
    LOW_PRICE = [float(CANDLESTICK[3]) for CANDLESTICK in CANDLESTICK_DATA]
    CLOSE_PRICE = [float(CANDLESTICK[4]) for CANDLESTICK in CANDLESTICK_DATA]
    VOLUME = [float(CANDLESTICK[5]) for CANDLESTICK in CANDLESTICK_DATA]
    CLOSE_TIME = [CANDLESTICK[6] for CANDLESTICK in CANDLESTICK_DATA]
    return DataFrame({
        'OPEN_TIME':OPEN_TIME,
        'OPEN_PRICE':OPEN_PRICE,
        'HIGH_PRICE':HIGH_PRICE,
        'LOW_PRICE':LOW_PRICE,
        'CLOSE_PRICE':CLOSE_PRICE,
        'VOLUME':VOLUME,
        'CLOSE_TIME':CLOSE_TIME,
    })


    
    
df = GET_UIKLINES('btcusdt','20m',1000)
print(df)

