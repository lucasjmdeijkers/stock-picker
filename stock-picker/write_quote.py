import csv



def write_stock_quote(stock_response):
    with open(file='quote_data.csv', mode='a', newline='') as csvfile:
        headers = ['ticker', 'price']

        writer = csv.writer(csvfile)
        writer.writerow(stock_response)




