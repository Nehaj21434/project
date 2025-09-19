# Input 5 subject marks from user and display grade
# (eg. First class, Second class ..)
# Program to calculate grade from 5 subjects

# Step 1: Input marks
s1 = int(input("Enter marks of Subject 1: "))
s2 = int(input("Enter marks of Subject 2: "))
s3 = int(input("Enter marks of Subject 3: "))
s4 = int(input("Enter marks of Subject 4: "))
s5 = int(input("Enter marks of Subject 5: "))

# Step 2: Calculate total and percentage
total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage, "%")

# Step 3: Decide grade using if-else
if percentage >= 75:
    print("Grade: Distinction")
else:
    if percentage >= 60:
        print("Grade: First Class")
    else:
        if percentage >= 50:
            print("Grade: Second Class")
        else:
            if percentage >= 35:
                print("Grade: Pass Class")
            else:
                print("Grade: Fail")
