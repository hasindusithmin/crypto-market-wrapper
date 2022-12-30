Welcome to the crypto_market_wrapper package! This package allows users to retrieve various types of data about cryptocurrency listed on the Binance exchange. 

With this package, users can access:

- Recent Trades List
- Aggregate Trades List
- Candlestick Data
- UIKlines data
- Current Average Price
- 24hr Ticker Price Change Statistics
- Symbol Order Book Ticker

#### Install

```
pip install crypto-market-wrapper
```


#### Import

```
from crypto_market_wrapper import crypto
```

##### Symbols

The function provides a DataFrame of valid cryptocurrency symbols.

    Returns:
        DataFrame: Symbols

usage
```
crypto.GET_SYMBOLS()
```

##### Recent Trades List

The function provides a DataFrame containing a list of recent trades.

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT"

    Returns:
        DataFrame: Recent Trades List

usage
```
crypto.GET_RECENT_TRADES_LIST()
```

##### Aggregate Trades List

The function provides a DataFrame containing an aggregate list of trades

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT".

    Returns:
        DataFrame: Aggregate Trades List

usage
```
crypto.GET_AGGREGATE_TRADES_LIST()
```

#### Candlestick Data

 The function provides a DataFrame containing candlestick data.

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT".
        INTERVAL (str, optinal): Defaults to "1h".('1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M')
        LIMIT (int, optional): A valid symbol is required(1000). Defaults to 500.

    Returns:
        DataFrame: Candlestick Data

usage  
```
crypto.GET_CANDLESTICK_DATA()
```

#### UIKlines data

The function provides a DataFrame containing candlestick data.

    Args:
        SYMBOL (str, optional): Defaults to "BTCUSDT".
        INTERVAL (str, optional): Defaults to "1h".('1s','1m','3m','5m','15m','30m','1h','2h','4h','6h','8h','12h','1d','3d','1w','1M')
        LIMIT (int, optional):  A valid limit is required(1000). Defaults to 500.

    Returns:
        DataFrame: UIKlines

usage
```
crypto.GET_UIKLINES()
```


#### Current Average Price

The function provides a dictionary containing the current average price

    Args:
        SYMBOL (str, optinal): Defaults to "BTCUSDT".

    Returns:
        Dict: Current Average Price

usage
```
crypto.GET_CURRENT_AVERAGE_PRICE()
```

#### 24hr Ticker Price Change Statistics

The function provides a DataFrame containing 24-hour ticker price change statistics.

    Args:
        SYMBOLS (list, optional): A valid symbol is required. Defaults to ["BTCUSDT"].

    Returns:
        DataFrame: 24hr Ticker Price Change Statistics

usage
```
crypto.GET_TICKER_PRICE_CHANGE_24H()
```


#### Symbol Order Book Ticker

The function provides a DataFrame containing order book ticker data.

    Args:
        SYMBOLS (list, optional): Defaults to ["BTCUSDT"].

    Returns:
        DataFrame: Order Book Ticker

usage
```
crypto.GET_SYMBOL_ORDER_BOOK_TICKER()
```

