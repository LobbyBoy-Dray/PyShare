# ========== 2.7 计算年数和天数==========
import math
totalminutes = eval(input("Enter the number of minutes: "))
totalDays = math.ceil(totalminutes // (24*60))
years = totalDays // 365
days = totalDays % 365
print(totalminutes, "minutes is approximately", years, "years and", days, "days")