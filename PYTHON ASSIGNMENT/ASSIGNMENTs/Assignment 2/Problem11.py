# 11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
# Program to find minimum number of notes for a given amount

# Input from user
amount = int(input("Enter the amount: "))

# List of denominations (in descending order)
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes required:")

for note in denominations:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} x {count}")
