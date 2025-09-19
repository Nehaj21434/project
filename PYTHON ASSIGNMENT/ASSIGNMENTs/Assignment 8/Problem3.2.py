# 1! + 2! + 3! + … + n!

# function to calulate facto
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
# function to calculates sum of facto
def sum_factorial(n):
    total = 0
    for i in range(1, n+1):
        total += factorial(i)
    return total


# input
n = int(input("Enter value of n: "))
print("sum of series (1!+2!+...+n!):", sum_factorial(n))
