# WAP to print all numbers in a range divisible by a given number.
n = int(input("Enter the range limit: "))
division = int(input("Enter the number to check divisibility:"))
for i in range(1, n + 1):
    if i % division == 0:
        print(i, end=" ")
