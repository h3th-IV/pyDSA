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