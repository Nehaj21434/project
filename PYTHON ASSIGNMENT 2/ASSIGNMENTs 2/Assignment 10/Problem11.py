# Write a program to print all numbers which are divisible by m and n in the list



# Step 1: Take input for list size
size = int(input("Enter number of elements in the list: "))

# Step 2: Create the list
numbers = []
for i in range(size):
    element = int(input(f"Enter element: "))
    numbers.append(element)

# Step 3: Take input for m and n
m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

# Step 4: Check divisibility and print results
print(f"Numbers divisible by {m} and {n} are:")
for value in numbers:
    if value % m == 0 and value % n == 0:
        print(value)
