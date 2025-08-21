# Write a program to print prime numbers between 1 to 100.

print("Print number between 1 to 100 are: ")

for num in range(2, 101):  # start form 2 bec 1 is not a prime number.
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):  # check divisibility up to sqrt(num).
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
