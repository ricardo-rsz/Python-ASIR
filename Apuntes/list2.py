import random

print(random.randint(1, 10))

abc = "abcdefghijklmnopqrstuvwxyz"
print(abc[random.randint(0, len(abc) - 1)])

stringlen = random.randint(0, 100)

newString = ""

for i in range(stringlen):
    newString += abc[random.randint(0, len(abc) - 1)]

print(newString)