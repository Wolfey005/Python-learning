#Python Program 3: Data Types and Conversions 
#Write a program that: 
#• Asks the user for a short sentence or phrase. 
short_sentence = input("Enter a short sentence or phrase: ")

#Performs the following operations and print the results: 
#a. Convert the sentence to uppercase. 
print("The sentence in uppercase:", short_sentence.upper())

#b. Count and print the number of characters in the sentence 
print("The number of characters in the sentence:", len(short_sentence))

#c/d  Convrt the sentence into a list of words (split by spaces  , print them
print(f"The sentence as a list of words:", short_sentence.split())
