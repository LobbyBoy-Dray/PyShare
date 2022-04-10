import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, Y1, facecolor = '#9999ff', edgecolor = 'white')
plt.bar(X, -Y2, facecolor = '#ff9999', edgecolor = 'white')

plt.ylim(-1.2, 1.2)

plt.xticks(())
plt.yticks(())

for x, y1 in zip(X,Y1):
    # ha: horizontal alignment
    # va: vertical alignment
	plt.text(x, y1, '%.2f' % y1, ha='center', va='bottom')

for x, y2 in zip(X,Y2):
    # ha: horizontal alignment
    # va: vertical alignment
	plt.text(x, -y2-0.03, '%.2f' % y2, ha='center', va='top')

plt.show()