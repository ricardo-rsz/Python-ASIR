#define a list of cities
cities = ["Málaga", "Cádiz", "Sevilla", "Granada", "Córdoba", "Huelva", "Jaén", "Almería"]

#2d city in the list
# print(cities[1])

#the last city in the list
# print(cities[-1])

#between the 5th and 6th city in the list
# print(cities[4:6])

#create a new list with the last 3 cities in the list
# andaluciaOriental = cities[-3:]
# print(andaluciaOriental)

#ask if a city exits in cities list
# cityName = input("Write a city: ").strip()
# if cityName in cities:
#     print(cityName, "exists")
# else:
#     print(cityName, "Doesn't exists")

#Check if the cityName exits in cities list
#case insensitive
#tips: loop the list cities
#tips2: check in each loop upper = upper
exist = False 

cityName = input("Write a city: ").strip().upper()

for city in cities:
    if cityName == city.upper():
        exist = True
        break
if exist:
    print(cityName, "EXIST!!")
else:
    print(cityName, "Doesn't exist!!")
