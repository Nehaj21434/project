# Python Program to Sort a List According to the Length of the Elements within the list



#  Take input for number of elements
n = int(input("Enter number of elements in the list: "))

#  Create the list
my_list = []
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)

# Sort the list manually based on length (Bubble Sort)
for i in range(len(my_list)):
    for j in range(0, len(my_list) - i - 1):
        if len(my_list[j]) > len(my_list[j + 1]):  # compare lengths
            # swap
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

#  Print result
print("List sorted by length of elements:", my_list)
