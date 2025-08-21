# Enter number of students from user. 
# For those many students accept marks of 5 subject marks from user and calculate percentage.
# Display all percentage and average percentage of students.

# Program to calculate percentage and average percentage of students

# Step 1: Number of students
n = int(input("Enter number of students: "))

# Step 2: List to store percentages
percentages = []

# Step 3: Loop for each student
for i in range(1, n + 1):
    print(f"\nEnter marks of 5 subjects for Student {i}:")
    total = 0
    for j in range(1, 6):   # 5 subjects
        marks = int(input(f"  Subject {j} marks: "))
        total += marks
    
    # Step 4: Calculate percentage (assuming each subject out of 100)
    percentage = total / 5
    percentages.append(percentage)
    print(f"Percentage of Student {i}: {percentage:.2f}%")

# Step 5: Average percentage of all students
average = sum(percentages) / n
print("\nAll Students Percentages:", percentages)
print(f"Average Percentage of all students: {average:.2f}%")
