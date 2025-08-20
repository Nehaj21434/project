# WAP to check if a given number is prime number or not.
n = int(input("Enter a number: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
        else:
            is_prime = True

if is_prime:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")
