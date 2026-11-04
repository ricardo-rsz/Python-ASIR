numbers = [1, 8, 3, 44, 56, 63, 778, 8, 9, 10, 8, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10]

#Exercise
#ask a number
#print how many times number is in the list
#ex: write a number: 2
#2 is 4 times in the list

numberList = int(input("Write a number: ").strip())

count = 0
for n in numbers:
    if n == numberList:
        count += 1

print(numberList, "is", count, "times in the list")
