from get_quote import get_stock_quote
from get_metrics import get_key_metrics, get_balance_sheet, get_cash_flow
from write_quote import write_stock_quote

stock_list = ['AAPL']

for stock in stock_list:
    # Base metrics
    stock_quote         = get_stock_quote(stock)
    stock_key_metrics   = get_key_metrics(stock)
    stock_balance_sheet = get_balance_sheet(stock)
    stock_cash_flow     = get_cash_flow(stock)

    # Derived metrics
    tangible_book_value = ( stock_balance_sheet[2]['stockholdersEquity']
                            - stock_balance_sheet[3]['goodwill']
                            - stock_balance_sheet[4]['intangibleAssets'] )

    price_to_TBV        = stock_key_metrics[2]['marketCap'] / tangible_book_value
    NCAV                = stock_balance_sheet[5]['currentAssets'] - stock_balance_sheet[6]['totalLiabilities']

    NNWC                = ( stock_balance_sheet[7]['cashAndCashEquivalents']
                            + (0.75 * stock_balance_sheet[9]['netReceivables'])
                            + (0.5 * stock_balance_sheet[8]['inventory'] )

    price_to_FCF        = stock_key_metrics[2]['marketCap'] / stock_cash_flow[2]['freeCashFlow']
    debt_to_equity      = stock_balance_sheet[12]['totalDebt'] / stock_balance_sheet[2]['stockholdersEquity']



    # TODO: Return clean list of desired metrics and quote




    # write_stock_quote(stock_response)

    # print(stock_response)


#price_to_tangible_book_value = marketCap / tangibleBookValue
# move computed metrics to seperate function?


# debt_to_euquit_ratio = totalDebt / totalStockholdersEquity


test = get_balance_sheet('AAPL')

print(test)