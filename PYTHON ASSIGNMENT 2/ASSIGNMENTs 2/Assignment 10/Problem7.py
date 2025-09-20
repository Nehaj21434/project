# Write a program to create a new list from existing list which contains cube of 
# each number of list.

n = int(input("Enter the number of element in the list: "))
li = []
for i in range(n):
    element = int(input("Enter the element: "))
    li.append(element)

cube_list = []
for value in li:
    cube = value * value * value  # calculating cube manually
    cube_list.append(cube)

print("Original list", li)
print("Cube list", cube_list)
