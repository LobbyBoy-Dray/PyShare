# ========== 2.6 对一个整数中各位数字求和==========
number = eval(input("Enter a number between 0 and 1000: "))
unitsDigit = number % 10
tensDigit = (number // 10) % 10
hundredsDigit = (number // 100) % 10
sum_ = unitsDigit + tensDigit + hundredsDigit
print("The sum of the digits is", sum_)