# Write a Python program to find elements in a given set that are not in another set. 


#  Take input for first set
n1 = int(input("Enter number of elements in first set: "))
set1 = []
for i in range(n1):
    element = int(input("Enter element of first set: "))
    set1.append(element)

# Take input for second set
n2 = int(input("Enter number of elements in second set: "))
set2 = []
for i in range(n2):
    element = int(input("Enter element of second set: "))
    set2.append(element)

# Find elements in set1 that are not in set2
difference_set = []
for elem in set1:
    if elem not in set2:
        difference_set.append(elem)

# Print results
print("First Set:", set1)
print("Second Set:", set2)
print("Elements in first set but not in second set:", difference_set)
