# Write a program to check whether the triangle is equilateral, isosceles
# or scalene triangle.
side1 = int(input("Enter first side:"))
side2 = int(input("Enter second side:"))
side3 = int(input("Enter third side:"))
if side1 == side2 and side2 == side3:  
    print("The triangle is equilateral.")
if side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
