# error handling using try and except

try: 
    age = int(input('enter your age: '))
    income = 200000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value!')
except ZeroDivisionError: 
    print('Cannot divide with zero.')