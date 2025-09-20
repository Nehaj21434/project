# Write a Python program to remove the intersection of a second set with a first set.


#Take input for first set
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

# Remove elements from first set that are in second set
result_set = []
for elem in set1:
    if elem not in set2:
        result_set.append(elem)

#  Print results
print("First Set:", set1)
print("Second Set:", set2)
print("First Set after removing intersection with second set:", result_set)
