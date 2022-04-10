# ========== 2.14 几何方面: 三角形的面积==========
import math

x1,y1,x2,y2,x3,y3 = eval(input("Enter three points for a triangle: "))
side1 = math.sqrt((x2-x3)**2 + (y2-y3)**2)
side2 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
side3 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))
print("The area of the triangle is", area)