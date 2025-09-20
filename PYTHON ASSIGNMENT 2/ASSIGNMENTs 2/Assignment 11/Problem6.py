#  Program to find the union of two lists

# Take first list input
n1 = int(input("Enter number of elements in first list: "))
list1 = []
for i in range(n1):
    element = int(input(f"Enter element of first list: "))
    list1.append(element)

# Take second list input
n2 = int(input("Enter number of elements in second list: "))
list2 = []
for i in range(n2):
    element = int(input(f"Enter element of second list: "))
    list2.append(element)

# Create union list manually
union_list = list1[:]  # copy all elements of first list

for value in list2:
    if value not in union_list:   # add only if not already present
        union_list.append(value)

# Print results
print("First List:", list1)
print("Second List:", list2)
print("Union of both lists:", union_list)
