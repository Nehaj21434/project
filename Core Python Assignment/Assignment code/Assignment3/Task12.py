# Write a program to check if given 3 digit number is a palindrome or not.


num = int(input("Enter a 3-digit number: "))

# Check if it's a valid 3-digit number
if num < 100 or num > 999:
    print("Please enter a valid 3-digit number.")
else:
    # Store original number
    original = num

    # Reverse the number
    last = num % 10
    num = num // 10

    middle = num % 10
    first = num // 10

    reversed_num = last * 100 + middle * 10 + first

    # Check if it's a palindrome
    if original == reversed_num:
        print(original, "is a palindrome.")
    else:
        print(original, "is not a palindrome.")
