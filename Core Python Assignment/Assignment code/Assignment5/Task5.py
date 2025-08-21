# Write a program to accept an integer amount from user and tell minimum  
# number of notes needed for representing that amount. (Use looping to optimize  
# the problem) 

# Program to find minimum number of notes for a given amount

# Step 1: Input amount
amount = int(input("Enter the amount: "))

# Step 2: Available denominations (India example)
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print(f"\nAmount: {amount}")
print("Minimum number of notes:")

# Step 3: Loop through each note
for note in notes:
    if amount >= note:
        count = amount // note     # how many notes of this denomination
        amount = amount % note     # remaining amount
        print(f"{note} x {count}")
