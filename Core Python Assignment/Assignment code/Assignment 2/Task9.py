# 9. Write a program to swap two numbers without using third variable.
a = int(input("Enter the first number(A)"))
b = int(input("Enete the second number (B)"))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping logic
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
