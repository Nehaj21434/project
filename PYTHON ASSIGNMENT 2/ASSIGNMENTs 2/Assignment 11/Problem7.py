# Python Program to Find the Intersection of Two Lists 



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

#  Find intersection manually
intersection_list = []
for value in list1:
    if value in list2 and value not in intersection_list:  # common and avoid duplicates
        intersection_list.append(value)

# Print results
print("First List:", list1)
print("Second List:", list2)
print("Intersection of both lists:", intersection_list)
