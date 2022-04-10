import math

today = int(input("Enter today's day: "))
after = int(input("Enter the number of days elapsed since today: "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

futureDay = after % 7
futureDay = (today + futureDay) % 7

print("Today is %s and the future day is %s" % (days[today], days[futureDay]))