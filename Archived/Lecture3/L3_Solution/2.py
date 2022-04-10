# 6.3 回文整数

def reverse(number):
	numberStr  = str(number)			# 将int转化为str
	reverseStr = numberStr[::-1]		# 使用切片将str反向
	reverseNum = int(reverseStr)		# 再转化为整数
	return reverseNum

def isPalindrome(number):
	palinNum = reverse(number)
	return palinNum == number


# 测试
print(isPalindrome(1000))
print(isPalindrome(654321000123456))