# 4.21: 科学问题: 一周的星期几
###############################################

weekDay = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

year  = int(input("Enter year: (e.g., 2008): "))
month = int(input("Enter month: 1-12: "))
day   = int(input("Enter the day of the month: 1-31: "))

# 判断是不是1月或2月
if month == 1 or month ==2:
	month += 12
	year  -= 1

i1 = day
i2 = (26*(month+1)/10)//1
i3 = year % 100
i4 = ((year%100) / 4)//1
i5 = (((year/100)//1) / 4)//1
i6 = 5 * ((year / 100)//1)

h = int((i1 + i2 + i3 + i4 + i5 + i6) % 7)

print("Day of the week is %s" % weekDay[h])