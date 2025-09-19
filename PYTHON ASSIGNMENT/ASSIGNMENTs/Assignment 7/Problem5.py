n = 5  # height of pyramid

for i in range(1, n+1):
    # print spaces
    print(" " * (n - i), end="")

    for j in range(1, i+1):
        # print numbers at boundaries or last row
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
