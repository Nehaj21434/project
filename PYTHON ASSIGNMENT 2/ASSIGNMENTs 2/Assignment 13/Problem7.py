# Python Program to Remove the Given Key from a Dictionary 
#  Create a dictionary
my_dict = {
    "name": "neha",
    "age": 25,
    "city": "London"
}

#  Input the key to remove
key_to_remove = input("Enter the key to remove: ")

#  Remove the key if it exists
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed successfully.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")

# Print the updated dictionary
print("Updated Dictionary:", my_dict)
