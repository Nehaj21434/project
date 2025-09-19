# WAP to check if given number Strong Number.
# Program to check Strong Number

num = int(input("Enter a number: "))
temp = num   # store original number
sum_fact = 0

while temp > 0:
    digit = temp % 10   # get last digit

    # calculate factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum_fact = sum_fact + fact
    temp = temp // 10   # remove last digit

# check condition
if sum_fact == num:
    print(num, "is a Strong Number.")
else:
    print(num, "is NOT a Strong Number.")
