# Print 1 to 100 in snakes and ladder pattern. 
board = []
for i in range(9, -1, -1):
    row = []
    for j in range((i * 10) + 1, (i * 10) + 11):
        # print(j, end='')
        row.append(j)
    # print()
    if (i % 2 != 0):
        row.reverse()
    board.append(row)
print(board)