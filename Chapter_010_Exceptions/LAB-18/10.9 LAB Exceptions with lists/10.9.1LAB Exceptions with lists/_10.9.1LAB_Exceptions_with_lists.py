# -----------------------------------------------------------
# Name: Jenny Wolf
# Date: October 30, 2026
# Course: CSC 1019 - Introduction to Programming (Python)
# Assignment: Exceptions with Lists
#
# Description:
# This Python program prompts the user to enter a list index
# and attempts to access a name stored in a list of 10 names.
# The program uses exception handling to catch IndexError
# exceptions when an invalid index is entered.
#
# If the index is valid, the corresponding name is displayed.
# If the index is out of range, the program displays the
# exception message and outputs the closest valid name:
#     - The first name in the list for invalid negative indexes.
#     - The last name in the list for invalid positive indexes.
#
# Concepts Demonstrated:
# - Lists
# - List indexing
# - Negative indexing
# - try/except exception handling
# - IndexError exceptions
# -----------------------------------------------------------

names = [
    "Ryley",
    "Edan",
    "Reagan",
    "Henry",
    "Caius",
    "Jane",
    "Guto",
    "Sonya",
    "Tyrese",
    "Johnny",
]
user_input = input("Enter an index( or 'quit' to exit): ")

while user_input.lower() != "quit":

    try:
        # Convert input to an integer
        index = int(user_input)

        # Attempt to access the specified name
        print(f"Name: {names[index]}")

    except IndexError as error:
        # Handle indexes that are outside the list range
        print(f"Exception! {error}")

        # Display the closest valid name
        if index < 0:
            print(f"The closest name is: {names[0]}")
        else:
            print(f"The closest name is: {names[-1]}")

    user_input = input("\nEnter an index (or 'quit' to exit): ")

print("Program ended.")