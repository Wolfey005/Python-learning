# -----------------------------------------------------------
# Name: Jenny Wolf 
# Course: CSC 1019 - Introduction to Python Programming
# Assignment: Exception Handling - Names and Ages
#Date: 
#
# Description:
# This program reads a person's first name and age.
# The program increments the age by one year and displays
# the result. 
# If the age entered is not an integer,
#  a ValueError exception is caught and the age is displayed
# as 0 instead.
#
# Enter "-1" to end the program.
# -------------------------------------------------------

print("Enter a first name and age seperated by a space.")
print ('Example: John 25')
print('Enter "-1" to quit.')

#Read first input line
parts = input("\n Enter name and age:"). split()
name = parts[0]
#process input until sentienl value is entered
while name != "-1":
	try:
		#convert age to an integer and add 1
		age = int(parts[1]) +1
		print(f"{name} {age}")
	except ValueError:
		#Handle invalid age input
		print(f"{name} 0")

	#Read next input line
	parts = input("Enter name and age: ").split()
	name = parts[0]



# 	#######test######
# 	Enter a first name and age seperated by a space.
# Example: John 25
# Enter "-1" to quit.

#  Enter name and age:Jenny 33
# Jenny 34
# Enter name and age: Ryan 33
# Ryan 34
# Enter name and age: Sam 9
# Sam 10
# Enter name and age: Brass monkey 10
# Brass 0
# Enter name and age: Brass 10
# Brass 11
# Enter name and age: -1
# Press any key to continue . . .


