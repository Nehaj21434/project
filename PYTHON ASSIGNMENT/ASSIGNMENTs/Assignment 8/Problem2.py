# using the function 
# Write a program to calculate area of circle 


def area_of_circle(radius):
    pi = 3.14
    return pi * radius * radius

# taking input from the user
radius = float(input("Enter the radius of the circle: "))

# calling the function 
area = area_of_circle(radius)

# display result
print("The area of tye circle is:", area)
