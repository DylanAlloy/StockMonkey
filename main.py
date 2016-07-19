# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:01:06 2016

@author: Dylan
"""
from googlefinance import getQuotes
import json
import time
import winsound
import datetime

def getData(company):
    data = getQuotes(company)
    stock = json.dumps(data)
    data = json.loads(stock)
    price = data[0]['LastTradePrice']
    compareData(price)
	
def compareData(price):
    time.sleep(1)
    data = getQuotes(company)
    stock = json.dumps(data)
    data = json.loads(stock)
    update = data[0]['LastTradePrice']
    if price != update:
        winsound.PlaySound('notif.wav', winsound.SND_FILENAME)
        print('\n'+update)
        with open("stocks.dat", "a") as f:
            f.write('\n'+update+','+str(datetime.datetime.now()))

welcome = str("StockMonkey Alpha v.1\nhttp://thisiswhereidostuff.com\n\nBy using this, you agree to the following terms:\n\n #1. You will not divulge features or functionality to the public. (This is to gaurantee that it stays cheap! Please don't give any secrets away if you find them!) \n #2. You will not modify this program. \n #3. You will not record operations with video or images. (Talk about it and give critique, follow me on social media (in the docs) to tell me that it sucks or it's great.) \n\n Enjoy. Read the docs!")
print(welcome)
company = input('Stock? (i.e. AAPL, MSFT): ')
while True:
    getData(company)