import os
import requests
from dotenv import load_dotenv
from datetime import date

load_dotenv()

BASE_URL = 'https://financialmodelingprep.com/stable/'
API_KEY = os.getenv('FMP_API_KEY')

def get_key_metrics(ticker):
    url = f'{BASE_URL}/key-metrics?symbol={ticker}&apikey={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        stock_key_metrics   = response.json()

        stock_ticker        = stock_key_metrics[0]['symbol']

        stock_market_cap    = stock_key_metrics[0]['marketCap']

        key_metrics_info    = [
            date.today(),
            stock_ticker,
            {'marketCap': stock_market_cap}
        ]

        return key_metrics_info

    else:
        print(f'Failed to retreive key metric data: {response.status_code}')

def get_balance_sheet(ticker):
    url = f'{BASE_URL}/balance-sheet-statement?symbol={ticker}&apikey={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        stock_balance_sheet = response.json()

        stock_ticker = stock_balance_sheet[0]['symbol']

        stock_stockholdersEquity    = stock_balance_sheet[0]['totalStockholdersEquity']
        stock_goodwill              = stock_balance_sheet[0]['goodwill']
        stock_intangibleAssets      = stock_balance_sheet[0]['intangibleAssets']

        stock_currentAssets         = stock_balance_sheet[0]['totalCurrentAssets']
        stock_liabilites            = stock_balance_sheet[0]['totalLiabilities']

        stock_cashCashEquivalents   = stock_balance_sheet[0]['cashAndCashEquivalents']
        stock_inventory             = stock_balance_sheet[0]['inventory']
        stock_netReceivables        = stock_balance_sheet[0]['netReceivables']

        stock_shortDebt             = stock_balance_sheet[0]['shortTermDebt']
        stock_longDebt              = stock_balance_sheet[0]['longTermDebt']
        stock_totalDebt             = stock_balance_sheet[0]['totalDebt']

        stock_currentLiabilities    = stock_balance_sheet[0]['totalCurrentLiabilities']

        balance_sheet_info          = [
            date.today(),
            stock_ticker,
            {'stockholdersEquity': stock_stockholdersEquity},
            {'goodwill': stock_goodwill},
            {'intangibleAssets': stock_intangibleAssets},
            {'currentAssets': stock_currentAssets},
            {'totalLiabilities': stock_liabilites},
            {'cashAndCashEquivalents': stock_cashCashEquivalents},
            {'inventory': stock_inventory},
            {'netReceivables': stock_netReceivables},
            {'shortTermDebt': stock_shortDebt},
            {'longTermDebt': stock_longDebt},
            {'totalDebt': stock_totalDebt},
            {'currentLiabilities': stock_currentLiabilities}
        ]

        return balance_sheet_info

    else:
        print(f'Failed to retreive balance sheet data: {response.status_code}')

def get_cash_flow(ticker):
    url = f'{BASE_URL}/cash-flow-statement?symbol={ticker}&apikey={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        stock_cash_flow     = response.json()

        stock_ticker        = stock_cash_flow[0]['symbol']

        stock_freeCashFlow  = stock_cash_flow[0]['freeCashFlow']

        cash_flow_info      = [
            date.today(),
            stock_ticker,
            {'freeCashFlow': stock_freeCashFlow}
        ]

        return cash_flow_info

    else:
        print(f'Failed to retreive cash flow data: {response.status_code}')


# test = get_balance_sheet('aapl')
# print(test)



