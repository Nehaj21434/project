# 5.WAP to calculate selling price of book based on cost price and discount.

# Step 1: Input cost price and discount percentage
cost_price = float(input("Enter the cost price of the book: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 2: Calculate discount amount, discount_amount=(CP×D)/100.
discount_amount = (cost_price * discount_percent) / 100

# Step 3: Calculate selling price,SP=CP−discount_amount.
selling_price = cost_price - discount_amount

# Step 4: Display the selling price
print("Selling Price of the book:", selling_price)
