# 1 Write a program to find sum of following series using recursive functions:  
# i. 1! + 2!  + 3! + 4! +….. + n!  
# Note : For fact and sum two recursive functions

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    

def sum_series(n):
    if n == 1:
        return fact(1)
    else:
        return fact(n) + sum_series(n - 1)
    

n = int(input("Enter the value of n: "))

result = sum_series(n)
print("Sum of series 1! + 2! +.........+", n, "! =", result)
