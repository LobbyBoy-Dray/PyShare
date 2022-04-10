# 程序清单 2-7
# import time
# currentTime = time.time()
# totalSeconds = int(currentTime)
# currentSecond = totalSeconds % 60
# totalMinutes = totalSeconds // 60
# currentMinute = totalMinutes % 60
# totalHours = totalMinutes // 60
# currentHour = totalHours % 24
# print("Current time is ", currentHour, ":",
# 	currentMinute, ":", currentSecond, " GMT", sep = '')

# ========== 2.18 当前时间==========
import time

offset = eval(input("Enter the time zone offset to GMT: "))

currentTime = time.time()
totalSeconds = int(currentTime) + offset * 60 * 60
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24

print("The current time is %d:%d:%d" % (currentHour, currentMinute, currentSecond))