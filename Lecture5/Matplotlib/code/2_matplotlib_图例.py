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

###### 5. 定义坐标轴刻度 ######
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

###### 6. 图例 ######
plt.legend(handles = [l1,l2,] , labels = ['aaa','bbb'], loc = 'best')
plt.show()