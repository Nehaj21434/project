# Write a program to print first n prime numbers.

n = int(input("Enter the number of prime numbers to print:"))

count = 0   # to count the number of prime numbers found
num = 2      # Start checking for prime numbers from 2

while count < n:
    is_prime = True    # Assume the number is prime.
    for i in range(2, num):      # check divisibility from 2 to num-1
        if num % i == 0:  # If num is divisible by any number,
            # it is not prime
            is_prime = False    # check failed so set is_prime to false
            break      # exit the loop early if not prime.

    if is_prime:  # If the number is still prime.
        print(num, end=' ')
        count += 1
    num += 1
