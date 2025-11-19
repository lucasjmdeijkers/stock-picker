import os
import requests
from dotenv import load_dotenv
from datetime import date

load_dotenv()

BASE_URL = 'https://financialmodelingprep.com/stable/'
API_KEY = os.getenv('FMP_API_KEY')

def get_market_cap(ticker):
    url = f'{BASE_URL}/key-metrics?symbol={ticker}&apikey={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        stock_key_metrics    = response.json()
        stock_market_cap    = stock_key_metrics[0]['marketCap']
        market_cap_list     = [date.today(), stock_key_metrics[0]['symbol'], stock_market_cap]

        return market_cap_list

    else:
        print(f'Failed to retreive key metric data: {response.status_code}')

def get_balance_sheet(ticker):
    url = f'{BASE_URL}/balance-sheet-statement?symbol={ticker}&apikey={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        stock_balance_sheet = response.json()
        stock_stockholdersEquity = stock_balance_sheet[0]['totalStockholdersEquity']
        stock_goodwill = stock_balance_sheet[0]['goodwill']
        stock_intangibleAssets = stock_balance_sheet[0]['intangibleAssets']
        # move computed metrics to seperate function?
        tangible_book_value = stock_stockholdersEquity - stock_goodwill - stock_intangibleAssets

        stock_currentAssets = stock_balance_sheet[0]['totalCurrentAssets']
        stock_liabilites = stock_balance_sheet[0]['totalLiabiltiies']
        NCAV = stock_currentAssets - stock_liabilites

        stock_cashCashEquivalents = stock_balance_sheet[0]['cashAndCashEquivalents']
        stock_inventory = stock_balance_sheet[0]['inventory']
        stock_netReceivables= stock_balance_sheet[0]['netReceivables']
        NNWC = stock_cashCashEquivalents + (0.75 * stock_netReceivables) + (0.5 * stock_inventory)

        stock_shortDebt = stock_balance_sheet[0]['shortTermDebt']
        stock_longDebt = stock_balance_sheet[0]['longTermDebt']
        stock_totalDebt = stock_balance_sheet[0]['totalDebt']

        stock_currentLiabilities = stock_balance_sheet[0]['totalCurrentLiabilities']








        # market_cap_list = [date.today(), stock_key_metrics[0]['symbol'], stock_market_cap]

        return tangible_book_value

    else:
        print(f'Failed to retreive key metric data: {response.status_code}')

def get_cash_flow(ticker):
    url = f'{BASE_URL}/cash-flow-statement?symbol={ticker}&apikey={API_KEY}'

    response = requests.get(url)
    response = response.json()

    return response

def get_ratio(ticker):
    url = f'{BASE_URL}/ratios?symbol={ticker}&apikey={API_KEY}'

    response = requests.get(url)
    response = response.json()

    return response



test = get_balance_sheet('AAPL')

print(test)



