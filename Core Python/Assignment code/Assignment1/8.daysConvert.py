"""8. Write a program to convert days into years, weeks and days. """
# This program converts a given number of days into yers, weeks, and remaining days.
# Ask the user to enter thenumber of days.
Days = int(input("Enter the number of days:"))
# calculates the number of years
years = Days //365
# calculates the weeks
weeks = (Days % 365) // 7
# calculates the remaining days
remaingDays = (Days % 365) % 7
# output
print(f"{Days} days is approximately {years} years, {weeks} weeks, {remaingDays} days.")
