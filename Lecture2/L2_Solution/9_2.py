# 5.13: 找出可被5或6整除但又不能被他俩同时整除的数
###########################

counter = 0
for i in range(100, 200):
	if ((i % 5 == 0) or (i % 6 == 0)) and (i % (5*6) != 0):
		counter += 1
		if counter % 10 == 0:
			print(i, end = '\n')
		else:
			print(i, end = ' ')
