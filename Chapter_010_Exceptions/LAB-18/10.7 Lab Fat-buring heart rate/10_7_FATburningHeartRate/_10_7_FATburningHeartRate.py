# -----------------------------------------------------------
# Name: Jenny Wolf 
# Course: CSC 1019 - Introduction to Programming
# Assignment: Lab 10.7.1 - Fat-Burning Heart Rate
# Date: Oct/30/2026
#
# Description:
# This program calculates an adult's fat-burning heart rate.
# The user's age must be between 18 and 75, inclusive.
# If an invalid age is entered, a ValueError exception
# is raised and handled appropriately.
# -----------------------------------------------------------

# -----------------------------------------------------------
# Function: get_age
# Purpose:
#     Prompts the user to enter an age and validates
#     that the age is within the allowed range.
#
# Returns:
#     int - A valid age between 18 and 75.
#
# Raises:
#     ValueError - If the age is outside the valid range.
# -----------------------------------------------------------

def get_age():
    age = int(input("Enter a valid age:"))
    # TODO: Raise exception for invalid ages
    if age < 18 or age > 75:
        raise ValueError("Invalid age")
    return age

# -----------------------------------------------------------
# Function: fat_burning_heart_rate
# Purpose:
#     Calculates the fat-burning heart rate based on age.
#
# Parameter:
#     age (int) - The user's age.
#
# Returns:
#     float - The calculated fat-burning heart rate.
# -----------------------------------------------------------

def fat_burning_heart_rate(age):
    heart_rate = 0.7*(220 - age)
    return heart_rate


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    try:
        # get user's age
       age = get_age()

       # calculate heart_rate
       heart_rate = fat_burning_heart_rate(age)

        #Display result
       print(f"Fat burning heart rate for a {age} year-old: {heart_rate} bpm")
    except ValueError:
        print(f"Invalid age.")
        print(f"Could not calculate heart rate info.")