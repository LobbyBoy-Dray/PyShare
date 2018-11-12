# 5.31 显示日历
##################################

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_30 = [4,6,9,11]
months_31 = [1,3,5,7,8,10,12]


# 判断是否为闰年
def isLeap(year):
	if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
		return True
	else:
		return False


# 根据第一天周几以及月天数计算最后一天是星期几
def getLastWeekday(firstWeekday, days):
	lastWeekday = (firstWeekday + days % 7) % 7
	lastWeekday = lastWeekday if lastWeekday != 0 else 7
	return lastWeekday


# 打印一个月的日历
def printAmonth(year, month, firstWeekday):
	if month in months_30:
		days = 30
	elif month in months_31:
		days = 31
	else:
		days = 29 if isLeap(year) else 28

	print("            %s %s             " % (months[month-1], str(year)))
	print("-------------------------------------")
	print("%5s" % ('Sun'), end = '')
	print("%5s" % ('Mon'), end = '')
	print("%5s" % ('Tue'), end = '')
	print("%5s" % ('Wed'), end = '')
	print("%5s" % ('Thu'), end = '')
	print("%5s" % ('Fri'), end = '')
	print("%5s" % ('Sat'))

	counter = 0
	for _ in range(firstWeekday % 7):
		print("     ", end='')
		counter += 1

	for i in range(days):
		print("%5s" % str(i+1), end = '')
		counter += 1
		if counter % 7 == 0:
			print("")

	return getLastWeekday(firstWeekday, days-1)


# 打印一整年的日历
def printAyear(year, firstWeekday):
	for i in range(12):
		month = i+1
		lastWeekday = printAmonth(year, month, firstWeekday)
		print("\n\n")
		firstWeekday = (lastWeekday + 1) % 7 if (lastWeekday + 1) % 7 != 0 else 7
		


# 执行
year = 2018							# 2018年
firstWeekday = 1					# 2018年1月1日是星期一
printAyear(year, firstWeekday)		# 显示日历

