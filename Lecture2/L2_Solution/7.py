# 4.26: 回文数
###############################################

number = str(int(input("Enter a three-digit integer: ")))

if number[0] == number[-1]:
	print("%s is a palindrome" % number)
else:
	print("%s is not a palindrome" % number)