# Write a program that first reads in the name of an input file and 
# then reads the file using the csv.reader() method. 
# The file contains a list of words separated by commas.
#  The program must output the words and their frequencies (the number of times each word appears in the file) without any duplicates.

# Ex: If the input is:

# input1.csv
# and the contents of input1.csv are:

# hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# the output is:

# hello - 1
# cat - 2
# man - 2
# hey - 2
# dog - 2
# boy - 2
# Hello - 1
# woman - 1
# Cat - 1

# Notes: Output words in order of first occurrence in input and end output with a newline. File input1.csv is available to download.
##############################################################################################################################################
import csv
# Write a program that first reads in the name of an input file and 
with open("grades.csv", "r") as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=",")

    row_num = 1
    for row in grades_reader:
        print(f"Row #{row_num}: {row}")
        row_num += 1
# then reads the file using the csv.reader() method. 

# The file contains a list of words separated by commas.

#  The program must output the words and their frequencies (the number of times each word appears in the file) without any duplicates.