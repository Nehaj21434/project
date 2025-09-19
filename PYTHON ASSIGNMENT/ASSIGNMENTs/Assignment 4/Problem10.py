# WAP to check if given number is Perfect Number.
num = int(input("Enter a number:  "))
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors +=i


# check condition
if sum_of_divisors == num:
    print(num, "Perfect Number")
else:
    print(num, "Not Perfect Number")
