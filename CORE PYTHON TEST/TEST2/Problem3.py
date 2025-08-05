"""3.A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
cost of fencing the field."""

radius = 20
length = 50
breadth = 40
costPer_meter = 35
round = 5

# perimeter of field
perimeter = length + breadth + (3.14 * radius)

# total wire length for 5 round
total_wire = perimeter * round

# total cost
total_cost = total_wire * costPer_meter

# Display result
print("Total cost of fencing is Rs", (total_cost))
