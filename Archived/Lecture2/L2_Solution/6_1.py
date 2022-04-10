# 4.23: 几何问题: 点在矩形内吗？
###############################################

x, y = eval(input("Enter a point with two coordinates: "))

x = float(x)
y = float(y)

halfHeight = 5.0/2
halfWidth  = 10.0/2

if abs(x) <= halfWidth and abs(y) <= halfHeight:
	print("Point (%s, %s) is in the rectangle" % (str(x), str(y)))
else:
	print("Point (%s, %s) is not in the rectangle" % (str(x), str(y)))