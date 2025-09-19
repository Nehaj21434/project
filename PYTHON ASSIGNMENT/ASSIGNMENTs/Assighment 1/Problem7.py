# 7. Program to Find the Roots of a Quadratic Equation

# This program calculates the root of quadratic equation
#  based on the coefficients a, b, and c.
a = int(input("Enter the cofficient A:"))
b = int(input("Enter the cofficient B:"))
c = int(input("Enter the cofficient C:"))

ans = b * b - 4 * a * c
ans = ans ** 0.5
root1 = (-b + ans) / (2 * a)
root2 = (-b - ans) / (2 * a)
print(f"The roots of quadratic equation are {root1} and {root2}")
