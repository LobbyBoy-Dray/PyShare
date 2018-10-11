# ========== 2.2 计算圆柱体的体积 ==========
pi = 3.14159
radius, length = eval(input("Enter the radius and length of a cylinder: "))
area = radius * radius * pi
volume = area * length
print("The area is", area)
print("The volume is", volume)