# WAP to check if no palindrome or not using recursion
def reverse_num(n, rev=0):
# base case when n = 0
    if n  == 0:
        return rev
    # Recrsive case 
    return reverse_num(n // 10, rev * 10 + n % 10)

def is_palindrome(n):
    return n == reverse_num(n)

num = int(input("Enter the number: "))
if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not palindrome.")
