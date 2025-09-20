# Python Program to Multiply All the Items in a Dictionary 

# Create a dictionary
my_dict = {
    "a": 2,
    "b": 3,
    "c": 4
}

#  Initialize product
product = 1

#  Multiply all values
for value in my_dict.values():
    product *= value

# Print the product
print("Product of all items in the dictionary:", product)
