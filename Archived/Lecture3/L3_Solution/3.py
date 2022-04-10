# 6.4 反向显示一个整数

def reverse(number):
	numberStr  = str(number)			# 将int转化为str
	reverseStr = numberStr[::-1]		# 使用切片将str反向
	reverseNum = int(reverseStr)		# 再转化为整数
	return reverseNum

# 测试
num = eval(input("Enter a number: "))
reverseNum = reverse(num)
print("Its reverse number is %s" % str(reverseNum))