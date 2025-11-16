from get_quote import get_stock_quote
from write_quote import write_stock_quote

stock_list = ['AMZN', 'AAPL', 'MSFT']

for stock in stock_list:
    stock_response = get_stock_quote(stock)
    write_stock_quote(stock_response)

    # print(stock_response)

