# 8.Write a program to swap two numbers using third variable.
A = int(input("Enter the First number:"))
B = int(input("Enter the second number:"))

# Swapping using third variable
temp = A
A = B
B = temp

print("After swapping")
print("Value of A =", A)
print("Value of B =", B)
