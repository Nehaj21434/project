# Write a program to find sum of digits of a number. 


# Function to calculate sum of digits
def sum_of_digits(num):
    total = 0
    while num > 0:          # Repeat until number becomes 0
        digit = num % 10    # Get last digit
        total += digit      # Add digit to sum
        num //= 10          # Remove last digit
    return total


n = int(input("Enter a number: "))
print("Sum of digits of", n, "is:", sum_of_digits(n))
