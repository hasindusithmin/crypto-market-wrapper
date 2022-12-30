import requests
import urllib
from pandas import DataFrame


def GET_SYMBOLS():
    """
    The function provides a DataFrame of valid cryptocurrency symbols.

    Returns:
        DataFrame: Symbols
    """
    URL = 'https://www.binance.com/api/v3/exchangeInfo'
    RES = requests.get(URL)
    DATA = RES.json()
    SYMBOLS = [SYMBOL['symbol'] for SYMBOL in DATA['symbols']]
    return DataFrame({'SYMBOLS': SYMBOLS})


def GET_RECENT_TRADES_LIST(SYMBOL="BTCUSDT"):
    """
    The function provides a DataFrame containing a list of recent trades.

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT"

    Returns:
        DataFrame: Recent Trades List

    """
    URL = f'https://www.binance.com/api/v3/trades?symbol={SYMBOL.upper()}'
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    RECENT_TRADES_LIST = RES.json()
    TIME = [RECENT_TRADE['time'] for RECENT_TRADE in RECENT_TRADES_LIST]
    PRICE = [float(RECENT_TRADE['price'])
             for RECENT_TRADE in RECENT_TRADES_LIST]
    QTY = [float(RECENT_TRADE['qty']) for RECENT_TRADE in RECENT_TRADES_LIST]
    QUOTE_QTY = [float(RECENT_TRADE['quoteQty'])
                 for RECENT_TRADE in RECENT_TRADES_LIST]
    IS_BUYER_MAKER = [RECENT_TRADE['isBuyerMaker']
                      for RECENT_TRADE in RECENT_TRADES_LIST]
    IS_BEST_MATCH = [RECENT_TRADE['isBestMatch']
                     for RECENT_TRADE in RECENT_TRADES_LIST]
    return DataFrame({
        "TIME": TIME,
        "PRICE": PRICE,
        "QTY": QTY,
        "QUOTE_QTY": QUOTE_QTY,
        "IS_BUYER_MAKER": IS_BUYER_MAKER,
        "IS_BEST_MATCH": IS_BEST_MATCH
    })


