# -----------------------------------------------------------
# Name: Jenny Wolf
# Course: CSC 1019 - Introduction to Python Programming
# Assignment: Inheritance - Libro and Encyclopedia
#  13.10 LAB: Libro information (overriding member methods)
# Date: 06 Nov 2026
#
# Description:
#   This program demonstrates inheritance in Python.
#   The Libro class serves as the base class and contains
#   attributes for a book's title, author, publisher, and
#   publication date, along with a method to display that
#   information.
#
#    The Encyclopedia class is derived from the Libro class.
#    It inherits the Libro attributes and methods while adding
#   its own attributes for edition and number of pages.
#
#    The Encyclopedia class also overrides the print_info()
#    method to display both the inherited Libro information
#    and Encyclopedia-specific information.
#
# The program creates and displays information for both
# a Libro object and an Encyclopedia object.
# -----------------------------------------------------------

class Libro:    # base class
     #constructor to intialize libro attributes
    def __init__(self, title, author, publisher, publication_date):
        #attributes
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
      # Method to display libro informaton
    def print_info(self):
        print("Libro Information:")
        print(f"   Libro Title: {self.title}")
        print(f"   Author: {self.author}")
        print(f"   Publisher: {self.publisher}")
        print(f"   Publication Date: {self.publication_date}")
#Devrided class that inherits from Libro
class Encyclopedia(Libro):
     #constructor initalizes inherited attributes
     #and adds Encyclopedia specific attributres
    def __init__(self, title, author, publisher, publication_date, edition,
                 num_pages):
        #Call the Libro Class constructor
        Libro. __init__(self, title, author, publisher, publication_date)
        #New attributes for Encyclopedia
        self.edition = edition
        self.num_pages = num_pages
     #overrides the print_info() method from Libro
    def print_info(self):
        #Call base class Method 
        Libro.print_info(self)
        #Display Encyclopedia- specific attributes
        print(f"   Edition: {self.edition}")
        print(f"   Number of Pages: {self.num_pages}")

if __name__ == "__main__":
    #Get input values for the Libro object
    title = input()
    author = input()
    publisher = input()
    publication_date = input()
    #Get input values for the Encyclopedia object
    e_title = input()
    e_author = input()
    e_publisher = input()
    e_publication_date = input()
    edition = input()
    num_pages = int(input())  #convert page to an int
    #Create a Libro object and display its info
    my_libro = Libro(title, author, publisher, publication_date)
    my_libro.print_info()
    #Create an Encyclopedia object and display its info
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher,
                                   e_publication_date, edition, num_pages)
    my_encyclopedia.print_info()











# TEST RUN ---------------------------------------------------------
# The Hobbit
# J. R. R. Tolkien
# George Allen & Unwin
# 21 September 1937
# The Illustrated Encyclopedia of the Universe
# Ian Ridpath
# Watson-Guptill
# 2001
# 2nd
# 84


# OUTPUT
# Libro Information:
#    Libro Title: The Hobbit
#    Author: J. R. R. Tolkien
#    Publisher: George Allen & Unwin
#    Publication Date: 21 September 1937
# Libro Information:
#    Libro Title: The Illustrated Encyclopedia of the Universe
#    Author: Ian Ridpath
#    Publisher: Watson-Guptill
#    Publication Date: 2001
#    Edition: 2nd
#    Number of Pages: 84
# Press any key to continue . . .