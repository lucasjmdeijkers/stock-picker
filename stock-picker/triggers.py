from query_quote import get_stock_info

def liquidation(stock_info):
    marketCap       = stock_info.get('marketCap')
    NNWC            = stock_info.get('NNWC')
    NCAV            = stock_info.get('NCAV')
    price_to_TBV    = stock_info.get('price_to_TBV')

    liquidation_trigger = False

    if marketCap < (NCAV * 0.66):
        liquidation_trigger = True
    else:
        liquidation_trigger = False

    if marketCap < NNWC:
        liquidation_trigger = True
    else:
        liquidation_trigger = False

    if price_to_TBV < 1:
        liquidation_trigger = True
    else:
        liquidation_trigger = False

    return liquidation_trigger

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

def safety(stock_info):
    debt_to_equity      = stock_info.get('debt_to_equity')
    currentAssets       = stock_info.get('currentAssets')
    currentLiabilities  = stock_info.get('currentLiabilities')

    safety = False

    if debt_to_equity < 0.5:
        safety = True
    else:
        safety = False

    if (currentAssets / currentLiabilities) > 1.5:
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

