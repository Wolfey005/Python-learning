# name: Jenny Wolf
# date " 28- oct - 2026
# project: program that reads intergers from input 
# each integer represents a signal recived by an antenna 
# when a signal is idenified to be above 130, 
#      it is repalced with 130
#   ---------promt :
#  List signals_list contains integers read from input. 
#  Each integer represents a signal received by an antenna. 
#  Write a loop to update all elements greater than 130 in signals_list with 130.

##############################################################

signals_list = []

tokens = input("Enter a range of antenna signals:").split()

#tokens = input().split()   # split() breaks when spaces are found

for token in tokens:       # right now the input is read as strings//  tokens = ['143', '128', '117',' 168']  each one is a pass through the loop
    signals_list.append(int(token))   #  converted to ineger usng int(token)  '143' --> 142 //  Add the integer to list ---> signals_list.append(int(token()))

print("Original signals:", end=" ")
for signal in signals_list:    # now that the strings are converted to integers , go through each item in list one at a time
    print(signal, end=" ")     # print the values with a space at the end 
print()

for pos in range(len(signals_list)):   #pos is postion
    if signals_list[pos] >  130:  #checks if signal is greater than 130
        signals_list[pos] = 130   # changes it to 130

print("Calibrated signals:", end=" ")   # goes through each value one at a time
for signal in signals_list
    print(signal, end=" ")           # prints each signal followed by a space after caliberatoin
print()

########################problems/testing################################
# problems:
#     1.kepted missspelling signals_list
#     2.Didnt understnad what pos ment == 
#       A:its positon , same as index just a diffrent name is used
#     3.print statements was output muliple times one with the list and the other two with out list
#        A:accidentally put print original signals  print statement inside of loop and the -- moved to outside loop
#
#---- test-----
# Enter a range of antenna signals:143 128 117 168
# Original signals: 143 128 117 168
# Calibrated signals: 130 128 117 130
# Press any key to continue . . .
