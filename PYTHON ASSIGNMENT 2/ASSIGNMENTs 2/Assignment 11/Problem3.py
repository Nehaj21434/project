# Python Program to Sort the List According to the Second Element in Sublist 
# Take input for number of sublists
n = int(input("Enter number of sublists: "))

#  Take input for each sublist
my_list = []
for i in range(n):
    a = int(input("Enter first element of sublist: "))
    b = int(input("Enter second element of sublist: "))
    my_list.append([a, b])

# Sort manually based on second element (Bubble Sort)
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i][1] > my_list[j][1]:  # compare by second element
            # swap
            my_list[i], my_list[j] = my_list[j], my_list[i]

# Print result
print("Sorted List (by second element):", my_list)
