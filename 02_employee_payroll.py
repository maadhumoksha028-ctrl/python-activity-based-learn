# Assignment 2: Employee Payroll and Deduction Analysis
# Calculate gross salary, a 10% deduction, and net salary.

basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))

if basic < 0 or allowance < 0 or overtime < 0:
    print("Salary amounts cannot be negative.")
else:
    gross = basic + allowance + overtime
    deduction = gross * 0.10
    net = gross - deduction

    print("Basic Salary:", basic)
    print("Gross Salary:", gross)
    print("Deduction:", deduction)
    print("Net Salary:", net)
