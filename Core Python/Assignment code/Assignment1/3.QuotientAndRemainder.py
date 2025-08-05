"""
Q3 Program to find quotient and remainder of two numbers.
"""
# This program calculates the quotient and remainder of two numbers.
# Ask the user to ente two numbers.

number1 = int(input("Enter the dividend(number to divide):"))
number2 = int(input("Enter the divisor(number to divide by):"))

# calculate the quotient.
quotient = number1 // number2

# calculate the remainder.
ramainder = number1 % number2

# print the quotient and remainder.
print("Quotient is", quotient)
print("Remainder is", ramainder)
