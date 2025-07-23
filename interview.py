# two sum
def two_sum(arr, target):
    mp = {}
    for i, v in enumerate(arr):
        diff = target - v
        if diff in mp:
            return [mp[diff], i]
        mp[v] = i
    return [0, 0]

arr = [2, 5, 1, 7, 6]
target = 9
print(two_sum(arr, target))



def anagram(str1, str2):
    n_str1 = str1.strip()
    n_str2 = str1.strip()

    return sorted(n_str1) == sorted(n_str2)

str1 = "listen"
str2 = "silent"
print(anagram(str1, str2))

def max_stock_profit(stock_day: list):
    print(type(stocks))

stocks = [2, 5, 7, 1, 9, 0]
max_stock_profit(stocks)

def convert_string(name: str) -> set:
    return set(name)

name = "Thread Miller"
print(convert_string(name))


class Queue:
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.is_empty():
            print('No item in queue!')
        else:
            self.queue.pop()
    
    def print_queue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            print(self.queue)


people = Queue()
print(people.is_empty())
people.dequeue()
people.enqueue("Thread Miller")
people.enqueue("Wool Miller")
people.enqueue("Cotton Mather")
people.print_queue()
people.dequeue()
people.print_queue()


class Stack():
    def __init__(self, name: str):
        self.stack = list()
        self.name = name

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            self.stack.pop()
    
    def print(self):
        if self.is_empty():
            print(f'{self.name} Stack is empty')
        else:
            for ind, val in enumerate(self.stack):
                print(f'|{val}|')
                print('_'* (len(val)+2))


plates = Stack('plates')

print(plates.print())
plates.push('Chinese')
plates.push('African_Wood')
plates.push('European_glass')
plates.push('Indian_ceramic')
print(plates.print())
plates.pop()
print(plates.print())



    




