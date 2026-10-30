# Project name: Python Project 3 Part 1: Strings
# Name :Jenny Wolf 
# Due date : 1 Nov 2026
#
# This program: 
#  1. prompts the user to enter a sentence.
#  2. Performs the following string operations:
#     - Displays the first 5 characters of the sentence
#     - Converts the sentence to lowercase
#     - Replaces all spaces with underscores(_).
#     - Splits the sentence into a list of words.
#     _ Joins the words back into a single string usng hypens(-)
#######################################################################


# user input ask for input sentence and output 
user_sentence= input("Enter a sentence: ")

# slice first 5 [char] of the string  and print
print(f"First 5  characters: { user_sentence[:5]}")

# Convets string  to lowercase prints result
print(f"Lowercase version: {user_sentence.lower()}")

# replaces all spaces with usnderscores (_) and prints the results
print(f"Spaces replaced with underscores: {user_sentence.replace(' ','_')}")

# Splits the [string into a list] of words and prints the list.
# create a new variable since list are mutable
words = user_sentence.split()

print(f"List of words: {words}")

# Join the list of words back to a single string, separated by hyphens (-), and prints it
print(f"Hyphen-joined string: {'-'.join(words)}")














########################problems/notes ###################################################
#problems:
#    1. confusing String methods and List methods
#   # strings are  imutable -> methods dont return a new string
#   # Lists -> Mutable->  many methonds modify the list directly
#     which is why sentence.replace(" ",("-"))  
#     split() turns a users sentence into a list: -- > better for strng not a list