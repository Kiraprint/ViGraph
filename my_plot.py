import numpy as np
from matplotlib import pyplot as plt

from graph import bezi

P = np.array([[1, 0], [2, 3], [3, 5], [4, 1]])
TAU = np.linspace(0, 1, 1000)
bezik = bezi(P, TAU)  # create curve and return values in all points of TAU
X, Y = bezik[:, 0], bezik[:, 1]  # as result get X and Y in 1 array
plt.plot(X, Y, color='#ff0000')
plt.show()

plt.axes(projection='polar')
phi = np.arctan(Y/X)
r = np.sqrt(np.square(X) + np.square(Y))
plt.plot(phi, r)

plt.show()