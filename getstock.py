import requests
from bs4 import BeautifulSoup
import json

mystocks = ['AAPL', 'NVDA', 'GOOG', 'MSFT']
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    url = f'https://www.google.com/finance/quote/{symbol}:NASDAQ';
    r = requests.get(url, headers=headers);
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'price': soup.find('div',{'class': 'YMlKec fxKbKc'}).text,
        'change': soup.find('div',{'class': 'JwB6zf'}).text,
        }
    return stock

for i in mystocks:
    stockdata.append(getData(i))
    print("Getting: ",i);

with open('stockdata.json','w') as outputdata:
    json.dump(stockdata, outputdata)