# Write a program to find maximum and minimum element in a list.


# create the list of the number
li = [12, 15, 20, 30, 40, 50, 60, 70, 55, 43]
# assume the first elemrnt as both max and min intitially.
maximum = li[0]
minimum = li[0]

# traverse the list using a loop
for num in li:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num 

# print the result
print("Number in the list:", li)
print("maximum element in the list:", maximum)
print("minmum element in the list:", minimum)
