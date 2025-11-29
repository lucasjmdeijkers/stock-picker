from triggers.py import value_score
from query_quote import get_stock_info
from datetime import date


today = date.today()

for stock in stock_list:
    try:    # Temporary handling of api response errors/bug
        stock_info = get_stock_info(stock)
        result = value_score(stock_info)

        stock_info.update('value_score': result)
        date_entry = {'date': today}

        query_result = date_entry
        query_result.update(stock_info)

        with open(file='stock_queries.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            headers = ['metric', 'value']

            for key, value in query_result.items():
                writer.writerow([key,value])

            writer.writerow([" ", " "]) # White space after a stock, is there a built-in param for this?

    except:     #TODO: Write message to csv output to indicate it failed
        print(f'Failed to calculate value score for {stock}')


