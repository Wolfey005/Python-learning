# Given class Triangle, complete the program to read and set the base and height of triangle1 and triangle2,
#  determine which triangle's area is smaller, and output the smaller triangle's info, 
#  making use of Triangle's relevant methods.

# Ex: If the input is:

# 3.0
# 4.0
# 4.0
# 5.0
# where 3.0 is triangle1's base, 4.0 is triangle1's height, 4.0 is triangle2's base, and 5.0 is triangle2's height, the output is:

# Triangle with smaller area:
# Base: 3.00
# Height: 4.00
# Area: 6.00

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