# numbre = int(input("Write a numbre:"))

# if numbre % 2 == 0:
#     print("The value is even")
# else:
#     print("The value is odd")

#convert the list of colors in a colors Array and print the colors that are even and odd

colors = "red, blue, green, yellow, orange, purple, pink"
colorsArray = colors.split(",")

index = 1
if len(colorsArray) > 0:
    for color in colorsArray:
        color = color.strip()
        if index % 2 == 0:
            print(color + " :EVEN")
        else:
            print(color + " :ODD")
        index +=  1