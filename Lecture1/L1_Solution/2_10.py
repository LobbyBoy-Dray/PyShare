# ========== 2.10 物理方面: 计算跑道长度==========
speed, acceleration = eval(input("Enter speed and acceleration: "))
minLength = speed * speed / (2*acceleration)
print("The minimum runway length for this airplane is", minLength)