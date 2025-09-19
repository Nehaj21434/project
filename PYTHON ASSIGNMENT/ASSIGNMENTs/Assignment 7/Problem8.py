
# write the the program to following patterns:



k = 7  # Initialize variable 'k' to control the number of spaces between number patterns

# Outer loop to control the number of rows (from 1 to 5)
for i in range(1, 6):

    # First inner loop: print increasing numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")  # Print number followed by space, stay on the same line

    # Second inner loop: print spaces (double spaces) for formatting
    for s in range(1, k + 1):
        print(" ", end=" ")  # Print space with padding, stay on the same line

    k -= 2  # Decrease the number of spaces by 2 after each row

    # Third inner loop: print decreasing numbers from i to 1
    for j in range(i, 0, -1):
        if j != 5:  # Skip printing 5 in the mirrored pattern
            print(j, end=" ")  # Print number followed by space

    print()  # Move to the next line after completing one row
