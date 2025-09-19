# Write a program to find print the following Fibonacci series using 
# functions: 
# 1  1  2  3 5 8  n terms

def fibonacci_series(n):
    a, b = 1, 1          # first two terms of fibonacci series
    print(a, b, end=" ")  # print first two terms

    for i in range(3, n+1):   # loop staet feom 3rd term
        c = a + b
        print(c, end=" ")
        a, b = b, c

n = int(input("Enter number of term: "))
fibonacci_series(n)

