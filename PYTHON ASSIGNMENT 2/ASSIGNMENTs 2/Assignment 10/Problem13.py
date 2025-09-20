#  Write a program to print list after removing even numbers.


#  Take input for list size
n = int(input("Enter number of elements in the list: "))

# Create the original list
numbers = []
for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)

#  Create a new list with only odd numbers
odd_list = []
for value in numbers:
    if value % 2 != 0:   # keep only odd numbers
        odd_list.append(value)

# Print results
print("Original List:", numbers)
print("List after removing even numbers:", odd_list)
