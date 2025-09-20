# Write a program to find sum of n numbers using recursion.

# Recursive function to find sum of first n numbers
def sum_n(n):
    if n == 1:          # base case
        return 1
    else:
        return n + sum_n(n - 1)


n = int(input("Enter n: "))
result = sum_n(n)
print("Sum of first", n, "numbers is:", result)
