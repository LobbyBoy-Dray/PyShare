# ========== 2.19 金融应用程序: 计算未来投资额==========
investAmount = eval(input("Enter investment amount: "))
annualRate = eval(input("Enter annual interest rate: ")) / 1001
years = eval(input("Enter number of years: "))

monthRate = annualRate / 12
months = years * 12

accValue = investAmount * (1+monthRate) ** months

print("Accumulated value is", accValue)