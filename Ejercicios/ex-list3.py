import random

numbers = []

# numbers.append(2)
# numbers.append(8)
# numbers.append(1)

# print(numbers)

#ask how many number do you want to add
#append ramdomly numbers to the list

numAdd = int(input("How many numbers do you want to add? "))

for i in range(numAdd):
    numbers.append(random.randint(1, 10))

numbers.sort()
print(numbers)

numbers.pop()
print(numbers)