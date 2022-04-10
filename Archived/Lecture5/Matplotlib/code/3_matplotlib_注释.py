import numpy as np
import matplotlib.pyplot as plt

###### 0. 数据生成 ######
x  = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

###### 1. 定义窗口(可选) ######
plt.figure(figsize=(10,5))
#plt.show()
#plt.figure(num=10, figsize=(10,10))
#plt.show()

###### 2. 画图 ######
l1, = plt.plot(x, y2)
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', marker='o', markersize=5)
#plt.show()

###### 3. 定义标题, 坐标轴名称 ######
plt.title('A demo')
plt.xlabel('I am x')
plt.ylabel('I am y')
#plt.show()

###### 4. 定义坐标轴范围 ######
plt.xlim((-1,2))
plt.ylim((-2,3))
#plt.show()

###### 5. 图例 ######
plt.legend(handles = [l1,l2,] , labels = ['aaa','bbb'], loc = 'best')

###### 6. 注释 ######
plt.annotate(r'$local\ minimum$', xy=(0,0), xytext=(+30,-30), textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=-.2'))
plt.text(1.5, -1, r'$This\ is\ some\ text.$', fontdict={'size':10, 'color':'r'})

plt.show()