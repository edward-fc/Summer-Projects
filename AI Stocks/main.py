""" This is machine project to learn the basic of machine learn and prediction using the bsic algorithms and functions"""

import requests
from bs4 import BeautifulSoup
def get_api(symbol,start_date,end_date):
    url = "https://www.investing.com/equities/apple-computer-inc"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)
    stock_name = soup.find('h1', {'class': 'text-xl'}).text.strip()
    print(stock_name)
    stock_price = soup.find('div', {'data-test': 'instrument-price-last'}).text.strip()
    print(stock_price)
    stock_change = soup.find('span', {'data-test': 'instrument-price-change'}).text.strip()
    return stock_name,stock_price,stock_change

"""
From any free finqnce website where i cqn use qn api to retrieve pqst data on a stock
"""
def get_data(tag):
    return 0


"""
From the same free finance website get the live data
"""
def get_live_data(tag):
    return 0

print(get_api(1,2,3))