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


def two_sum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None


def two_sum_eff(arr, target):
    mp = {}
    for ind, val in enumerate(arr):
        diff = target - val
        if diff in mp:
            return [mp[diff], ind]
        mp[val] = ind
    return [0, 0]

arr = [2, 0, 5, 1, 7, 3, 8, 6, 4]
print(two_sum_eff(arr, 9))