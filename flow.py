# comparison operator <, >, ==, !=
print(10 > 3)


#control flow
weather = input('enter today\'s weather(rainy, windy, sunny, snowy): ').strip().lower()
weather.strip()

pick_jacket = None


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

my_age = 25
# ternary operator: and, or, not
legal = 'You are considered legal' if my_age > 18 else 'You are a minor'
print(legal)

rainy = weather == 'rainy'
if pick_jacket is not None:
    pick = pick_jacket == 'yes'
else:
    pick = False

if rainy and pick:
    print('you are set for a rainy day!')
else:
    print('i thought i made it clear earlier to take an umbrella, get wet then it ain\'t my problem')
