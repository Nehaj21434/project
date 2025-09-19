# Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 
# b. 1!+ 2! + 3! + 4!+….. + n! 
# c. 1^1 + 2^2 + 3^3+ …… n^n


# a.  1+ 2 + 3 + 4+….. + n 

# function calculate sum of  1+ 2 + 3 + 4+….. + n 

def sum_natural(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

# input
n = int(input("Enter the value of n: "))
print("sum of series(1+2+......+n)",sum_natural(n))
