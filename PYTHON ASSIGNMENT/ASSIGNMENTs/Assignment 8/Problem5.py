# Sum of all prime numbers between 1 to n 


# fuction to check if number is prime
def is_prime(num):
    if num < 2:   # prime number are greater then 1
        return False
    for i in range(2, num):  # check divisibility from 2 to num-1
        if num % i == 0:          # if divisible, then not prime
            return False
    return True                # if no divisors found its prime


# function to find sum of all prime numnber from 1 to n
def sum_of_prime(n):
    total = 0            # variable to store sum
    for i in range(2, n+1):            # loop from 2 to n 
        if is_prime(i):            # check if i is prime
            total +=1                 # if prime add  to total
        return total               # return final sum

n = int(input("Enter value of n: "))
print("sum of all prime number between 1 and", n, "is", sum_of_prime(n))
