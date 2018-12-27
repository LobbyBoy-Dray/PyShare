import numpy as np
import matplotlib.pyplot as plt

X = np.random.uniform(0,10,150)
Y = np.random.uniform(0,10,150)

plt.scatter(X, Y, s = 75, alpha = 0.5)
plt.show()