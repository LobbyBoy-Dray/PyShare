# 6.2 求一个整数各个数字的和

def sumDigits(n):
	n = -n if n < 0 else n
	total = 0
	while n > 0:
		total += n % 10
		n     =  n // 10
	return total


# 测试
print(sumDigits(123456789))