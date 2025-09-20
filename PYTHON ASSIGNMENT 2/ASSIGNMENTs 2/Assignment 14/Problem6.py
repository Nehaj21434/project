# Write a Python program to find the two numbers whose product 
# is maximum among all the pairs in a given list of numbers. Use the Python set.



li = [2,3,4,5,9,10,8,6,7]

li =set(li)

sort = sorted(li ,reverse=True)

max1 , max2 = sort[0],sort[1]

print("Maximum Product: ",max1 * max2)