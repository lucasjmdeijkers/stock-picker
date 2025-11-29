from triggers.py import value_score
from query_quote import get_stock_info
from datetime import date


stock_list = ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'NVDA', 'GOOGL', 'META', 'NFLX', 'JPM', 'V', 'BAC', 'AMD', 'PYPL', 'DIS', 'T', 'PFE', 'COST', 'INTC', 'KO', 'TGT',
              'NKE', 'BA', 'BABA', 'XOM', 'WMT', 'GE', 'CSCO', 'VZ', 'JNJ', 'CVX', 'PLTR', 'SHOP', 'SBUX', 'SOFI', 'HOOD', 'RBLX', 'SNAP', 'AMD',
              'UBER', 'FDX', 'ABBV', 'ETSY', 'MRNA', 'LMT', 'GM', 'F', 'RIVN', 'LCID', 'CCL', 'DAL', 'UAL', 'AAL', 'TSM', 'SONY', 'ET', 'NOK', 'MRO', 'COIN',
              'RIVN', 'SIRI', 'SOFI', 'RIOT', 'CPRX', 'PYPL', 'TGT', 'VWO', 'SPYG', 'NOK', 'ROKU', 'HOOD', 'VIAC', 'ATVI', 'BIDU', 'DOCU', 'ZM', 'PINS',
              'TLRY', 'WBA', 'VIAC', 'MGM', 'NFLX', 'NIO', 'C', 'GS', 'WFC', 'ADBE', 'PEP', 'UNH', 'CARR', 'FUBO', 'HCA', 'TWTR', 'BILI', 'SIRI', 'VIAC',
              'FUBO', 'RKT']

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

    except:     #TODO: Write message to csv output to indicate it failed
        print(f'Failed to calculate value score for {stock}')


