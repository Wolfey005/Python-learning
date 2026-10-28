# Name: Jennifer Wolf                                                         #
# project name: Project 2 part 3                                              #
# Project due date: Oct 20th 2026                                             #
# Project description:                                                        #
#     Part 3 of project 2 focus on use of functions                           #
#                                                                             #
#     uses a function that takes radius of a circle as a perameter and        #
#       retruns the circumfence and area of a circle                          #
#                                                                             #
#       Asks the user to input the radius                                     #
#        which calls the functions and prints the results                     #
#                                                                             #
###############################################################################
import math         # import math module

# define circle_calculations
def circle_calculations(radius):
    #calculate the circumference
    circumference = 2 * math.pi * radius
    # calculate the area
    area = math.pi * radius * radius
    #package and return circumference, area in a tuple
    return circumference, area

# asks for user radius input
user_radius = float(input("Enter the radius of the circle: "))    
print()

# call the function and unpack tuple (6.15)
circumference, area = circle_calculations(user_radius)

# print results
print(f"For a circle with radius: {user_radius}")
print(f"Circumference = {circumference}")
print(f"Area = {area}")