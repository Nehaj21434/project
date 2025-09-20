# Python Program to Concatenate Two Dictionaries Into One 

#  Create first dictionary
dict1 = {}
n1 = int(input("Enter number of elements in first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

#  Create second dictionary
dict2 = {}
n2 = int(input("Enter number of elements in second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

#  Concatenate dictionaries manually
concatenated_dict = {}
for key in dict1:
    concatenated_dict[key] = dict1[key]
for key in dict2:
    concatenated_dict[key] = dict2[key]

# Print the concatenated dictionary
print("Concatenated Dictionary:", concatenated_dict)
