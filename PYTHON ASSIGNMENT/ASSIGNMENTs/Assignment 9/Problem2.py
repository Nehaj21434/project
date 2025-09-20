# Write a program to check if given number is Armstrong or not using recursive 
# function. 

# Recursive function to calculate sum of powers of digits
def armstrong_sum(num, power):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return (digit ** power) + armstrong_sum(num // 10, power)

# Function to check Armstrong number
def is_armstrong(num):
    # Count digits
    power = len(str(num))
    return num == armstrong_sum(num, power)

# Driver code
n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is NOT an Armstrong number")
