# Program to merge two lists and sort it

#  Take first list input
n1 = int(input("Enter number of elements in first list: "))
list1 = []
for i in range(n1):
    element = int(input("Enter element of first list: "))
    list1.append(element)

# Take second list input
n2 = int(input("Enter number of elements in second list: "))
list2 = []
for i in range(n2):
    element = int(input("Enter element of second list: "))
    list2.append(element)

#  Merge two lists
merged_list = list1 + list2

#  Sort the merged list manually (Bubble Sort for simplicity)
for i in range(len(merged_list)):
    for j in range(i + 1, len(merged_list)):
        if merged_list[i] > merged_list[j]:
            # swap
            merged_list[i], merged_list[j] = merged_list[j], merged_list[i]

#  Print results
print("First List:", list1)
print("Second List:", list2)
print("Merged and Sorted List:", merged_list)
