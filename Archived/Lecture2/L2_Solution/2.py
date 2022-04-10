import math

a,b,c = eval(input("Enter a, b, c: "))

delta = b**2 - 4*a*c

if delta > 0:
	r1 = (-b + math.sqrt(delta)) / (2*a)
	r2 = (-b - math.sqrt(delta)) / (2*a)
	print("The roots are %s and %s" % (str(r1), str(r2)))
elif delta == 0:
	r = (-b) / (2*a)
	print("The root is %s" % str(r))
else:
	print("The equation has no real roots")