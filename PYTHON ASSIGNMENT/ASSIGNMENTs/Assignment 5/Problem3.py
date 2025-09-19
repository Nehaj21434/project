# Accept no. of passengers from user and per ticket cost. Then accept age of each  
# passenger and then calculate total amount to ticket to travel for all of them based on  
# following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full.

# Program to calculate total ticket amount for passengers

# Step 1: Input number of passengers and per ticket cost
n = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost of one ticket: "))

total_amount = 0   # store total ticket amount

# Step 2: Loop for each passenger
for i in range(1, n + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    # Step 3: Apply discount conditions
    if age < 12:
        fare = ticket_cost * 0.70   # 30% discount
    elif age > 59:
        fare = ticket_cost * 0.50   # 50% discount
    else:
        fare = ticket_cost          # full cost

    print(f"Ticket for passenger {i}: {fare:.2f}")
    total_amount += fare

# Step 4: Print total
print("\nTotal ticket amount for all passengers:", total_amount)
