# Write a program of having n number of elements in the list and find out even 
# and odd elements in that list and then create two separate lists which will have 
# even elements and other will have odd elements. 

n = int(input("Enter the number of element in the list: "))
number = []
for i in range(n):
    element = int(input("Enter the number: "))
    number.append(element)

even_list = []
odd_list = []

for value in number:
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)

print("original list", number)
print("even list ", even_list)
print("Odd list", odd_list)
