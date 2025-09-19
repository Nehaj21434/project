# Write a program to check if given number is Armstrong number or not.  
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  
# 4*4*4*4)
# Program to check Armstrong number

num = int(input("Enter a number: "))

# Step 1: Convert number to string to count digits
order = len(str(num))

# Step 2: Initialize sum
sum_of_powers = 0

# Step 3: Copy the number
temp = num

while temp > 0:
    digit = temp % 10              # get last digit
    sum_of_powers += digit ** order  # add digit raised to 'order'
    temp //= 10                    # remove last digit

# Step 4: Compare result
if sum_of_powers == num:
    print(num, "is an Armstrong number ")
else:
    print(num, "is NOT an Armstrong number ")
