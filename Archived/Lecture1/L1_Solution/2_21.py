# ========== 2.21 金融应用程序: 复利值==========
monthSaving = eval(input("Enter the monthly saving amount: "))
monthRate = 0.05 / 12

accValue1 = monthSaving * (1+monthRate)
accValue2 = (accValue1 + monthSaving) * (1+monthRate)
accValue3 = (accValue2 + monthSaving) * (1+monthRate)
accValue4 = (accValue3 + monthSaving) * (1+monthRate)
accValue5 = (accValue4 + monthSaving) * (1+monthRate)
accValue6 = (accValue5 + monthSaving) * (1+monthRate)

print("After the sixth month, the account value is", accValue6)