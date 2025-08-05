# 4. Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.

length = float(input("Enter the length of wall (in meter):"))
heigth = float(input("Emter the heigth of wall (in meter):"))
costPer_sqm = float(input("Enter the cost of painting per square meter:"))

# calculates total wall area
total_area = 4 * (length * heigth)

total_cost = total_area * costPer_sqm

print("total cost of painting the walls is RS,(total_cost)")
