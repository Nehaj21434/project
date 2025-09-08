# 1. all list contains the denmoiation as follows D = [2000, 500, 200, 100, 50, 20, 10, 5]
# accept an amount from user and calculates how many minimum number of notes will br neeede for that amount

# list denomination
li = [2000, 500, 200, 100, 50, 20, 10, 5]

# amount from user
amount = int(input("Enter the amount: "))

print("minimum number of note are required:  ")

for note in li:
    if amount >= note:
        count = amount // note    # how many notes of this types
        amount = amount % note    # remaining amount
        print(f"{note} - {count}")
