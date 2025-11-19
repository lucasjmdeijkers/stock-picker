import os
import requests
from dotenv import load_dotenv
from datetime import date

load_dotenv()

BASE_URL = 'https://api.stockdata.org/v1/data/'
API_KEY = os.getenv('STOCKDATA_API_KEY')

def get_stock_quote(ticker):
    url = f'{BASE_URL}/quote?symbols={ticker}&api_token={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        stock_data = response.json()
        stock_data = stock_data['data']
        stock_data = stock_data[0]
        quote_list = [date.today(), stock_data["ticker"], stock_data["price"]]


        return quote_list

    else:
        print(f'Failed to retrieve quote data: {response.status_code}')









