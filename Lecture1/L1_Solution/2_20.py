# ========== 2.20 金融应用程序: 计算利息==========
balance, rate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))
interest = balance * (rate/1200)
print("The interest is", interest)