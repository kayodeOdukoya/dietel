employee_name = input("Enter employees name: ")
number_of_hours = int(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
month = input("Enter month:")
federal_tax_rate = float(input("Enter federal tax witholding rate: "))
state_tax_rate = float(input("Enter state tax witholding rate: "))


gross_pay = number_of_hours * pay_rate
federal_withholding = gross_pay * (federal_tax_rate / 100)
state_withholding = gross_pay * (state_tax_rate / 100)
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay * total_deduction


print("\n\n")
print("{}payroll statement for the month of {}".format(employee_name, month))
print("Employee_name:", employee_name)
print("Number of hours worked in a week", number_of_hours)
print("Hours Pay Rate", hourly_pay_rate)
print("Gross pay:$", gross_pay)
print("Month", month)
print("Federal Withholding rate({}%):".format(federal_tax_rate),federal_withholding)
print("State Withholding rate({}%):".format(state_tax_rate),state_withholding)
print("Total Deduction:$",total_deduction)
print("Net Pay:$",net_pay)
