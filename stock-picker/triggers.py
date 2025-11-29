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

    if marketCap < tangible_book_value:
        liquidation_score += 2

    return liquidation_score

def cash_flow(stock_info):
    price_to_FCF            = stock_info.get('price_to_FCF')
    marketCap               = stock_info.get('marketCap')
    freeCashFlow            = stock_info.get('freeCashFlow')
    cashAndCashEquivalents  = stock_info.get('cashAndCashEquivalents')
    totalDebt               = stock_info.get('totalDebt')

    enterprise_value    = marketCap + totalDebt - cashAndCashEquivalents
    FCF_yield           = (freeCashFlow / enterprise_value) * 100

    cash_flow_score = 0

    if enterprise_value / freeCashFlow < 5:
        cash_flow_score += 4
    elif enterprise_value / freeCashFlow < 8:
        cash_flow_score += 2

    if FCF_yield > 10:
        cash_flow_score += 1

    return cash_flow_score

def safety_gate(stock_info):
    debt_to_equity      = stock_info.get('debt_to_equity')
    currentAssets       = stock_info.get('currentAssets')
    currentLiabilities  = stock_info.get('currentLiabilities')

    safety = False

    if debt_to_equity < 1:
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
# -  Debug empty API responses (e.g. SPY, SQ)
# -  Add check for reported currency?
# -  Debug 402 response
