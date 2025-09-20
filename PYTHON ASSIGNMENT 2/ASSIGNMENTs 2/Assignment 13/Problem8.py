# Python Program to Count the Frequency of Words Appearing in a String Using 
# a Dictionary

#  Input the string
text = input("Enter a string: ")

# Split the string into words
words = text.split()  # splits by spaces

#  Create an empty dictionary to store word frequencies
freq = {}

# Count frequency of each word
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

#  Print the word frequencies
print("Word Frequencies:")
for word in freq:
    print(word, ":", freq[word])
