# 5.12: 找出可被5和6同时整除的数

############ 方法一：
counter = 0
for i in range(100, 1000):
	if i % (5*6) == 0:
		counter += 1
		if counter % 10 == 0:
			print(i, end = '\n')
		else:
			print(i, end = ' ')

############ 方法二：
# numbers = []
# for i in range(100, 1000):
# 	if i % (5*6) == 0:
# 		numbers.append(str(i))
# 		if len(numbers) == 10:
# 			temp = ' '.join(numbers)
# 			print(temp)
# 			numbers.clear()
# temp = ' '.join(numbers)
# print(temp)