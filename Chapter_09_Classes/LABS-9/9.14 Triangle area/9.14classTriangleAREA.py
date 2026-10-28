# """
# Triangle Area Comparison
# Author: Jenny Wolf

# This program creates two Triangle objects, calculates
# their areas using object-oriented programming principles,
# and displays the triangle with the smaller area.
# """


class Triangle:

    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
        
    def print_info(self):
        print(f"Base: {self.base:.2f}")
        print(f"Height: {self.height:.2f}")
        print(f"Area: {self.get_area():.2f}")

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()
    print("Triangle area Comparison Program")
    print("-" * 32)

    print("Enter Triangle 1 information:")
    # Read and set base and height for triangle1
    triangle1.set_base(float(input("Base: ")))
    triangle1.set_height(float(input("Height: ")))

    print(" ")
    print("Enter Triangle 2 information:")
    # Read and set base and height for triangle2
    triangle2.set_base(float(input("Base: ")))
    triangle2.set_height(float(input("Height: ")))

    print(" ")
    print("Triangle with smaller area:")
    # Determine smaller triangle and output smaller triangle's info
    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info()


# #######################------test--------################
# Triangle area Comparison Program
# --------------------------------
# Enter Triangle 1 information:
# Base: 5.0
# Height: 2.0

# Enter Triangle 2 information:
# Base: 1.0
# Height: 8.0

# Triangle with smaller area:
# Base: 1.00
# Height: 8.00
# Area: 4.00
# Press any key to continue . . .