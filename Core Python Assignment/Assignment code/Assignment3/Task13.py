#  Write a program to input electricity unit charges and calculate total electricity bill 
# according to the given condition: 
# For first 50 units Rs. 0.50/unit 
# For next 100 units Rs. 0.75/unit 
# For next 100 units Rs. 1.20/unit 
# For unit above 250 Rs. 1.50/unit 
# An additional surcharge of 20% is added to the bill

units = int(input ("Enter the units : "))
total_bill = 0

if(units >0):
    if(units > 50):
        if(units > 150):
            if(units >=151):
                if(units > 250):
                    print("something wrong")
                else:
                    total_bill = 100 * 1.20
                    unit4 = units - 100
                    total_bill = total_bill + (units * 1.50)
            else:
                total_bill = 100 * 0.75
                unit3 = units - 100
                total_bill = total_bill + (units * 1.20 )
        else:
            total_bill = 50 * 0.5
            unit2 = units - 50
            total_bill = total_bill + (units * 0.75)
    else:
        total_bill = units * 0.5
else:
    print("Invalid input.")
    
# Add 20% surcharge
surcharge = total_bill * 0.20
total_bills = total_bill + surcharge

print("Electricity Bill: ₹", round(total_bill, 2))
