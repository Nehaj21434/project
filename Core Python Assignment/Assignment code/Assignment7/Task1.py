# Write a program print following patterns: 

Name = "Kajkatali"
print("Kajkatali !")
n = 5  # size

# Upper part
for i in range(1, n + 1):
    # Leading spaces
    print(" " * (n - i), end="")

    # Stars and inner spaces
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()

# Lower part
for i in range(1, n):
    # Leading spaces
    print(" " * i, end="")

    # Stars and inner spaces
    for j in range(1, n - i + 1):
        if j == 1 or j == (n - i + 1):
            print("*", end=" ")
        else:
            print("  ", end="")
    print()
