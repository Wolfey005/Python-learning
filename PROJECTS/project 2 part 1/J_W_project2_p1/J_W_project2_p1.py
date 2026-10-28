# Name: Jennifer Wolf                                                         #
# project name: Project 2 part 1                                              #
# Project due date: Oct 20th 2026                                             #
# Project description:                                                        #
#     Part 1 of project 2 focus on use of branching                           #
#     It  asks user to input a number in order for  program                   #
#     to determine if:                                                        #
#            1. number is positive negative or zero                           #
#               2. number is even or odd                                      #
#     Program  ends with a print statement that displays the                  #
#     appropriate message for each case.                                      #
#                                                                             #
###############################################################################

# Ask the user to input a number. 
user_num = int(input("Enter a number: "))
# Checks if the number is:o Positive, negative, or zero
if user_num > 0:          # any number greater than  0 is positive
    sign = "positive"      # outputs positive
elif user_num < 0:        # number less than zero is negative
    sign = "negative"      # outputs negative
else:
    sign = "zero"
# checks if even or odd 
if user_num % 2 == 0:      
    odd_even = "even"      # %2 =+ 0 -> even
else:
      odd_even = "odd"     # %2 != 0 -> odd
 
# Print appropriate messages for each case.  
print(f"The number {user_num} is {sign}. The\nnumber {user_num} is {odd_even}.") 



###############################-Problems-#######################################
# 1. spelled input incorrectly --fixed : input not intput
# 2. forgot to earse psudeo code number  fix: changed to user_num
# 3. wrote num_user instead of user_num  fix: change to user_num
# 4. didnt include a chioce for a sign for zero added as an else 
# 5. incorrect newline was /n instead of \n
# 6.
## branching- decison making if, if/else, if/elif/else
# Loops-  iterations- while       for

# formating in instructions show that the print statment might be on one 
#   statement and a new line \n starts after the 2nd "The" 
#    please do not reduce points for such , i am following instructions as shown.
#  
#   tested :
# # # 0 : 
# #    output : Enter a number : 0
#  The number 0 is zero. The
#  number 0 is even.
#
# pos / even
# output :
#
# Enter a number : 2
# The number 2 is positive. The
# number 2 is even.
#
# pos/odd
# output :
#
# Enter a number : 333
# The number 333 is positive. The
# number 333 is odd.
#
# neg/ even:
# output:
# Enter a number : -10
# The number -10 is negative. The
# number -10 is even.

#  neg/ odd :
# # output:
# Enter a number : -99
# The number -99 is negative. The
# number -99 is odd.
# #  