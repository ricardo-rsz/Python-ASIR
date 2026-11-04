filename = "students.txt"
with open(filename, "a") as file:

    while True:
        name = input("Write a name: ").strip()
        file.write(name + "\n")

        while True:
            askQuestion = input("Do you want to add new students? (Y/N): ").lower()
            if askQuestion == "n" or askQuestion == "y": 
                break
            elif askQuestion != "y":
                print("Please write only Y or N")
                
        if askQuestion == "n":
            break