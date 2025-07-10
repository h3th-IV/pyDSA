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