# 4. WAP to calculate area of triangle and rectangle.

# Input of Rectangle.
Length = float(input("Enter a length of rectangle:"))
Breadth = float(input("Enter a Breadth of rectangle:"))

# calculate area of rectangle.
area_of_rectangle = Length * Breadth

# Input of Triangle.
base = float(input("Enter base of triangle:"))
heigth = float(input("Enter heigth of triangle:"))

# Calulate area of triangle
area_of_triangle = 1/2 * base * heigth

# Display output.
print("Area of rectangle:", area_of_rectangle)
print("Area of Triangle:", area_of_triangle)
