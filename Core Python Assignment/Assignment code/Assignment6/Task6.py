# Write a program print following patterns:
#        1
#       1 2 3
#     1 2 3 4 5
#    1 2 3 4 5 6 7
#  1 2 3 4 5 6 7 8 9


# Pyramid Number Pattern

rows = 5   # number of rows

for i in range(1, rows + 1):
    # print spaces
    print(" " * (rows - i), end="")

    # print numbers
    for j in range(1, 2*i):
        print(j, end=" ")
    print()
