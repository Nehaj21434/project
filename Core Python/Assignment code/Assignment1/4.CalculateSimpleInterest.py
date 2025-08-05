"""
Q4  Write a program to enter P, T,R and calculate simple interest.
"""
# This program calculates the simple interest based on the principal amount (p), time (t), rate (r).
# input value for user.
P = float(input("Enter the principal amount (P):"))
T = float(input("Enter the time in year (T):"))
R = float(input("Enter the rate of interest (R):"))
# calculate the simple interest using the formula SI = (P * T * R)
SI = (P * T * R) / 100
# print the simple interest.
print("simple interest is", SI)
# shoe the result.
