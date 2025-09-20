# Write a program to print Fibonacci series using recursion.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:   # base care 
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

n = int(input("Enter the numner of trem: "))

print("Fibonacci Series: ")
for i in range(n):
    print(fib(i), end=" ")
