# Write a program find reverse of a number 

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


n = int(input("Enter a number: "))
print("reverse Of", n, "is:",reverse_number(n))
