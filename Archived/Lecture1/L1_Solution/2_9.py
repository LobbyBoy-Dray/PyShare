# ========== 2.9 科学: 风寒温度==========
T = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
windSpeed = eval(input("Enter the wind speed in miles per hour: "))
windChillIndex = 35.74 + 0.6215 * T - 35.75 * windSpeed ** 0.16 + 0.4275 * T * windSpeed ** 0.16
print("The wind chill index is", windChillIndex)