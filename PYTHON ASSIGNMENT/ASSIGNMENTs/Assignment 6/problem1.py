# Write a program print following patterns:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# Hollow square star pattern

rows = 5   # number of rows
cols = 5   # number of columns

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        # print star for first row, last row, first column, last column
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()
