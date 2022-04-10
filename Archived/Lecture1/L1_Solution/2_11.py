# ========== 2.11 金融应用程序: 投资额==========
finalValue = eval(input("Enter final account value: "))
annualRate = eval(input("Enter annual interest rate in percent: "))/100
years = eval(input("Enter number of years: "))

monthRate = annualRate / 12
months = years * 12
initialValue = finalValue / ((1+monthRate)**months)

print("Initial desposit value is", initialValue)