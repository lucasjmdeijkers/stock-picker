import requests


BASE_URL = 'https://api.stockdata.org/v1/data/'

API_KEY =  'sBRGxGtAXIFewvu3Sn6ePUoOC7RMFsvO3ArAWsuu'

def get_stock_quote(ticker):
    url = f'{BASE_URL}/quote?symbols={ticker}&api_token={API_KEY}'
    response = requests.get(url)
    print(url)
    print('\n')
    print(response.status_code)

stock = 'AAPL'

get_stock_quote(stock)



