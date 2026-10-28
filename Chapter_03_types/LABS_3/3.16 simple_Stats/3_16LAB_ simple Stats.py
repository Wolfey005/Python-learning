#Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers.

#Output each rounded integer using the following:
#print(f"{your_value:.0f}")

#Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
#print(f"{your_value:.3f}")


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
# average and product formulas (int)
pro_duct= num1 * num2 * num3 * num4 
average = (num1 + num2 + num3 + num4)/4 

# product and average as int
print(f"{pro_duct:.0f} {average:.0f}")

#product and average as float

# product and average as float point (one print statement = same line)
print(f"{pro_duct:.3f} {average:.3f}")

#problems
# converting to int too earlry - fixed
# was calculating average in correctly , accidentally used * instead of *- fixed
#formating was bad, moved  formulas together and  combined floats into own
# print statement and ints into own print statement