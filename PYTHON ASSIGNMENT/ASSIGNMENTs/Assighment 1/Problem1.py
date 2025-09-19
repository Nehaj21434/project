# Q1. Write a program to calculate the percentage of
# student based on marks of any 5 subjects.

# algoritham:
# 1. start
# 2. input the marks for 5 subjects (out of 100)
# 3. calculate the total marks obtained
# 4. calculate the percentage using the
# formula: percentage = (totalMarks / 500) * 100
# 5. display the total marks and percentage
# 6. end.

# This program calcutes the percentage of marks for 5 subjects.
# Ask the user to enter the marks out of 100 for each subject.
# calaculate the percentage and print it.
print("Enter the marks for 5 subjects(out of 100):")
# inter marks for each sunject.
subject1 = int(input("Enter Marks for subject 1:"))
subject2 = int(input("Enter marks for subject 2:"))
subject3 = int(input("Enter marks for subject 3:"))
subject4 = int(input("Enter marks for subject 4:"))
subject5 = int(input("Enter marks for subject 5:"))

# calculate the total marks.
totalMarks = subject1 + subject2 + subject3 + subject4 + subject5

# calculate the percentage.
percentage = (totalMarks / 500) * 100

# print the percentage.
# show the result.
print("Total marks =", totalMarks, "out of 500")
print("Percentage =", percentage, "%")
