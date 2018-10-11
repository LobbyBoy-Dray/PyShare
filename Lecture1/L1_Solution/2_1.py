# ========== 2.1 将摄氏温度转化为华氏温度 ==========
celsius = float(input("Enter a degree in Celsius: "))
fahrenheit = (9/5) * celsius + 32
print("%s Celsius is %s Fahrenheit" % (str(celsius), str(fahrenheit)))

# 最后一条打印语句还可以有以下两种写法：
# print("%f Celsius is %f Fahrenheit" % (celsius, fahrenheit))
# print(celsius, "Celsius is", fahrenheit, "Fahrenheit")