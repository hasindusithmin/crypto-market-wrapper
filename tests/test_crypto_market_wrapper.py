from crypto_market_wrapper import __version__
from crypto_market_wrapper import crypto
import requests
import urllib
from pandas import DataFrame
def test_version():
    assert __version__ == '0.1.0'
    
def test_GET_SYMBOLS():
    SYMBOLS = crypto.GET_SYMBOLS()
    URL = 'https://www.binance.com/api/v3/exchangeInfo'
    RES = requests.get(URL)
    DATA = RES.json()
    assert len(SYMBOLS) == len(DataFrame({'SYMBOLS': [SYMBOL['symbol'] for SYMBOL in DATA['symbols']]}))
