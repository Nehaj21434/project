# 6.Write a Program to input two angles from user and find third angle of the
# triangle.
# This program to calculates the third angle of,
# a triangle based on the first two angles.
# ask the user to enter the first two angles.

angle1 = float(input("Enter the first angle of the triangle:"))
angle2 = float(input("Enter the second angle of the triangle:"))

# calculate the third angle using formula :
# thirdangle = 180 - (angle1 + angle2)
thirdAngle = 180 - (angle1 + angle2)
# output of third angle.
print("The third angle of the triangle is", thirdAngle)
# result display.