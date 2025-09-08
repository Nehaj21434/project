# A teacher comes to class with a large box.
#  tokhat  has several coins. Each coin has a number printed on it before coming to class.
#  She ensures that all the numbers occur an even number of times, however, while coming to the class, one coin fell down and got lost.
#  She wants to find out the number on missing coin, input the original number of coin and actual number of each of the coin, separate by space, 
# output the number on missing coin, sample 
# input 8, 5, 7, 2, 7, 5, 2, 5, sample output 5.


# input list of coin

coins = [5, 7, 2, 7, 5, 2, 5]

missing = 0
for coin in coins:
    missing = missing ^ coin   # xor operation

print("Missing coin number is:", missing)
