#  10.Write a program to reverse three-digit number.

# Program to reverse a three-digit number

# Input from user
number = int(input("Enter a three-digit number: "))

# Check if it's a valid three-digit number
if 100 <= number <= 999:
    # Extract digits
    last_digit = number % 10
    middle_digit = (number // 10) % 10
    first_digit = number // 100

    # Reverse the number
    reversed_number = (last_digit * 100) + (middle_digit * 10) + first_digit

    # Display result
    print(f"Reversed number: {reversed_number}")
else:
    print("Please enter a valid three-digit number.")
