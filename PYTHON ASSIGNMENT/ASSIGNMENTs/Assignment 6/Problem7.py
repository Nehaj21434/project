# Write a program print following patterns:
#        A
#      A B C
#    A B C D E
#  A B C D E F G
# A B C D E F G H I

# Alphabet Pyramid Pattern

rows = 5   # number of rows

for i in range(1, rows + 1):
    # print spaces
    print(" " * (rows - i), end="")

    # print alphabets
    for j in range(1, 2*i):
        print(chr(64 + j), end=" ")
    print()
