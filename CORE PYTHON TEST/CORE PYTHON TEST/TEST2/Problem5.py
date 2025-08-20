"""5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
the total bill after adding 18% GST"""

# Accept prices of 5 products
p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))

# Step 1: Calculate total price
total_price = p1 + p2 + p3 + p4 + p5

# Step 2: Add 18% GST
final_bill = total_price * 1.18  # same as total + (total*0.18)

# Step 3: Display total bill
print("Total bill after 18% GST is Rs", (final_bill))
