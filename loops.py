# # loops: for, while
# rows = 5
# for i in range(rows):
#     spaces = " " * (rows - i - 1)
#     asteriks = "*" * (2 * i + 1)
#     print(f"{spaces}{asteriks}{spaces}")
        

# random_num = 15
# for i in range(0, 20):
#     if i == random_num:
#         print('gotten to value')
#         break
#     elif i == 10:
#         print('gotten to half value skipping 10')
#         continue
#     print(f'lift off in {i}...')

# if type(my_height) is str:
#     print('got a float directly')


# iterator = 10
# while iterator > 0:
#     print(iterator)
#     iterator -= 1

# simple shell
print('a  simple shell')
while True:
    command = input("# ")
    if command.lower() == "quit":
        break
    print('command is being processed')



# print even numbers
count = 0
for num in range(0, 10):
    if num % 2 == 0 and num != 0:
        count +=1
        print(num)
print(f'we have {count} even numbers')