# Write a program to check if entered number is a palindrome or 
# not.

# Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10          # Get last digit
        rev = rev * 10 + digit    # Add to reverse
        num //= 10                # Remove last digit
    return rev

# Function to check palindrome
def is_palindrome(num):
    return num == reverse_number(num)   # Compare original and reversed

# Main program
n = int(input("Enter a number: "))

if is_palindrome(n):
    print(n, "is a Palindrome number.")
else:
    print(n, "is NOT a Palindrome number.")
