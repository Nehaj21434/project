# 2.Write a program to accept 3 digit number. If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.

# Accpet 3 digit number form the user
num = int(input("Enter the three digit number:"))

First = num // 100
Second = (num // 10) % 10
Third = num % 10

# check Condition
if (First == 2 * Second) and (First == Third / 2):
    print("Yes, you have done it")
else:
    print("Please try next time")
