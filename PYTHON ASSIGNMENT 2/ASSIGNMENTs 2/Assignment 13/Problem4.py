# Python Program to Generate a Dictionary that Contains Numbers (between 1 
# and n) in the Form (x,x*x). 

# Input the value of n
n = int(input("Enter a number n: "))

#  Create an empty dictionary
squares_dict = {}

#  Fill the dictionary with x:x*x
for x in range(1, n + 1):
    squares_dict[x] = x * x

# Print the dictionary
print("Dictionary of numbers and their squares:", squares_dict)
