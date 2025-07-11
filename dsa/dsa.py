def two_sums(array, target):
    differences = {}
    sums = []
    for ind, val in enumerate(array):
        diff = target - val
        if diff in differences:
            sums.append(differences[diff])
        differences[val] = ind
    return sums


num_array = [2, 4, 5, 7, 3, 6]
print(two_sums(num_array, 9))
