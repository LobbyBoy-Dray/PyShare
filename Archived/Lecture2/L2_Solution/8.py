# 5.1: 统计正数和负数的个数然后计算这些数的平均值
###############################################

total = 0
num_of_positive = 0
num_of_negative = 0 

while True:
	i = int(input("Enter an integer, the input ends if it is 0: "))
	if i == 0:
		break
	else:
		if i > 0:
			num_of_positive += 1
		else:
			num_of_negative += 1
		total += i

if num_of_positive == 0 and num_of_negative == 0:
	print("You didn't enter any number")
else:
	print("The number of positive is %s" % str(num_of_positive))
	print("The number of negative is %s" % str(num_of_negative))
	print("The total is %s" % str(total))
	print("The average is %s" % str(total/(num_of_positive + num_of_negative)))