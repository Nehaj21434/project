# Write a program to reverse a given number using recursive function.


# Recursive function to count digits
def count_digits(num):
    if num == 0:
        return 0
    return 1 + count_digits(num // 10)

# Recursive function to reverse number
def reverse_num(num, digits):
    if num == 0:
        return 0
    last_digit = num % 10
    return (last_digit * (10 ** (digits - 1))) + reverse_num(num // 10, digits - 1)


n = int(input("Enter a number: "))
digits = count_digits(n)
rev = reverse_num(n, digits)
print("Reversed number:", rev)
