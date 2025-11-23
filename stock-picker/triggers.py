from query_quote import get_stock_info

def value_score(stock_info):
    stock_ticker = stock_info.get('ticker')

    score = 0

    stock_safety = safety_gate(stock_info)

    if not stock_safety:
        stock_score = f'{stock_ticker} does not pass the safety check.'

    else:
        liquidation_score   = liquidation(stock_info)
        cash_flow_score     = cash_flow(stock_info)
        score += liquidation_score
        score += cash_flow_score

        stock_score = f'{stock_ticker} has a score of {score}'

    return stock_score

def liquidation(stock_info):
    marketCap           = stock_info.get('marketCap')
    NNWC                = stock_info.get('NNWC')
    NCAV                = stock_info.get('NCAV')
    tangible_book_value = stock_info.get('tangible_book_value')

    liquidation_score = 0

    if marketCap < NNWC:
        liquidation_score += 5
    elif marketCap < NCAV:
        liquidation_score += 3
    elif marketCap < tangible_book_value:
        liquidation_score += 2

   return liquidation_score

def cash_flow(stock_info):
    price_to_FCF            = stock_info.get('price_to_FCF')
    marketCap               = stock_info.get('marketCap')
    freeCashFlow            = stock_info.get('freeCashFlow')
    cashAndCashEquivalents  = stock_info.get('cashAndCashEquivalents')
    totalDebt               = stock_info.get('totalDebt')

    cash_flow_trigger =  False

    if price_to_FCF < 10:
        cash_flow_trigger = True
    else:
        cash_flow_trigger = False

    if (freeCashFlow / marketCap) > 0.1:
        cash_flow_trigger = True
    else:
        cash_flow_trigger = False

    if ((marketCap + totalDebt - cashAndCashEquivalents) / freeCashFlow) < 8:
        cash_flow_trigger = True
    else:
        cash_flow_trigger = False

    return cash_flow_trigger

def safety_gate(stock_info):
    debt_to_equity      = stock_info.get('debt_to_equity')
    currentAssets       = stock_info.get('currentAssets')
    currentLiabilities  = stock_info.get('currentLiabilities')

    safety = False

    if debt_to_equity < 0.5:
        safety = True
    elif (currentAssets / currentLiabilities) > 1.5:
        safety = True
    else:
        safety = False

    return safety


#TODO:
# -  Return sub-triggers
# -  Create point-system to allow ranking
# -  Write all (sub) results and (sub) trigger eval

stock_list = ['AAPL']

stock_info = get_stock_info(stock_list)

result = safety(stock_info)

print(result)

