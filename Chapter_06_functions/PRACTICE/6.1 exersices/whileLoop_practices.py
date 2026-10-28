#You press the first key combo (Ctrl + K) and then, while still holding Ctrl, press the second key (C or U).

# user_value = int(input())

# min_number = user_value

# while user_value > 0:
#     if user_value < min_number:
#         min_number = user_value
#     user_value = int(input())

# print(f"Min value: {min_number}")


############################2###################################
# final_product = 1

# user_value = int(input())

# while user_value > 0:
#     final_product = final_product * user_value
#     user_value = int(input())

# print(f"Product: {final_product}")

# Product: 24
# Correct final_product is assigned with 1. Then, user_value is assigned with the first input.
# The while loop iterates while user_value is greater than 0. In each iteration, final_product is assigned with final_product times user_value.
# At the loop body's end, user_value is assigned with the next input. After the loop exits, final_product's value is output.
#####################################################################################


# curr_age = int(input())

# while (curr_age < 16 or curr_age > 65):
#     if curr_age < 16:
#         print("20% discount")
#     else:
#          print("10% discount")
#     curr_age = int(input())

# print("No discount")

# input :55 22
# Correct curr_age is assigned with the first input. 
# The while loop iterates while curr_age is less than 16 or curr_age is greater than 65.
# In each iteration, if curr_age is less than 16, then "20% discount" is output. 
# Otherwise, "10% discount" is output. At the loop body's end, curr_age is assigned with the next input. After the loop exits, "No discount" is output.

# Yours	No discount
# Expected	
# No discount
 ##################################################################

 #Jump to level 1
# Integer num_successes is initialized with 0. 
# Input consists of integers that are experimental data.
#  Write a loop that iterates while num_successes is less than 4.
#   In each iteration of the loop:

# Read integer curr_displacement from input.
# If curr_displacement is between 18 and 48, both inclusive,
#  then increment num_successes and 
#  output curr_displacement.
# 
# Click here for example

# Ex: If the input is:
# 18
# 49
# 48
# 48
# 17
# 40
# then the output is:

# 18
# 48
# 48
# 40

############################################################
# String input_key and integer food_count are read from input. Write a loop that iterates while food_count is between 55 and 80, both exclusive. In each iteration of the loop:

# Read string input_key from input.
# Read integer food_count from input.

# num_successes = 0;

# while num_successes < 4 :    #while num_successes is less than 4.
#     curr_displacement = int(input())    # Read integer curr_displacement from input.

#     if (curr_displacement >= 18) and (curr_displacement <= 48): # If curr_displacement is between 18 and 48, both inclusive,
#         num_successes = num_successes +1 #  then increment num_successes and 
#         print(curr_displacement)        #  output curr_displacement.
############################################################

# String input_key and integer food_count are read from input. 
# Write a loop that iterates while food_count is between 55 and 80, both exclusive.

#  In each iteration of the loop:

#     Read string input_key from input.
#     Read integer food_count from input.


# input_key = input()
# food_count = int(input())

# #Write a loop that iterates while food_count is between 55 and 80, both exclusive.
# while (food_count > 55 and food_count < 80):
#                                          # In each iteration of the loop:
#     input_key = input()                  #Read string input_key from input.

#     food_count = int(input())                #Read integer food_count from input. INT
# print(f"{input_key}: needs attention!")

# A while loop iterates while (food_count > 55) and (food_count < 80) is True. In each iteration:

#         String input_key is read from input.
#         Integer food_count is read from input.
#         Click here for example
#         All tests passed.

#         1: Compare output
#         Input
#         Rhubarb
#         65
#         Jackfruit
#         60
#         Roselle
#         17
#         Your output
#         Roselle: needs attention!
#         ############################################################

# The first and second integers in the input are read into variables previous_data and current_data, respectively.
# Write a loop that iterates while current_data is 6 plus previous_data. 
#    In each iteration:

#    Output current_data, followed by " is 6 plus ", previous_data, and ". Sequence is increasing arithmetically." on one line.
#     Assign previous_data with current_data.
#     Read the next integer from input and assign current_data with the integer read.

# After the loop, output the last integer read followed by " breaks the sequence." on one line.

previous_data = int(input())
current_data = int(input())
print(f"Sequence starts at {previous_data}.")

while (current_data == 6 + previous_data):  #loop iterates while current_data is 6 plus previous_data. 
#Output current_data, followed by " is 6 plus ", previous_data, and ". Sequence is increasing arithmetically." on one line.
    print(f"{current_data} is 6 plus {previous_data}. Sequence is increasing arithmetically.")
    previous_data = current_data                   # Assign previous_data with current_data.
    current_data = int(input())   # Read the next integer from input and assign current_data with the integer read.

# After the loop, output the last integer read followed by " breaks the sequence." on one line.
print(f"{current_data} breaks the sequence.") 
    # loop, output the last integer read followed by " breaks the sequence." on one line.

 previous_data = int(input())
current_data = int(input())
print(f"Sequence starts at {previous_data}.")

while (current_data == 6 + previous_data):  
    print(f"{current_data} is 6 plus {previous_data}. Sequence is increasing arithmetically.")
    previous_data = current_data                   
    current_data = int(input())  

print(f"{current_data} breaks the sequence.") 
#### update 