# 1. Convert the time entered in hh,min and sec into seconds.

# take input from user.
hh = int(input("Enter the Houres:"))
MM = int(input("Enter the Min:"))
SS = int(input("Enter the Sec:"))

# Total second = hh(3600)+ min(60) + sec
total_seconds = (hh * 3600) + (MM * 60) + SS

# Display Output
print(f"total second : {total_seconds}")
