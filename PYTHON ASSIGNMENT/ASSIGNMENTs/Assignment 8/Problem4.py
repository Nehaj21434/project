# Sum of all odd numbers between 1 to n  


def sum_of_odds(n):
    total = 0
    for i in range(1, n+1, 2):  # only odd number
        total += i
    return total

# input
n = int(input("Enter value of n: "))

# calling function
print("sum of odd number from 1 to", n, "is:",sum_of_odds(n))
