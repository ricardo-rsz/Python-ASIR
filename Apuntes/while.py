

while True:
    ask = input("Do you want to finish? (Y/N): ").upper()
    if ask == "Y":
        break
    elif ask != "N":
        print("Please write only Y or N")
print("Goodbye!!")