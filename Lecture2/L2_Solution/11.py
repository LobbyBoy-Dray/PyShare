# 5.24 财务应用程序: 贷款摊销时间表
#####################################


# 截断到小数点后2位，并非四舍五入
def truncateTo2(number):
	return int(number / 0.01)/100

A = eval(input("Loan Amount: "))                          # 贷款总额
numberOfYears = eval(input("Number of Years: "))          # 总期数: 年
annualRate = eval(input("Annual Interest Rate: "))/100    # 年利率

beta = annualRate/12                                      # 月利率
m = numberOfYears*12                                      # 总期数: 月

# 等额还款，计算月偿还额
X = (A * beta * (1+beta) ** m) / ((1+beta) ** m -1)
X = truncateTo2(X)

# 打印
print("")
print("Monthly Payment: %s" % str(X))
print("Total Payment: %s" % str(truncateTo2(X*m)))
print("")
print("{:<17}{:<17}{:<17}{:<17}".format("Payment#", "Interest", "Principal", "Balance"))
balance = A
for i in range(1, m+1):
	interest = truncateTo2(beta * balance)
	principal = truncateTo2(X - interest)
	balance = truncateTo2(balance - principal)
	print("{:<17}{:<17}{:<17}{:<17}".format(i, interest, principal, balance))
