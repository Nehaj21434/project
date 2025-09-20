# Python Program to Put Even and Odd elements of a List into two Different Lists


#  Take input for list size
n = int(input("Enter number of elements in the list: "))

#  Create the original list
numbers = []
for i in range(n):
    element = int(input(f"Enter element: "))
    numbers.append(element)

#  Create empty lists for even and odd numbers
even_list = []
odd_list = []

#  Separate even and odd elements
for value in numbers:
    if value % 2 == 0:   # even condition
        even_list.append(value)
    else:                # odd condition
        odd_list.append(value)

# Print results
print("Original List:", numbers)
print("Even Elements List:", even_list)
print("Odd Elements List:", odd_list)
