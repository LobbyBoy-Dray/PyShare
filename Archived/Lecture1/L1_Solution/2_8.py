# ========== 2.8 科学: 计算能量==========
amount = eval(input("Enter the amount of water in kilograms: "))
initialT = eval(input("Enter the initial temperature: "))
finalT = eval(input("Enter the final temperature: "))
Q = amount * (finalT - initialT) * 4184
print("The energy needed is", Q)