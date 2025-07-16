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



class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return 'stack is empty'
        else:
            self.stack.pop()

    def print(self):
        for ele in reversed(self.stack):
            print(f'|{ele}|')
            print('___')



my_stack = Stack()

print(my_stack.pop())
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.print()
my_stack.pop()
print('stack after pop\n\n')
my_stack.print()
