# Write a program to accet a basic salary of n emp (n should be acceoted from user) if basic salary is below 2000 then da = 10%  ta = 12% and hra = 15% otherwise sa = 15% ta =18% and hra = 20%  . based on this calculate the total salary of each emp and also tatal salary of all emp
n = int(input("Enter the number of employees: "))
total_salary = 0.0
for i in range(n):
    basic_salary = float(input(f"Enter the basic salary of employee {i + 1}: "))
    
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
