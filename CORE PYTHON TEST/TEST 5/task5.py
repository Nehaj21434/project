# Task 5


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

union_list = list1.copy()

for item in list2:
    if item not in union_list:
        union_list.append(item)

print("union of list:", union_list)
