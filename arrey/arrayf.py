def sort_array(array):
    # do something
    return sorted(array)

# quick hack, sort the array: incorrect
def max_stock_profit(stock_prices):
    sorted_stock = sort_array(stock_prices)
    stock_length = len(sorted_stock)

    buy_price = sorted_stock[0]
    sell_price = sorted_stock[stock_length - 1]

    max_profit = sell_price - buy_price

    return([buy_price, sell_price], max_profit)

    