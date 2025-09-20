#  Write a program to find the second largest element in the list.

li = [10, 30, 40, 50, 60, 20, 70, 80]
max = li[0]
Smax = 0
for i in range(1, len(li)):
    if (li[i] > max):
        Smax = max
        max = li[i]
    elif (li[i] > Smax):
        Smax = li[i]
print("Maximum number is ", max)
print("second largest number is", Smax)
