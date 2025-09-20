# Write a program to create three lists of numbers, their squares and cubes

# Take input for list size
n = int(input("Enter number of elements: "))

#  Create the numbers list
numbers = []
for i in range(n):
    element = int(input(f"Enter element: "))
    numbers.append(element)

#  Create squares and cubes lists
squares = []
cubes = []

for value in numbers:
    squares.append(value * value)       # square
    cubes.append(value * value * value) # cube

#  Print results
print("Numbers List :", numbers)
print("Squares List :", squares)
print("Cubes List   :", cubes)
