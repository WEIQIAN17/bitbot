import requests 
import json
import pandas as pd 
from flaskr.models import User, Transaction, Balance, BitPrice
from datetime import datetime

key = '3711ff28a46fd9f7cbc915ca70a67b30'
#get cypto historical prices 
def request_CyptoPrice_hour(num=-1):
    try:
        r = requests.get('https://financialmodelingprep.com/api/v3/historical-chart/1hour/BTCUSD?apikey=' + key)

        data = r.json()
        _data = {}
        for line in data[:num]:
            _data[line["date"]] = line['close']   
        return _data
    except Exception as exc:
        print('error: ',exc)

def request_CyptoPrice_30min():
    try:
        r = requests.get('https://financialmodelingprep.com/api/v3/historical-chart/30min/BTCUSD?apikey=' + key)
        return r.json()
    except Exception as exc:
        print('error: ',exc)

def request_CyptoPrice_day(num=-1):
    try:
        r = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/BTCUSD?apikey=' + key)
        data = r.json()['historical']
        _data = {}
        for line in data[:num]:
            _data[line["date"]] = line['close']
            
        return _data
    except Exception as exc:
        print('error: ',exc)

def get_cypto_price():
        try:
            r = requests.get('https://financialmodelingprep.com/api/v3/quote/BTCUSD?apikey=' + key)
            
            price = r.json()[0]['price']
            return round(price,2)
        except Exception as exc:
            print('error: ',exc)
            

def get_balance_dict(user_name):
    user = User.query.filter_by(username=user_name).first()
    balance_list = user.balance
    balance_dict = {}
    for balance_idx in balance_list:
        #balance = Balance(balance_idx)
        #balance_dict[balance.date] = balance.cash_balance + balance.bitcoin_value + balance.bitcoin_amount
        balance_dict[balance_idx.date.strftime("%Y-%m-%d")] = balance_idx.cash_balance + balance_idx.bitcoin_value
    return balance_dict
        


if __name__ == '__main__':
    print('nothing')
