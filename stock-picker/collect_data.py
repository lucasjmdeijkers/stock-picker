import requests


BASE_URL = 'https://api.stockdata.org/v1/data/'

API_KEY =  'sBRGxGtAXIFewvu3Sn6ePUoOC7RMFsvO3ArAWsuu'

def get_stock_quote(ticker):
    url = f'{BASE_URL}/quote?symbols={ticker}&api_token={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        stock_data = response.json()
        return stock_data

    else:
        print(f'Failed to retrieve data: {response.status_code}')


stock = 'AAPL'

stock_response = get_stock_quote(stock)
stock_data = stock_response['data']
stock_data = stock_data[0]

if stock_response:
    print(f'{stock_data["ticker"]}: {stock_data["price"]}')





