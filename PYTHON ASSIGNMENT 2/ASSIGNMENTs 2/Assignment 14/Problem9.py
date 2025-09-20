# Write a Python program to find all the unique combinations of 3 
# numbers from a given list of numbers, adding up to a target number.

# Input list of numbers
n = int(input("Enter number of elements in the list: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))

# Input the target sum
target = int(input("Enter the target sum: "))

# Find all unique combinations of 3 numbers
combinations = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                combo = [numbers[i], numbers[j], numbers[k]]
                # Sort to avoid duplicates like [1,2,3] and [3,2,1]
                combo.sort()
                if combo not in combinations:
                    combinations.append(combo)

# Print results
print("Unique combinations of 3 numbers that sum to", target, ":")
for combo in combinations:
    print(combo)
