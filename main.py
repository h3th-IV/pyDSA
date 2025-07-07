#variables
my_name = 'Thread Miller'
my_age = 22
my_height = input('enter your height in meters: ')
float(my_height.strip())
married = input('are you married(yes/no): ')
if married == 'yes':
    is_married = ''
elif married == 'no':
    is_married = 'not'
print(f'my name is {my_name}, i\'m {my_age} years old, {my_height}m tall and i\'m {is_married} married')


# comparison operator <, >, ==, !=
print(10 > 3)

#control flow
weather = input('enter today\'s weather(rainy, windy, sunny, snowy): ')
weather.strip()
if weather == 'rainy':
    message = 'it\'s raining today, take an umbrella when going out!'
    pick_jacket = input('have you taken an umbrella(yes, no): ')
    if pick_jacket == 'yes':
        print('have a great day!')
    else:
        print('fool!, go back or get wet')
elif weather == 'windy':
    message = 'Take a jacket, it\'s a bit cold outside.'
elif weather == 'sunny':
    message = 'it\'s bright outside, drink a lot water to help hydrate properly'
elif weather == 'snowy':
    message = 'it\'s freezing today, keep yourself warm'
else:
    message = 'weather command not understood!'

print(message)

# ternary operator: and, or, not
legal = 'You are considered legal' if my_age > 18 else 'You are a minor'
print(legal)

rainy = True if weather == 'rainy' or not '' else False
pick = True if pick_jacket == 'yes' or not '' else False

if rainy and pick:
    print('you are set for a rainy day!')
else:
    print('i thought i made it clear earlier to take an umbrella, get wet then it ain\'t my problem')

# loops: for, while
for i in range(1, 10):
    if i % 2 != 0:
        print('*' * i)

