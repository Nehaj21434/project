# 5 Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list. 

n = int(input("Enter the number of element in the list: "))
li = []
for i in range(n):
    ele = int(input("Enter the element: "))
    li.append(ele)

num = int(input("Enter the number to search: "))
count = 0
for value in li:
    if value == num: # check if element matches
        count += 1

if count > 0:
    print(f'present in the list',{num})
    print(f"It appears {count} time")

else:
    print(f'is not persent in the list',{num})
