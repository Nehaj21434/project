# Using function
# Write a program to calculate area of rectangle

def area_of_rectangle(length, width):
    return length * width

# Taking the input from the user

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the recatangle: "))

# calling thhe function 
area = area_of_rectangle(length, width)

# display result
print("The area of the rectange is : ", area)
