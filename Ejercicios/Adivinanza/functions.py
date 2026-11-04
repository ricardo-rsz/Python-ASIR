# def maxCheck(max):
#     if max > 0:
#         return True
#     else: 
#         return False

def writeNumber(text):
    while True:
        try:
            number = int(input(text).strip())
            return number
        except ValueError:
            print("Error! you must write a number")

def inputMax():
    while True:
        dificulty = input("Select difficulty--> Easy, Medium, Hard or Expert: ").strip().lower()
        if dificulty == "easy":
            print("The number max is 10.")
            return 10
        elif dificulty == "medium":
            print("The number max is 50.")
            return 50
        elif dificulty == "hard":
            print("The number max is 100.")
            return 100
        elif dificulty == "expert":
            print("The number max is 1000.")
            return 1000
        else:
            print("Error! Select Easy, Medium, Hard or Expert.")
        # if maxCheck(max):
        #     return max
        # else:
        #     print("Error! The maximum value must be greater than 0")

def guessNumber(secretNumber, maxNumber):
    counter = 0
    repeated = set()

    while True:
        number = writeNumber("Guess the secret number: ")

        if number < 1 or number > maxNumber:
            print("Error! Enter a number between 1 and", maxNumber)
            continue

        if number in repeated:
            print("You have already tried that number. It does not count as an attempt.")
            continue

        repeated.add(number)

        if number == secretNumber:
            print("Congratulations!!! You found the secret number")
            print("Numbers used:", sorted(repeated))
            return counter

        coldHot = abs(number - secretNumber)

        if 1 <= coldHot <= 2:
            print("Very hot!")
        elif 3 <= coldHot <= 5:
            print("Hot!")
        elif 6 <= coldHot <= 10:
            print("Warm!")
        else:
            print("Cold!")

        if number > secretNumber:
            print("The secret number is smaller")
        else:
            print("The secret number is larger")

        counter += 1
        print("Attempts so far:", counter)


def saveScore(gameNumber, counter, score):
    with open("puntuaciones.txt", "a", encoding="utf-8") as file:
        file.write(
            "Partida: " + str(gameNumber) +
            " | Fallos: " + str(counter) +
            " | Puntuación: " + str(score) +
            " puntos\n"
        )