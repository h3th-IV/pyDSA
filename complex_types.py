# list
numbers = [-2, -9, -7, -5, -3]

max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)


def two_sum(numbers, target):
    num_map = {}
    for ind, val in enumerate(numbers):
        diff = target - val
        if diff in num_map:
            return [num_map[diff], ind]
        num_map[val] = ind
    return []

numbers = [ 9, 2, 5, 7, 3]
print(two_sum(numbers, target=9))


def best_profit_days(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0

    buy_price = stock_prices[0]
    sell_price = stock_prices[0]
    # start at the second price
    for price in stock_prices[1:] :
        if price < min_price:
            min_price = price
            buy_price = price
        elif price - min_price > max_profit:
            sell_price = price
            max_profit = sell_price - buy_price
    return ([buy_price, sell_price], max_profit)

stock_prices = [9, 2, 5, 7, 3]
print(best_profit_days(stock_prices))

name = "Thread Miller"
print(sorted(name.replace(" ", ""), reverse=True))


# tuples
coordinates = (75, 45)
print(coordinates.count(75))

# dictionaries
customer = {
    'name': 'Thread Miller',
    'age': 30,
    'is_verified': True
}

print(customer['name'])
# or use the get keyword
print(customer.get('name'))

# incase key do not exist, we can set a default value
print(customer.get('is_married', False))

nums = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'three',
    '4' : 'four'
}

output = ''
phone = input('enter number 1-4> ')
for i in phone:
    output += nums.get(i, "Null") + " "
print(output)

