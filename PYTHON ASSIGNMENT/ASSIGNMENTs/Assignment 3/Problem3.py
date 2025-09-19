# 3 Write a program to input angles of a triangle and check whether
# the triangle is valid or not.
angle1 = int(input("Enter first angle:"))
angle2 = int(input("Enter second angle:"))
angle3 = int(input("Enter third angle:"))
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
