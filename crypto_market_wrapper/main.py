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

df = GET_RECENT_TRADES_LIST('btcusd')
print(df)

