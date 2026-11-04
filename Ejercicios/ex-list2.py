myList = [3,4,5,6,8,0,3,25,487,41,655,4,41,76,47,34,9,10]

#list leng
print(len(myList))

#multiply each item by input number
#and print in the new list

myNumber = int(input("Write a number: ").strip())

index = 0
for n in myList:
    myList[index] *= myNumber
    index += 1

print(myList)