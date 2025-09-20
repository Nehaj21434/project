# Write a program to create a duplicate of an existing list. It should not point to 
# same list.

n = int(input("Enter the number of element in the list: "))
original_list = []
for i in range(n):
    element = int(input("Enter the element: "))
    original_list.append(element)


duplicate_list = []
for value in original_list:
    duplicate_list.append(value)

print("Original element list", original_list)
print("Duplicates element list", duplicate_list)

print("both memory pointing to same element", original_list is duplicate_list)
