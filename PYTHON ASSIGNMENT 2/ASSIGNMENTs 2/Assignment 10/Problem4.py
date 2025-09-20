# 4. Write a program to reverse the list.

n = int(input("Enter the number of element in the list: "))
li = []
for i in range(n):
    ele = int(input("Enter the element: "))
    li.append(ele)

reverse_li = []
for i in range(len(li) - 1, -1, -1):
    reverse_li.append(len(li))

print("original list", li)
print("Reverse list is", reverse_li)    
