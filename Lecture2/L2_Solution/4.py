exRate = eval(input("Enter the exchange rate from dollars to RMB: "))
isRMBtoDollars = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if isRMBtoDollars == 1:
	RMB = eval(input("Enter the RMB amount: "))
	Dollars = RMB / exRate
	print("%.2f yuan is $%.2f" % (RMB, Dollars))
elif isRMBtoDollars == 0:
	Dollars = eval(input("Enter the dollar amount: "))
	RMB = Dollars * exRate
	print("$%.2f is %.2f yuan" % (Dollars, RMB))
else:
	print("Incorrect input")