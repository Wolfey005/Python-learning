# -----------------------------------------------------------
# Name: Jenny Wolf
# Date: October 31, 2026
# Course: CSC 1019 - Introduction to Programming (Python)
# Assignment: LAB 10.12 Exception Handling - Custom Types
#
# Description:
# This program allows users to search a student database using
# either a student's name or ID. Student records are stored in
# a dictionary and displayed in a formatted menu interface.
# Custom exception handling is used to provide meaningful error
# messages when a requested student record cannot be found.
# ----------------------------------------------------------

 #Define custom exception
class StudentInfoError(Exception):

    def __init__(self, message):
        self.message = message  # Initialize the exception message

def find_ID(name, info):
    # check if student name exists in dictionary
    if name in info:
        return info[name]
    #otherwise raise exception w/ custom type StudentInfoError,("Student ID not found for studentName",)
    # student name = name of student?
    raise StudentInfoError(f"Student ID not found for {name}")
    
# Find a students name using ID
def find_name(ID, info):
    #search for matching ID in dictionary
    for name, student_id in info.items():
        if student_id == ID:
            return name
    raise StudentInfoError(f"Student name not found for {ID}")

def display_students(info):
    """Display all students currently in the database."""

    print("\n+----------------------------------+")
    print("|     Available Student Names      |")
    print("+----------------------------------+")

    for student in info:
        print(f"| {student:<32} |")

    print("+----------------------------------+\n")

if __name__ == "__main__":
    # Dictionary of student names and IDs
    student_info = {
        "Reagan": "rebradshaw835",
        "Ryley": "rbarber894",
        "Peyton": "pstott885",
        "Tyrese": "tmayo945",
        "Caius": "ccharlton329",
    }

    print("\n+==================================+")
    print("|    Student Information Lookup    |")
    print("+==================================+")
    print("| Select a search option:          |")
    print("|    0 - Find Student ID           |")
    print("|    1 - Find Student Name         |")
    print("+==================================+")

    display_students(student_info)

    userChoice = input("Enter your choice (0 or 1):")  # Read search option from user. 0: find_ID(), 1: find_name()

        # FIXME: find_ID() and find_name() may raise an Exception.
        #        Insert a try/except statement to catch the exception and output any exception message.
    try:
        if userChoice == "0":
            name = input("Enter student name: ")
            result = find_ID(name, student_info)
            print("\n+----------------------------------+")
            print("|           Search Result          |")
            print("+----------------------------------+")
            print(f"| Student ID: {result:<20} |")
            print("+----------------------------------+")
        elif userChoice =="1":
            ID = input("Enter student ID: ")
            result = find_name(ID, student_info)
            print("\n+----------------------------------+")
            print("|           Search Result          |")
            print("+----------------------------------+")
            print(f"| Student Name: {result:<18} |")
            print("+----------------------------------+")

        else:
            raise StudentInfoError("Invalid menu option selected.")
        ID = input()
    except StudentInfoError as excpt:
        print("\n+----------------------------------+")
        print("|              ERROR               |")
        print("+----------------------------------+")
        #output exception message
        print(excpt.message)
        print("+----------------------------------+")
    