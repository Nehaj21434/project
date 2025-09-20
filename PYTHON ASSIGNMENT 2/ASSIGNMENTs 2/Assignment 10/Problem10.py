# Write a program to remove all occurrences of a given element in the list. 
# Program to remove all occurrences of a given element in the list

# Step 1: Take input for list size
n = int(input("Enter number of elements in the list: "))

# Step 2: Create the original list
my_list = []
for i in range(n):
    element = int(input(f"Enter element: "))
    my_list.append(element)

# Step 3: Take the element to remove
remove_item = int(input("Enter the element to remove: "))

# Step 4: Create a new list excluding that element
new_list = []
for value in my_list:
    if value != remove_item:   # keep only values not equal to remove_item
        new_list.append(value)

# Step 5: Print result
print("Original List:", my_list)
print(f"List after removing all occurrences of {remove_item}:", new_list)

