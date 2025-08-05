# 1. Write a program to accept year from user and check if it is a leap year or not.

year = int(input("Enter the year: "))
# this year is used to check if it is a leap year or not
# if the year is divisible by 100 then it must also be divisible by 400
# nested if statements are used to check the conditions for leap year
# If the year is not divisible by 4 → Not a leap year.
# If divisible by 4 but not divisible by 100 → Leap year.
# If divisible by 100, then it must also be divisible by 400 → Leap year

# the if statement checks if the year is divisible by 4
if year % 4 == 0:
    # the nested if statement checks if the year is divisible by 100
    if year % 100 == 0:
        # if the year is divisible by 100 then it must also be divisible by 400
        if year % 400 == 0:
            # if the year is divisible by 400 then it's a leap year
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")
