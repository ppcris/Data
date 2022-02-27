import pandas as pd
import requests
import json

## Alpaca Keys
API_KEY = "PKGTCTIG0Z2HQAIBYP76"
SECRET_KEY = "PnncC28SD0VKwgs9HyI0hruixLOxLswtMkZb1orU"
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
MARKET_URL = "https://data.alpaca.markets/v2"
BASE_URL = "https://paper-api.alpaca.markets"

## Twitter Keys 
consumer_key = "5B50sAhYk35iw8w2ey3deRhdL"
consumer_secret = "9OoduwmsiwX9eLYt0cAvym7Itc7hMvhKE94sE9P8zP5pKXvQzU"
key = "472582293-5apxX5qa9ST6aboedWk3JocB9pFkLn3l0dF3sAms"
secret = "vAlwZ9nAsv8w6A9XfYivYmtkK4VXyF36ujSEItWTbdlsr"


class Screener:
    def __init__(self, symbol):
        self.symbol = symbol
        self.max_price = 0 
        self.min_price = 0
        self.actual_price = 0
        self.rate = 0
        self.recovery = 0

def stocks():
    eliminate = ['Last Sale', 'Net Change', '% Change', 'Market Cap', 'Country', 'IPO Year',
                'Name', 'Industry', 'Sector']
    
    url = "https://github.com/ppcris/TwitterBot/blob/main/List_stocks2.csv?raw=true"
    excel = pd.read_csv(url , delimiter= ",")
    excel = excel.drop(eliminate, axis=1)

    symbols = excel["Symbol"]
    symbols = pd.Series.tolist(symbols)
    symbols_string = ','.join(symbols)

    chunks = [symbols[x:x+100] for x in range(0, len(symbols), 100)]
    chunks_string = [i for i in range(len(chunks))]
    for i in range(len(chunks_string)):
        chunks_string[i] = ','.join(chunks[i])

    return symbols, symbols_string, chunks, chunks_string

def api_call():
    return API_KEY, SECRET_KEY, APCA_API_BASE_URL 
    
def snapshoots(symbols):
    snap = "{}/stocks/snapshots".format(MARKET_URL) + "?symbols=" + symbols
    r = requests.get(snap, headers=HEADERS)
    return json.loads(r.content)

def twitter_keys():
    return consumer_key, consumer_secret, key, secret

def clock():
    clock_url = "{}/v2/clock".format(BASE_URL)
    r = requests.get(clock_url, headers=HEADERS)
    r = json.loads(r.content)
    if r["is_open"] == True:
        return "Market is open \nTime: " + r["timestamp"][0:10] 
    else:
        string = "Market is close \nTime: " + r["timestamp"][0:10]
        return string
