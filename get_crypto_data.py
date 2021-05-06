import pandas as pd 
from requests_html import HTMLSession
from dotenv import load_dotenv
import os
import requests 
import time
import hmac



def get_html_table(url, table_index=0, timeout=60):
    'not using this anymore - might use it later though'
    session = HTMLSession()
    FTX = session.get(url)
    FTX.html.render(timeout=timeout)
    FTX = FTX.html.html
    return pd.read_html(FTX)[table_index]

def get_coinmarket_data():
    'get data from coinmarket using their api'
    load_dotenv() #load .env file
    coin_api_key = os.environ['COINMARKETCAP_API_KEY']
    parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'CAD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': coin_api_key,
    }
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    data = requests.get(url, params=parameters, headers=headers).json()
    df = []
    for d in data['data']: 
        record = {}
        record['name'] = d['name']
        record['symbol'] = d['symbol']
        for q in d['quote']['CAD'].keys():
            record[q] = d['quote']['CAD'][q]
        df.append(record)
    return pd.DataFrame(df)

def get_ftx_data():
    'get data from ftx using their api'
    url = 'https://ftx.com/api/futures'
    secret = os.environ['READ_ONLY_FTX_API_SECRET']
    key = os.environ['READ_ONLY_FTX_API_KEY']
    ts = int(time.time()*1000)

    signature_payload = f'{ts}GET{url}'.encode()
    signature = hmac.new(secret.encode(),signature_payload,'sha256').hexdigest()
    headers = {
        'FTX-KEY': key,
        'FTX-SIGN': signature,
        'FTX-TS': str(ts)
    }
    data = requests.get(url, headers=headers).json()
    data = pd.DataFrame(data['result'])
    data['timestamp'] = ts
    return data


if __name__ == '__main__':
    load_dotenv() #load .env file
    print('Getting FTX data')
    FTX = get_ftx_data()
    print('Getting Coinmarket data')
    Crypto = get_coinmarket_data()
    print('dumping data to csv')
    FTX.to_csv('FTX.csv', index=False)
    Crypto.to_csv('Crypto_prices.csv', index=False)
