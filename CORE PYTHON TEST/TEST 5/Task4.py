# Task4


number = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

# empty dict
freq_dict = {}

for num in number:
    if num not in freq_dict:
        freq_dict[num] = 1
    else:
        freq_dict[num] += 1
print(freq_dict)
