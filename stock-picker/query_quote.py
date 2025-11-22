from get_quote import get_stock_quote
from get_metrics import get_key_metrics, get_balance_sheet, get_cash_flow
from write_quote import write_stock_quote



def get_stock_info(stock_list):
    stock_info = {}

    for stock in stock_list:
        # Base metrics
        stock_quote             = get_stock_quote(stock)
        stock_info['date']      = stock_quote[0]
        stock_info['ticker']    = stock_quote[1]
        stock_info['quote']     = stock_quote[2]


        stock_key_metrics   = get_key_metrics(stock)
        stock_info.update(stock_key_metrics[2])

        stock_balance_sheet = get_balance_sheet(stock)
        for metric in range(2,len(stock_balance_sheet)):
            stock_info.update(stock_balance_sheet[metric])

        stock_cash_flow     = get_cash_flow(stock)
        for metric in range(2, len(stock_cash_flow)):
            stock_info.update(stock_cash_flow[metric])

        # Derived metrics
        tangible_book_value = ( stock_balance_sheet[2]['stockholdersEquity']
                                - stock_balance_sheet[3]['goodwill']
                                - stock_balance_sheet[4]['intangibleAssets'] )
        tangible_book_value_dict = {'tangible_book_value': tangible_book_value}
        stock_info.update(tangible_book_value_dict)

        price_to_TBV        = stock_key_metrics[2]['marketCap'] / tangible_book_value
        price_to_TBV_dict   = {'price_to_TBV': price_to_TBV}
        stock_info.update(price_to_TBV_dict)

        NCAV                = stock_balance_sheet[5]['currentAssets'] - stock_balance_sheet[6]['totalLiabilities']
        NCAV_dict           = {'NCAV': NCAV}
        stock_info.update(NCAV_dict)

        NNWC                = ( stock_balance_sheet[7]['cashAndCashEquivalents']
                                + (0.75 * stock_balance_sheet[9]['netReceivables'])
                                + (0.5 * stock_balance_sheet[8]['inventory'] ) )
        NNWC_dict           = {'NNWC': NNWC}
        stock_info.update(NNWC_dict)

        price_to_FCF        = stock_key_metrics[2]['marketCap'] / stock_cash_flow[2]['freeCashFlow']
        price_to_FCF_dict   = {'price_to_FCF': price_to_FCF}
        stock_info.update(price_to_FCF_dict)

        debt_to_equity      = stock_balance_sheet[12]['totalDebt'] / stock_balance_sheet[2]['stockholdersEquity']
        debt_to_equity_dict      = {'debt_to_equity': debt_to_equity}
        stock_info.update(debt_to_equity_dict)


        return stock_info




ticker_list = ['AAPL']

result = get_stock_info(ticker_list)

for metric, value in result.items():
    print(f'{metric}: {value}')









