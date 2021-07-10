from matplotlib import pyplot as plt
from celluloid import Camera
import numpy as np

TAU = np.linspace(0, 1, 1000) # number of points in graph


def Bezier(t, P): # P - array of 3 points like np.array([[0, 0],[2, 4],[5, 3]])

    # Bezier Matrix:
    Mb = np.matrix([
        [1, -2, 1],
        [-2, 2, 0],
        [1, 0, 0],
    ])
    # T matrix
    xx, yy = np.meshgrid(np.arange(2, -1, -1), t)
    xx = np.matrix(xx)
    yy = np.matrix(yy)
    T_mat = np.power(yy, xx)
    B = T_mat * Mb * P
    return B

def new_plot(P):

    fig = plt.figure()
    plt.xlim(-2, 6)
    plt.ylim(-2, 6)
    X, Y = Bezier(TAU, P)[:, 0], Bezier(TAU, P)[:, 1]
    camera = Camera(fig)

    for i in range(100):
        coord = Bezier(i / 100, P)
        plt.plot(X, Y, color='#ff0000')
        plt.scatter(P[:, 0], P[:, 1], color='#0000FF', marker='o')
        plt.scatter(coord[0, 0], coord[0, 1], color='#00ff00', marker='o', s=100)
        camera.snap()

    animation = camera.animate(interval=20, repeat=True,
                               repeat_delay=0)
    animation.save('animation.gif', writer='pillow', fps=24)