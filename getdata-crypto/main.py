#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import json
import time
import configparser
from datetime import datetime
from binance.client import Client

config = configparser.ConfigParser()
config.read('getdata-cripto/config.ini')


def get_client_binance(**kwargs):
    binnace_account = config['binance']
    client = Client(binnace_account['API_KEY'],
                    binnace_account['API_SECRET'])
    return client

def main(**kwargs):
    symbols = ['BTCUSDT', 'ETHBTC']
    if "symbols"  in  kwargs:
        symbols = kwargs["symbols"]    
    limit = 60
    client = get_client_binance()
    data = get_data_from_symbol(client, symbols, limit)
    save_to_storage(data)
    return True

def get_data_from_symbol(client, symbols, limit):
    data_symbol = {}
    for symbol in symbols:
        try:
            candlestick = client.get_klines(symbol=symbol,
                    interval=Client.KLINE_INTERVAL_1MINUTE, limit=limit)
            data_symbol[symbol] = candlestick
        except:
            print('api-binance not found u.u')
    return data_symbol

def save_to_storage(data):
    if data is None:
        print('No data')
        return False
    timestamp = time.strftime('%Y%m%d-%H%M')
    for (symbol, values) in data.items():
        name_file = f'/data/{str(symbol)}-{timestamp}.csv'
        with open(name_file, 'w', newline='\n') as csvfile:
            candlestick_writer = csv.writer(csvfile, delimiter=',')
            for v in values:
                candlestick_writer.writerow(v)
    return True


if __name__ == '__main__':
    main()
    