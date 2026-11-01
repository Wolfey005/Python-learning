# Python Program 3: Classes 
# Name: Jenny Wolf
# Date: October 31,2026
# Desciption:
#        This program demonstrtates the use of classes and objects in Python.
#        The TripItem class stores information about items needed for a trip
#            including the items name and quantity
#        The user creates three tripItem objects entering item names and quantities
#        The objects are stored in a list, and the program iterates through the list 
#           to display formatted packing list using the describe() method of each object.
#        
##########################################################################################

class TripItem:
 # Constutor to initialize attributes name(string) and quantity(integer)
    def __init__(self, name,quantity):
        self.name = name        
        self.quantity = quantity

# Method descrtibe() that prints Item[name], Quantity[quantity]
    def describe(self):
        print(f"Item: {self.name}, Quantity: {self.quantity} ")

# Store ojects in a list
packing_list = []

# store the strings for first,second,third in a list to use for the input prompts
item_order = ["first", "second", "third"]

# Ask the user to create 3 TripItem objects entering name and quantity for each
for i in range(3):
    input_name = input(f"Enter the name of the {item_order[i]} item: ")
    input_quantity = int(input(f"Enter the quantity for {input_name}: "))
    print() 
    #create a TripItem object
    trip_item = TripItem(input_name, input_quantity)
    # store the oject in a list
    packing_list.append(trip_item)
print("Packing List:")

# Iterate through the list of TripItem objects and call the describe() method for each object
for item in packing_list:
    item.describe()














##################problems and fixes#################
# 1.test printed numerical values for item  instead of the string vaues for first, second, third
#   fix: I changed the input prompt to use a list of strings and indexing to get the correct string for first , second ,thrid
# 