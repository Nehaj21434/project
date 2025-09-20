# 1. Write a program to find sum of all elements of list.


# function to calculates sum of element in a list
def sum_of_element(number):
    total = 0     # start with 0
    for num in number:   # loop through each elemant of the list.
        total = total + num   # keep adding element one by one
    return total


my_list = [10, 20, 30, 40, 50, 60]

# function call
result = sum_of_element(my_list)

# print result
print("The sum of all element in the list is:", result)
