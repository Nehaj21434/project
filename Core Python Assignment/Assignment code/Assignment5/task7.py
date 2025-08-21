# Write a program to print first n prime numbers.
# Program to print first n prime numbers

n = int(input("Enter how many prime numbers you want: "))

count = 0       # how many primes printed so far
num = 2         # start checking from 2

print(f"First {n} prime numbers are:")

while count < n:
    # check if num is prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1   # increase count of primes found

    num += 1   # check next number
