# Import all functions from the student_functions module
from student_functions import *

# Import pandas to work with tabular data
import pandas as pd


# Main function that displays and manages the application menu
def menu():

    # Register when the application starts
    fileLog("Application started")

    # Repeat the main menu until the user exits the application
    while True:

        # Check that the required files exist
        checkFile()

        # Display the main menu options
        print("============ STUDENT MANAGEMENT ============")
        print("1. List")
        print("2. New student")
        print("3. Query")
        print("4. View log")
        print("5. Exit")
        print("===========================================")

        # Ask the user to select an option
        student = input("Choose an option: ")

        # Option 1: List all students
        if student == "1":

            # Open the student file in read mode
            with open("students.txt", "r", encoding="utf-8") as file:

                # Read and display the file contents
                print(file.read())

            # Record the listing action in the log file
            fileLog("Students listed")

        # Option 2: Register a new student
        elif student == "2":

            # Display the new student section
            print("New student\n")

            # Request the student's name
            name = inputName("Name: ")

            # Request the student's surname
            subName = inputSubName("Subname: ")

            # Request the student's ID
            id = inputID("ID: ")

            # Request and validate the student's birth date
            birthDate = inputBirthDate("Birth Date: ")

            # Open the student file in append mode to preserve existing records
            with open("students.txt", "a", encoding="utf-8") as file:

                # Save the student's data, separating each field with a semicolon
                file.write(f"{name};{subName};{id};{birthDate}\n")

            # Record the student creation action in the log file
            fileLog(f"Student created: {id}")

            # Confirm that the student has been saved
            print("Student added successfully.")

        # Option 3: Search for students using different criteria
        elif student == "3":

            # Display the search submenu
            print("============ QUERY STUDENT ============")
            print("1. Search by Name")
            print("2. Search by Surname")
            print("3. Search by ID")
            print("4. Search by Birth Date")
            print("5. Back to Main Menu")
            print("===========================================")

            # Ask the user to select a search criterion
            query = input("Which option will you choose: ")

            # Search for a student by name
            if query == "1":

                # Read the student file into a pandas DataFrame
                # The semicolon is used to separate the columns
                df = pd.read_csv("students.txt", sep=";")

                # Request the name to search for and remove surrounding spaces
                name = input("What is the name? ").strip()

                # Compare names without distinguishing uppercase and lowercase
                result = df[df["Name"].str.lower() == name.lower()]

                # Display the search results
                print(result)

                # Record the search action in the log file
                fileLog(f"Search by name: {name}")

            # Search for a student by surname
            elif query == "2":

                # Read the student file into a pandas DataFrame
                df = pd.read_csv("students.txt", sep=";")

                # Request the surname to search for
                subName = input("What is the Subname? ").strip()

                # Compare surnames without distinguishing uppercase and lowercase
                result = df[df["Subname"].str.lower() == subName.lower()]

                # Display the search results
                print(result)

                # Record the surname search action in the log file
                fileLog(f"Search by subname: {subName}")

            # Search for a student by ID
            elif query == "3":

                # Read the student file into a pandas DataFrame
                df = pd.read_csv("students.txt", sep=";")

                # Request the ID to search for
                id = int(input("What is the ID? "))

                # Filter the DataFrame to find the matching ID
                result = df[df["ID"] == id]

                # Display the search results
                print(result)

                # Record the ID search action in the log file
                fileLog(f"Search by ID: {id}")

            # Search for a student by birth date
            elif query == "4":

                # Read the student file into a pandas DataFrame
                df = pd.read_csv("students.txt", sep=";")

                # Request the birth date to search for
                birthDate = input("What is the Birth Date? ").strip()

                # Filter the DataFrame to find students with the specified birth date
                result = df[df["Birth date"] == birthDate]

                # Display the search results
                print(result)

                # Record the birth date search action in the log file
                fileLog(f"Search by Birth Date: {birthDate}")

            # Return to the main menu
            elif query == "5":
                return menu()

        # Option 4: Display the application log
        elif student == "4":

            # Open the log file in read mode
            with open("access.log", "r", encoding="utf-8") as file:

                # Read and display all log entries
                print(file.read())

            # Record that the log file has been viewed
            fileLog("View log file")

        # Option 5: Exit the application
        elif student == "5":

            # Display the exit message
            print("Program exit")

            # Record the application shutdown in the log file
            fileLog("Application closed")

            # Stop the main menu loop
            break


# Call the main function to start the application
menu()