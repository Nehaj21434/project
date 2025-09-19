# 1^1 + 2^2 + 3^3+ …… n^n
# Function to calculate power (without using pow() or **)
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Function to calculate sum of series
def sum_powers(n):
    total = 0
    for i in range(1, n+1):
        total += power(i, i)   # i^i
    return total

# Input
n = int(input("Enter value of n: "))
print("Sum of series (1^1+2^2+...+n^n):", sum_powers(n))
