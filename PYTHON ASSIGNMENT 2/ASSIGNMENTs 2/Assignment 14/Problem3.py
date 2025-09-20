# Write a Python program to find all the unique words and count the 
# frequency of occurrence from a given list of strings. Use Python set data type. 



words_list = ["Apple","Banana","Apple" ,"Orange" ,"Banana" ,"Mango"]

words =set(words_list)
print("Unique words:",words)

for words in words:
    count = words_list.count(words)
    print(f'{words} : {count}')