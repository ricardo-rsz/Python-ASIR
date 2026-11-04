fruit = "banana"
print(fruit[0])

for x in fruit:
    print(x, end="-")

print("")
print(fruit[3:6])#This prints ana
print(fruit[:3])#This prints ban
print(fruit[3:6])#This prints ana
print(fruit[-4:-2])#This prints na

fruit = fruit.upper()#This converts the string to uppercase
print(fruit)#This prints BANANA
print(fruit.lower())#This prints banana

hello = " Hello, World! "
hello = hello.strip()#deletes the whitespace at the beginning and end of the string
print(hello)

print(hello.replace("H", "K"))#This replaces the H with K

nombres="oscar,miguel,jose carlos,carmen"
nombresArray = nombres.split(",")#This splits the string into an array

for nombre in nombresArray:
    print(nombre)

print(nombresArray[len(nombresArray)-1])#This prints the last element of the array