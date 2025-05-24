# ----------------------------------------------------------------------------------- #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   JDuldulao, 05/24/2025, Created Script
# ----------------------------------------------------------------------------------- #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program --------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------  
'''
FILE_NAME: str = 'Enrollments.json'

# Define the Data Variables
menu_choice: str = ''   # Hold the choice made by the user.
students: list = []     # A table of student data.

# Start of class named IO
# -----------------------------------------------------------------------------------
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    JDuldulao, 05/24/2025,Created Class
    JDuldulao, 05/24/2025,Added menu output and input functions
    JDuldulao, 05/24/2025,Added a function to display the data
    JDuldulao, 05/24/2025,Added a function to display custom error messages
    """

    @staticmethod
    # Function 1: output_error_messages(message: str, error: Exception = None)
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays the custom error messages to the user

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    # Function 2: output_menu(menu: str)
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025,Created function

        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    # Function 3: input_menu_choice()
    def input_menu_choice():
        """
        This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025,Created function

        :return: string with the users choice
        """

        menu_choice = ""

        try:
            menu_choice = input("Enter your menu choice number: ")
            if menu_choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message
        return menu_choice

    @staticmethod
    # Function 4: output_student_courses(student_data: list)
    def output_student_courses(student_data: list):
        """
        This function displays the student's name and course separated by comma. Each
        entry is separated by a new line.

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025, Created function

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            message = " {},{},{}."
            print(message.format(student["FirstName"], student["LastName"],
                student["CourseName"]))
        print("-"*50)

    @staticmethod
    # Function 5: input_student_data(student_data: list)
    def input_student_data(student_data: list):
        """
        This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025, Created function

        :return: A list of student data
        """
        try:
            # Input the data
            student_first_name = input("Enter the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Enter the student's course name? ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data
# -----------------------------------------------------------------------------------
# End of class IO

# Start of class named FileProcessor
# -----------------------------------------------------------------------------------
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    JDuldulao, 05/24/2025, Created Class
    """

    @staticmethod
    # Function 6: read_data_from_file(file_name: str, student_data: list)
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function extracts the data from JSON file and read the file data into table

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025, Created Function

        :return: A list of student data
        """

        file = None

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and not file.closed:
                file.close()
        return student_data

    @staticmethod
    # Function 7: write_data_to_file(file_name: str, student_data: list)
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function saves the data to the JSON file

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025, Created Function

        :return: None
        """

        file = None

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()

            print("-" * 50)
            print("The following data has been saved to the file:")
            for student in students:
                message = " {},{},{}."
                print(message.format(student["FirstName"], student["LastName"],
                    student["CourseName"]))
            print("-" * 50)

        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not file.closed:
                file.close()
# -----------------------------------------------------------------------------------
# End of Class FileProcessor

# Beginning of the main body of this script
# -----------------------------------------------------------------------------------
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True: # Repeat the follow tasks

    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break # out of the while loop

print("Program Ended")
