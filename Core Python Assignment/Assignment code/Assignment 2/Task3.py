# 3.Convert distant given in feet and inches into meter and centimeter.
# 1foot = 0.3048.
# 1inch = 0.0254
# 1meter = 100 cen.

# Input distance in feet and inches
feet = float(input("Enter the Distance in feet:"))
inches = float(input("Enter the Distance in inches:"))

# convert feet and inches to meters.
meters_from_feet = feet * 0.3048
meters_from_inches = inches * 0.0254

# Total distance in meter.
Total_meter = meters_from_feet + meters_from_inches

# Converts meter to centimeter.
Total_centimeter = Total_meter * 100

# Display output
print("Distance in meter:", Total_meter)
print("Distance in centimeter:", Total_centimeter)
