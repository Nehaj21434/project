n = 5  # Total number of rows

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print number only if it's first or last in the row, or it's the last row
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
