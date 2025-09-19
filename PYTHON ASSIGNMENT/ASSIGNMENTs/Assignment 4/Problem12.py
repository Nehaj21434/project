#  WAP to print Armstrong number within a given range.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for i in range(lower, upper + 1):
    num = i
    sum = 0
    while num > 0:
          digit = num % 10
          sum += digit ** 3
          num //= 10
    if sum == i:
        print(i, "is an Armstrong number.")
