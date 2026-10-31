# Python Program 2: List and Dictionaries 
# Name: Jenny Wolf
# Date: October 29,2026
# Desciption:
#        This program asks the user to enter five items they would pack for at trip.
#        The program stores the items in a list, sorts them alphabetically
#        removes the last item,  adds a new item, 
#        Creates a dictionary from the final list, and displays 
#        each item with its quantity
##########################################################################################

# create an empty list
packing_list = []

# Asks the user to input 5 items
print("Enter 5 items you would pack for a trip (seperate with Enter): " )

# Store these in a list. 
for number, _ in enumerate(range(5), start =1):
    item = input(f"{number}: ").title()
    packing_list.append(item)

# Sort the list alphabetically and print it.
packing_list.sort()
print("\nSorted list:", packing_list)

# Removes the last item from the list and prints the updated list.
packing_list.pop()
print(f"Updated list after removing the last item: {packing_list}")

# Adds a new item to the list and prints the updated list. ( didnt specify if userinput or predefined item)
packing_list.append("Backpack")
print(f"Updated list after adding an item: {packing_list}")

# Creates a dictionary
packing_dict ={}

for item in packing_list:
    packing_dict[item] = 1

# Display dictionary
print("\nPacked items dictionary:", packing_dict)
for item, quantity in packing_dict.items():
    print(f"Item: {item}, Quantity: {quantity}")


#############problems##################
# 1.Problem:
#   . I entered some of the items without capitilazton and realized that sort() isn't 
#       sorting as expected. This occurs because Python compares the ASCII values of charactes,
#       and uppercase and lowercase letters have diffrent values.
#  Fix: 
#       Use .title() when accepting user input. This creates consistent capitalizaton
#       for all enteries, allowing the list to be sorted alphabeically
# 2. problem:

#################Test run:
# Enter 5 items you would pack for a trip (seperate with Enter):
# 1: Tent
# 2: flashlight
# 3: Sleeping bag
# 4: Food
# 5: water
#
# Sorted list: ['Flashlight', 'Food', 'Sleeping Bag', 'Tent', 'Water']
# Updated list after removing the last item: ['Flashlight', 'Food', 'Sleeping Bag', 'Tent']
# Updated list after adding an item: ['Flashlight', 'Food', 'Sleeping Bag', 'Tent', 'Backpack']

# Packed items dictionary: {'Flashlight': 1, 'Food': 1, 'Sleeping Bag': 1, 'Tent': 1, 'Backpack': 1}
# Item: Flashlight, Quantity: 1
# Item: Food, Quantity: 1
# Item: Sleeping Bag, Quantity: 1
# Item: Tent, Quantity: 1
# Item: Backpack, Quantity: 1
# Press any key to continue 