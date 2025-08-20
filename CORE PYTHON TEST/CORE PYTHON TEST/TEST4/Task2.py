# Write a program to find factorial of given number using recursion

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Input from user
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))
