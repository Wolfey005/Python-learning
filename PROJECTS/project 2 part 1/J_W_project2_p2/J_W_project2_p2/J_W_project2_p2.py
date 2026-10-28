# Name: Jennifer Wolf                                                         #
# project name: Project 2 part 2                                              #
# Project due date: Oct 20th 2026                                             #
# Project description:                                                        #
#     Part 2 of project 2 focus on use of Loops: for & while                  #
#     It asks user to input a  positive number                                #
#     uses for loop to print all numbers in range 1 to n                      #
#     while loop is used to calculate and print the sum of numbers in         #
#     indicated range                                                         #
#                                                                             #
###############################################################################

n  = int(input("Enter a positive integer: "))    # asks for user input
print(f"Numbers from 1 to {n} are: ")

for n in range(1, n +1):
    print(n)
#calculate the sum from 1 to n
sum = 0
i = 1

# while loop to add each number 1 through n
while i <= n:
    sum += i         # add current value of i to running total
    i += 1           # increase i by 1 for next loop iteration
#print the final sum
print(f"The sum of numbers from 1 to {n} is {sum}.")





