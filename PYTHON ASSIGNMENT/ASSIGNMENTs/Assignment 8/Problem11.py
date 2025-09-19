#  WAP to check if a given number is Armstrong number or not. For 
# each task create separate functions.

# Function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

# Function to calculate power (without using ** or pow())
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# Function to check Armstrong number
def is_armstrong(num):
    digits = count_digits(num)   # Find number of digits
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += power(digit, digits)   # Raise digit to power of digits
        temp //= 10
    return total == num

# Main program
n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong number.")
else:
    print(n, "is NOT an Armstrong number.")
