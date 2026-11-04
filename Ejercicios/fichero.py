from os.path import exists
import random

# 1 Ask for the file name
nameFile = input("Enter the name of the file: ")

# 2 Create the file with that name
if exists(nameFile):
    if exists(nameFile):
        print("The file already exists. Please choose another name.")
    else:

    # Create the file
        with open(nameFile, "w") as file:

            while True:  
                # 3 Ask for the minimum random number
                minNum = int(input("Enter the number minimum: "))

                # 4 Ask for the maximum random number
                maxNum = int(input("Enter the number maximum: "))

                # Check that the minimum is not greater than the maximum
                if minNum > maxNum:
                    print("The minimum number cannot be greater than the maximum number. Please try again.")
                    continue

                # 5 Create a line with 10 random numbers
                randomNum = []
                for i in range(10):
                    randomNum.append(str(random.randint(minNum, maxNum)))

                newRandomNumber = ",".join(randomNum)

                # Write the line to the file
                file.write(newRandomNumber + "\n")

                # 6 Ask if they want to add another line
                while True: 
                    askQuestion = input( "Do you want to add another line? (Y/N): ").lower() 
                    if askQuestion == "y": 
                        break 
                    elif askQuestion == "n": 
                        print("End of the program") 
                        break 
                    else: 
                        print("Please write only Y or N.") 
            # 7. End if N has responded
                if askQuestion == "n": 
                    break