def GET_AGGREGATE_TRADES_LIST(SYMBOL="BTCUSDT"):
    """
    The function provides a DataFrame containing an aggregate list of trades

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT".

    Returns:
        DataFrame: Aggregate Trades List
    """
    URL = f'https://www.binance.com/api/v3/aggTrades?symbol={SYMBOL.upper()}'
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    AGGREGATE_TRADES_LIST = RES.json()
    AGGREGATE_TRADE_ID = [AGGREGATE_TRADE['a']
                          for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    TIMESTAMP = [AGGREGATE_TRADE['T']
                 for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    PRICE = [AGGREGATE_TRADE['p'] for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    QUANTITY = [AGGREGATE_TRADE['q']
                for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    FIRST_TRADE_ID = [AGGREGATE_TRADE['f']
                      for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    LAST_TRADE_ID = [AGGREGATE_TRADE['l']
                     for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    WAS_THE_BUYER_THE_MAKER = [AGGREGATE_TRADE['m']
                               for AGGREGATE_TRADE in AGGREGATE_TRADES_LIST]
    return DataFrame({
        "AGGREGATE_TRADE_ID": AGGREGATE_TRADE_ID,
        "TIMESTAMP": TIMESTAMP,
        "PRICE": PRICE,
        "QUANTITY": QUANTITY,
        "FIRST_TRADE_ID": FIRST_TRADE_ID,
        "LAST_TRADE_ID": LAST_TRADE_ID,
        "WAS_THE_BUYER_THE_MAKER": WAS_THE_BUYER_THE_MAKER
    })


def GET_CANDLESTICK_DATA(SYMBOL="BTCUSDT", INTERVAL="1h", LIMIT=500):
    """
    The function provides a DataFrame containing candlestick data.

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT".
        INTERVAL (str, optinal): Defaults to "1h".('1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M')
        LIMIT (int, optional): A valid symbol is required(1000). Defaults to 500.

    Returns:
        DataFrame: Candlestick Data
    """
    if not INTERVAL in ['1s', '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']:
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
        'OPEN_TIME': OPEN_TIME,
        'OPEN_PRICE': OPEN_PRICE,
        'HIGH_PRICE': HIGH_PRICE,
        'LOW_PRICE': LOW_PRICE,
        'CLOSE_PRICE': CLOSE_PRICE,
        'VOLUME': VOLUME,
        'CLOSE_TIME': CLOSE_TIME,
    })


def GET_UIKLINES(SYMBOL="BTCUSDT", INTERVAL="1h", LIMIT=500):
    """
    The function provides a DataFrame containing candlestick data.

    Args:
        SYMBOL (str, optional): Defaults to "BTCUSDT".
        INTERVAL (str, optional): Defaults to "1h".('1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M')
        LIMIT (int, optional):  A valid limit is required(1000). Defaults to 500.

    Returns:
        DataFrame: UIKlines
    """
    if not INTERVAL in ['1s', '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']:
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
        'OPEN_TIME': OPEN_TIME,
        'OPEN_PRICE': OPEN_PRICE,
        'HIGH_PRICE': HIGH_PRICE,
        'LOW_PRICE': LOW_PRICE,
        'CLOSE_PRICE': CLOSE_PRICE,
        'VOLUME': VOLUME,
        'CLOSE_TIME': CLOSE_TIME,
    })


def GET_CURRENT_AVERAGE_PRICE(SYMBOL="BTCUSDT"):
    """
    The function provides a dictionary containing the current average price

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT".

    Returns:
        Dict: Current Average Price

    """
    URL = f'https://www.binance.com/api/v3/avgPrice?symbol={SYMBOL}'
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_CURRENT_AVERAGE_PRICE function to retrieve a list of valid symbols, and display them for reference."
    return RES.json()


def GET_TICKER_PRICE_CHANGE_24H(SYMBOLS=["BTCUSDT"]):
    """
    The function provides a DataFrame containing 24-hour ticker price change statistics.

    Args:
        SYMBOLS (list, optional): A valid symbol is required. Defaults to ["BTCUSDT"].

    Returns:
        DataFrame: 24hr Ticker Price Change Statistics

    """
    SYMBOLS = [SYMBOL.upper() for SYMBOL in SYMBOLS]
    STR = urllib.parse.quote(str(SYMBOLS).replace("'", '"'))
    STR = STR.replace('%2C%20', ',')
    URL = f'https://www.binance.com/api/v3/ticker/24hr?symbols={STR}'
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    TICKER_PRICE_CHANGE_24H = RES.json()
    SYMBOL = [TICKER_PRICE_CHANGE['symbol']
              for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    PRICE_CHANGE = [TICKER_PRICE_CHANGE['priceChange']
                    for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    PRICE_CHANGE_PERCENT = [TICKER_PRICE_CHANGE['priceChangePercent']
                            for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    WEIGHTED_AVGPRICE = [TICKER_PRICE_CHANGE['weightedAvgPrice']
                         for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    PREV_CLOSE_PRICE = [TICKER_PRICE_CHANGE['prevClosePrice']
                        for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    LAST_PRICE = [TICKER_PRICE_CHANGE['lastPrice']
                  for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    LAST_QTY = [TICKER_PRICE_CHANGE['lastQty']
                for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    BID_PRICE = [TICKER_PRICE_CHANGE['bidPrice']
                 for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    BID_QTY = [TICKER_PRICE_CHANGE['bidQty']
               for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    ASK_PRICE = [TICKER_PRICE_CHANGE['askPrice']
                 for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    ASK_QTY = [TICKER_PRICE_CHANGE['askQty']
               for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    OPEN_PRICE = [TICKER_PRICE_CHANGE['openPrice']
                  for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    HIGH_PRICE = [TICKER_PRICE_CHANGE['highPrice']
                  for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    LOW_PRICE = [TICKER_PRICE_CHANGE['lowPrice']
                 for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    VOLUME = [TICKER_PRICE_CHANGE['volume']
              for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    QUOTE_VOLUME = [TICKER_PRICE_CHANGE['quoteVolume']
                    for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    OPEN_TIME = [TICKER_PRICE_CHANGE['openTime']
                 for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    ASK_PRICE = [TICKER_PRICE_CHANGE['symbol']
                 for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    CLOSE_TIME = [TICKER_PRICE_CHANGE['closeTime']
                  for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    FIRST_ID = [TICKER_PRICE_CHANGE['firstId']
                for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    LAST_ID = [TICKER_PRICE_CHANGE['lastId']
               for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    COUNT = [TICKER_PRICE_CHANGE['count']
             for TICKER_PRICE_CHANGE in TICKER_PRICE_CHANGE_24H]
    return DataFrame({
        "SYMBOL": SYMBOL,
        "PRICE_CHANGE": PRICE_CHANGE,
        "PRICE_CHANGE_PERCENT": PRICE_CHANGE_PERCENT,
        "WEIGHTED_AVGPRICE": WEIGHTED_AVGPRICE,
        "PREV_CLOSE_PRICE": PREV_CLOSE_PRICE,
        "LAST_PRICE": LAST_PRICE,
        "LAST_QTY": LAST_QTY,
        "BID_PRICE": BID_PRICE,
        "BID_QTY": BID_QTY,
        "ASK_PRICE": ASK_PRICE,
        "ASK_QTY": ASK_QTY,
        "OPEN_PRICE": OPEN_PRICE,
        "HIGH_PRICE": HIGH_PRICE,
        "LOW_PRICE": LOW_PRICE,
        "VOLUME": VOLUME,
        "QUOTE_VOLUME": QUOTE_VOLUME,
        "OPEN_TIME": OPEN_TIME,
        "CLOSE_TIME": CLOSE_TIME,
        "FIRST_ID": FIRST_ID,
        "LAST_ID": LAST_ID,
        "COUNT": COUNT
    })


def GET_SYMBOL_ORDER_BOOK_TICKER(SYMBOLS=["BTCUSDT"]):
    """
    The function provides a DataFrame containing order book ticker data.

    Args:
        SYMBOLS (list, optional): Defaults to ["BTCUSDT"].

    Returns:
        DataFrame: Order Book Ticker
    """
    SYMBOLS = [SYMBOL.upper() for SYMBOL in SYMBOLS]
    STR = urllib.parse.quote(str(SYMBOLS).replace("'", '"'))
    STR = STR.replace('%2C%20', ',')
    URL = f'https://www.binance.com/api/v3/ticker/bookTicker?symbols={STR}'
    RES = requests.get(URL)
    if RES.status_code != 200:
        return "It has been determined that the symbol provided is invalid. Please utilize the GET_SYMBOLS function to retrieve a list of valid symbols, and display them for reference."
    SYMBOL_ORDER_BOOK_TICKER = RES.json()
    SYMBOL = [TICKER['symbol'] for TICKER in SYMBOL_ORDER_BOOK_TICKER]
    BIDPRICE = [TICKER['bidPrice'] for TICKER in SYMBOL_ORDER_BOOK_TICKER]
    BIDQTY = [TICKER['bidQty'] for TICKER in SYMBOL_ORDER_BOOK_TICKER]
    ASKPRICE = [TICKER['askPrice'] for TICKER in SYMBOL_ORDER_BOOK_TICKER]
    ASKQTY = [TICKER['askQty'] for TICKER in SYMBOL_ORDER_BOOK_TICKER]
    return DataFrame({
        "SYMBOL": SYMBOL,
        "BIDPRICE": BIDPRICE,
        "BIDQTY": BIDQTY,
        "ASKPRICE": ASKPRICE,
        "ASKQTY": ASKQTY
    })
