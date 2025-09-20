# Python Program to Find the Second Largest Number in a List Using Bubble 
# Sort 


# Take input for list size
n = int(input("Enter number of elements in the list: "))

#  Create the list
numbers = []
for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)

#  Bubble Sort (Ascending order)
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Find the second largest
if len(numbers) < 2:
    print("List must have at least two elements.")
else:
    second_largest = numbers[-2]  # second last element in sorted list
    print("Sorted List:", numbers)
    print("Second Largest Number:", second_largest)
