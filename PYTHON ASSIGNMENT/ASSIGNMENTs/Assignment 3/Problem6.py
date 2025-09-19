# 6 Write a program to calculate profit or loss.
CP = float(input("Enter cost price:"))
SP = float(input("Enter selling price:"))
if SP > CP:          # profit
    profit = SP - CP
    print(f"profit: {profit}")
else:
    if (SP < CP):      # loss
        loss = CP - SP
        print(f"loss: {loss}")
    else:
        print("No profit no loss")
