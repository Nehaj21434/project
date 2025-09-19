# Write a program print following patterns:
#    1
#   1 1
#  1 2 1
# 1 3 3 1

# Pascal's Triangle Pattern

rows = 4   # number of rows

for i in range(4):
    # print spaces for alignment
    print(" " * (rows - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        # update value using binomial coefficient formula
        num = num * (i - j) // (j + 1)
    print()
