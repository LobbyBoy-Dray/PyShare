import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
	height = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
	return height

# 数据点数量
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

print(X.flatten())

#### 填充颜色
plt.contourf(X.flatten(), Y.flatten(), f(X,Y), 8, alpha=0.75, cmap=plt.cm.RdBu)
#### 绘制等高线
C = plt.contour(X, Y, f(X,Y), 8, colors='black')
#### 添加高度数字
plt.clabel(C, inline=True, fontsize=10)
plt.show()