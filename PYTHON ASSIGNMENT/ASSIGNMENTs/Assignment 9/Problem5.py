# Write a program to find factorial using recursion. 


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # recursive call


n = int(input("Enter a number: "))
print("Factorial of ", n, "is: ", factorial)
