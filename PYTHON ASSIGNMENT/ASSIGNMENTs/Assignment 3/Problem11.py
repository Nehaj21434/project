# 11 Accept age of five people and also per person ticket amount and then
# calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# Ticket Calculation for 5 People

# Step 1: Take ticket price input (per person)
ticket_price = float(input("Enter ticket price per person: "))

# Step 2: Initialize total amount
total_amount = 0

# Step 3: Loop for 5 people
for i in range(1, 6):
    age = int(input("Enter age of person " + str(i) + ": "))

    # Step 4: Apply discount using only if and else
    if age < 12:
        pay = ticket_price * 0.70   # 30% discount
    else:
        if age > 59:
            pay = ticket_price * 0.50   # 50% discount
        else:
            pay = ticket_price          # Full price

    # Add to total
    total_amount += pay

    # Show per person payment
    print("Person", i, "pays:", pay)

# Step 5: Show total
print("Total ticket amount for all 5 persons:", total_amount)
