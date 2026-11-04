import random
from functions import *
# from collections import Counter

gameNumber = 0

while True:
    maxNumber = inputMax()
    gameNumber += 1
    secretNumber = random.randint(1, maxNumber)
    counter = guessNumber(secretNumber, maxNumber)
    score = max(0, 1000 - counter * 100)

    print("Failed attempts:", counter)
    print("Total attempts:", counter + 1)
    print("Your score:", score, "points")

    saveScore(gameNumber, counter, score)

    while True: 
        askQuestion = input("Do you want to play another game? (Y/N): ").lower() 
        if askQuestion == "y": 
            break 
        elif askQuestion == "n": 
            print("End of the program") 
            break 
        else: 
            print("Please write only Y or N.") 

    if askQuestion == "n": 
        break