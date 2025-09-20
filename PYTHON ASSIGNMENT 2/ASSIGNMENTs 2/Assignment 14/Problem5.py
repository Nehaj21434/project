# Write a Python program to find the longest common prefix of all strings. Use the Python set.


#List of words
words = ["Flower" ,"Flow" ,"Flight",]

#Initialize prefix
prefix = ""

#Find length of shortest word
min_len = min(len(w) for w in words)  #"Flow" ------ 4 letters


for i in range(min_len):
    chars =set(word[i] for word in words)
    
    if len(chars) == 1:
        prefix += chars.pop()
        
    else:
        break
    
print("Lomgest common perfix: ",prefix)