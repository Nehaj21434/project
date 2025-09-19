# 7.Find the sum of three-digit number.

num = float(input("Enter the three-digit number:"))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

sum_digit = num + digit1 + digit2 + digit3

print(f"sum of digit: {sum_digit}")
