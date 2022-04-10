import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,2,1])

plt.figure(figsize=(16,4))
gs = gridspec.GridSpec(1,4)
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1])
ax3 = plt.subplot(gs[0,2])
ax4 = plt.subplot(gs[0,3])

ax1.step(x, y)
ax1.scatter(x,y)
ax2.step(x, y, where='pre')
ax2.scatter(x,y)
ax3.step(x, y, where='post')
ax3.scatter(x,y)
ax4.step(x, y, where='mid')
ax4.scatter(x,y)

plt.show()

