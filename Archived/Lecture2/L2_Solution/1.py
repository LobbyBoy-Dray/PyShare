name = input("Enter employee's name: ")
workHours = float(input("Enter number of hours worked in a week: "))
payPerHour = float(input("Enter hourly pay rate: "))
federalTaxRate = float(input("Enter federal tax withholding rate: "))
stateTaxRate = float(input("Enter state tax withholding rate: "))

grossPay = workHours * payPerHour
federalWithholding = grossPay * federalTaxRate
stateWithholding = grossPay * stateTaxRate
totalWithholding = federalWithholding+stateWithholding
netPay = grossPay - totalWithholding

print("Employee Name: %s" % name)
print("Hours Worked: %s" % str(workHours))
print("Pay Rate: $%s" % str(payPerHour))
print("Gross Pay: $%s" % str(grossPay))
print("Deductions:")
print("  Federal Withholding (%.1f%%): $%s" % (federalTaxRate*100, str(federalWithholding)))
print("  State Withholding (%.1f%%): $%s" % (stateTaxRate*100, str(stateWithholding)))
print("  Total Deduction: $%s" % str(totalWithholding))
print("Net Pay: $%.2f" % netPay)