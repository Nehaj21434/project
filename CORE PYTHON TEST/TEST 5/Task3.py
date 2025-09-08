# task 3

data = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Tannu", 14000],
    [320, "Suresh", 35000]
]

for i in range(len(data)):
    for j in range(1, len(data)):
        if data[i][2] > data[j][2]:    # compar salary
            data[i], data[j] = data[j], data[i]   # swap

# sort data
for EMP in data:
    print(EMP)

