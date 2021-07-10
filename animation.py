import bezier
import numpy as np
from celluloid import Camera
from matplotlib import pyplot as plt

nodes = np.asfortranarray([
    [0.0, 0.625, 2.0, 4.2],
    [0.0, 0.5  , 0.7, -1],
])
curve = bezier.Curve(nodes, degree=3)
fig = plt.figure()
camera = Camera(fig)


res = curve.evaluate_multi(np.linspace(0, 1, 1000))
plt.plot(res[0], res[1], color='#ff0000')
plt.scatter(nodes[0], nodes[1], color='#0000FF', marker='o')
    #plt.scatter(X[i * 10, 0], Y[i * 10, 0], color='#00ff00', marker='o', s=200)
plt.show()