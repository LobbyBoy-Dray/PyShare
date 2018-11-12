# 5.14 找出最小的n满足n^2 > 12000 (不考虑负整数)
###########################

n = 0
while True:
	n_square = n ** 2
	if n_square > 12000:
		break
	else:
		n += 1

result = n
print(result)
print(result ** 2)