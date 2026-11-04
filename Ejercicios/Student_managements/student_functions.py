# Import the function used to check whether a file exists
from os.path import exists

# Import datetime to validate dates and record access timestamps
from datetime import datetime


# Check whether the required files exist and create them if necessary
def checkFile():

    # Create students.txt if it does not exist
    if not exists("students.txt"):
        with open("students.txt", "x") as file:

            # Write the column headers to the student file
            file.write("Name;Subname;ID;Birth date\n")

    # Create access.log if it does not exist
    if not exists("access.log"):
        with open("access.log", "a") as file:

            # Write the log file headers
            file.write("Date;Action\n")


# Request and validate the student's name
def inputName(text):
    while True:

        # Ask the user for a name and remove surrounding spaces
        name = input(text).strip()

        # Check that the name contains only alphabetic characters
        if name.isalpha() and len(name) >= 1:
            print("Name saved\n")

            # Return the validated name
            return name
        else:
            # Display an error message if the name is invalid
            print("Error: Invalid name, it must contain at least 1 letter!!")


# Request and validate the student's surname
def inputSubName(text):
    while True:

        # Ask the user for a surname and remove surrounding spaces
        subName = input(text).strip()

        # Check that the surname contains only alphabetic characters
        if subName.isalpha() and len(subName) >= 1:
            print("SubName saved\n")

            # Return the validated surname
            return subName
        else:
            # Display an error message if the surname is invalid
            print("Error: Invalid Subname, it must contain at least 1 letter!!")


# Request an ID and check that it is valid and unique
def inputID(num):
    while True:

        # Ask the user for an ID and remove surrounding spaces
        numID = input(num).strip()

        # Check that the ID is not empty and contains only digits
        if not numID.isnumeric() or len(numID) < 1:
            print("Error: Invalid ID, it must contain at least 1 number!!")

        # Check whether the ID already belongs to a registered student
        elif existsID(numID):
            print("This ID already exists. Enter another one!")

        else:
            # Confirm that the ID is valid and return it
            print("ID saved\n")
            return numID


# Check whether an ID already exists in the student file
def existsID(numID):

    # Open the student file in read mode
    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:

            # Split each line into fields using the semicolon separator
            row = line.strip().split(";")

            # Compare the ID field with the ID entered by the user
            if len(row) > 2 and row[2] == numID:
                return True

    # Return False if the ID was not found
    return False


# Request and validate the student's birth date
def inputBirthDate(text):
    while True:

            # Ask the user for a birth date and remove surrounding spaces
            birthDate = input(text).strip()

            try:
                # Convert the input into a date using the DD/MM/YYYY format
                fecha = datetime.strptime(birthDate, "%d/%m/%Y").date()

                # Check that the birth date is not in the future
                if fecha > datetime.today().date():
                    print("Error: The birth date cannot be in the future.")
                    continue
                else:
                    # Return the validated date in DD/MM/YYYY format
                    print("Birth date saved\n")
                    return fecha.strftime("%d/%m/%Y")

            except ValueError:
                # Handle invalid dates or an incorrect date format
                print("Error: Invalid date. Use the format DD/MM/YYYY.")


# Record an action in the application log file
def fileLog(action):

    # Ensure that the required files exist before writing to the log
    checkFile()

    # Get the current date and time in DD/MM/YYYY HH:MM:SS format
    access = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Open the log file in append mode to preserve existing entries
    with open("access.log", "a", encoding="utf-8") as file:

        # Write the timestamp and action as a new log entry
        file.write(f"{access} | {action}\n")