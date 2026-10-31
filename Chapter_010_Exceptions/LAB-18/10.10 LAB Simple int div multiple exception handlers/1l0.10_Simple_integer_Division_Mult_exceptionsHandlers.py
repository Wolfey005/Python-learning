# -----------------------------------------------------------
# Name: Jenny Wolf
# Date: October 30, 2026
# Course: CSC 1019 - Introduction to Programming (Python)
# Assignment: Exception Handling - Integer Division
#
# Description:
# This Python program prompts the user to enter two integers.
# The program performs integer division and displays the result.
# Exception handling is used to catch division-by-zero errors
# and invalid input errors.
# -----------------------------------------------------------

try:
    # Prompt user for the first integer
    user_num = int(input("Enter the first integer: "))

    # Prompt user for the second integer
    div_num = int(input("Enter the second integer: "))

    # Perform integer division
    quotient = user_num // div_num

    # Display the result
    print(f"The quotient is: {quotient}")

except ZeroDivisionError as error:
    # Handle division by zero
    print(f"Zero Division Exception: {error}")

except ValueError as error:
    # Handle invalid input
    print(f"Input Exception: {error}")