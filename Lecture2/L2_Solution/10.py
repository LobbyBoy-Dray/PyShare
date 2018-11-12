# 5.18 找出一个整数的所有因子
###########################

number = int(input("Enter an integer: "))
n = 2
result = []

while n <= number:
	while n != number:
		if number % n == 0:
			result.append(str(n))
			number /= n
		else:
			break
	n += 1

result.append(str(n-1))

print(', '.join(result))