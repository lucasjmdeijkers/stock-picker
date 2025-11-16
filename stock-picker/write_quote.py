from get_quote import get_stock_quote
import csv

stock = 'AMZN'

stock_response = get_stock_quote(stock)

print(stock_response)

with open(file='quote_data.csv', mode='a', newline='') as csvfile:
    headers = ['ticker', 'price']
    writer = csv.writer(csvfile)
    writer.writerow(stock_response)




