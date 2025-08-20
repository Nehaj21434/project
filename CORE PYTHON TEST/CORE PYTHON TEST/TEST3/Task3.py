# Write a program to accept a basic salary of n employees (n should be accepted
# from user). If basic salary is below 2000 then da = 10%, ta = 12% and
# hra = 15%.
# Otherwise da = 15%, ta = 18% and hra = 20%. Based on this, calculate the
# total salary of each employee and also total salary of all employees.
n = int(input("Enter the number of employees: "))
total_salary = 0.0
for i in range(n):
    prompt = f"Enter the basic salary of employee {i + 1}: "
    basic_salary = float(input(prompt))
    
    if basic_salary < 2000:
        da = 0.10 * basic_salary
        ta = 0.12 * basic_salary
        hra = 0.15 * basic_salary
    else:
        da = 0.15 * basic_salary
        ta = 0.18 * basic_salary
        hra = 0.20 * basic_salary

    total_salary_emp = basic_salary + da + ta + hra

    total_salary += total_salary_emp
    
    print(f"Total salary of employee {i + 1} is: {total_salary_emp:.2f}")
