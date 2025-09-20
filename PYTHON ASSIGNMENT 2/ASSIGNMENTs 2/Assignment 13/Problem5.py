#  Python Program to Sum All the Items in a Dictionary

# Create a dictionary
my_dict = {
    "a": 10,
    "b": 20,
    "c": 30
}

# Initialize sum
total = 0

#  Sum all values
for value in my_dict.values():
    total += value

#  Print the sum
print("Sum of all items in the dictionary:", total)
