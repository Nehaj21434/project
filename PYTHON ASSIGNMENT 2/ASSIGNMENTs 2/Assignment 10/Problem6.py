# Write a program to remove duplicates from the list.

n = int(input("Enter the  number of element in thr list: "))

li = []
for i in range(n):
    ele = int(input("Enter the element: "))
    li.append(ele)

unique_list = []
for value in li:
    if value not in unique_list:   # check if already added
        unique_list.append(value)

print("Original list", li)
print("after element removing the duplicates ele", unique_list)
