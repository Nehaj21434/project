# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.



# Take input for list size
n = int(input("Enter number of elements in the list: "))

#  Create the list
numbers = []
for i in range(n):
    num = int(input(f"Enter element : "))
    numbers.append(num)

#  Take input for the target sum
target = int(input("Enter the target sum: "))

#  Find all pairs whose sum equals the target
print("Pairs with sum", target, ":")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("({numbers[i]}, {numbers[j]})")
