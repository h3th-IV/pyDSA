# module learning; make code more organized

def max_stock_profit(stock_prices):
    if len(stock_prices) < 2:
        return ([stock_prices[0], stock_prices[0]], 0)
    min_cost_price = stock_prices[0]
    max_profit_price = 0

    buy_price = stock_prices[0]
    sell_price = stock_prices[0]

    for price in stock_prices[1:]:
        if price < min_cost_price:
            min_cost_price = price
            buy_price = price
        
        elif price - min_cost_price > max_profit_price:
            max_profit_price = price - buy_price
            sell_price = price
    
    return ([buy_price, sell_price], max_profit_price)


