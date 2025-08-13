# write a program to calculate the sum of following series where  is input by the user
#  1/1! + 2/2! + 3/3! + ... + n/n!

n =  int(input("Enter the value of n:"))
sum_series = 0.0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    sum_series += 1 * i / factorial

print(f'The sum of the series is: {sum_series}')
