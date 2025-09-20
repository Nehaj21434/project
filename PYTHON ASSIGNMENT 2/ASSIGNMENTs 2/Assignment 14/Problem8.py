# Write a Python program to find all the anagrams and group them 
# together from a given list of strings.

# Input the list of strings
n = int(input("Enter number of strings: "))
words = []
for i in range(n):
    word = input("Enter string: ")
    words.append(word)

# Find anagrams and group them
groups = []

for word in words:
    found = False
    for group in groups:
        # If sorted word matches sorted first word in group, it's an anagram
        if sorted(word) == sorted(group[0]):
            group.append(word)
            found = True
            break
    if not found:
        groups.append([word])

# Print the groups of anagrams
print("Groups of anagrams:")
for group in groups:
    print(group)
