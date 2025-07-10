def check_anagrams(word1, word2):
   n_word1 = word1.strip().lower()
   n_word2 = word2.strip().lower()

   return sorted(n_word1) == sorted(n_word2)

print(check_anagrams('silEnt', 'lisTen'))


# keyword arguments
def increment(number, by):
    return number + by

increment(5, by=1) #keyword argument to show argument name

# optional parameters, note: optional parameters are to be defined last
def _increment(number, by=1):
    return number + by

_increment(5) #function works without passing optional parameter

# xargs for function helps us to pass multiple(same type) arguments to functions
def multiply_list(*numbers):
    total = 0
    for number in numbers:
        total *= number
    return total