import numpy as np
from celluloid import Camera
from matplotlib import pyplot as plt

TAU = np.linspace(0, 1, 1000)  # 1000 of points from [0; 1000]

def from_polar(p_pts):
    r = p_pts[:, 0]
    phi = p_pts[:, 1]
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return np.array([x, y]).T


def bezi(P, t):  # core function that evalueat
    MB = np.matrix([
        [-1, 3, -3, 1],
        [3, -6, 3, 0],
        [-3, 3, 0, 0],
        [1, 0, 0, 0]
    ])
    xx, yy = np.meshgrid(np.arange(3, -1, -1), t)  # powers of t
    xx = np.matrix(xx)
    yy = np.matrix(yy)
    T_mat = np.power(yy, xx)  # yy in power of xx
    B = T_mat * MB * P  # get coords
    return B  # returns coords


def new_plot(P, polar=False):  # P - nparray of points that must init like np.array([[1,0], [2, 3], [3, 5], [4, 1]])
    fig = plt.figure()
    camera = Camera(fig)  # creating camera for animation

    if polar:
        pts = from_polar(P)
        bezik = bezi(pts, TAU)  # create curve and return values in all points of TAU
        X, Y = bezik[:, 0], bezik[:, 1]  # as result get X and Y in 1 array
        plt.axes(projection='polar')
        phi = np.arctan(Y / X)
        r = np.sqrt(np.square(X) + np.square(Y))

        for i in range(100):
            plt.plot(phi, r, color='#ff0000')
            plt.scatter(phi[i * 10, 0], r[i * 10, 0], color='#0000ff', marker='s', s=100)
            camera.snap()
    else:
        bezik = bezi(P, TAU)  # create curve and return values in all points of TAU
        X, Y = bezik[:, 0], bezik[:, 1]  # as result get X and Y in 1 array
        for i in range(100):  # 100 cadres of animation, marker = which line used for anim
            plt.plot(X, Y, color='#ff0000')
            plt.scatter(P[:, 0], P[:, 1], color='#000000', marker='o')
            plt.scatter(X[i * 10, 0], Y[i * 10, 0], color='#0000ff', marker='s', s=100)
            camera.snap()  # +cadre

    animation = camera.animate(interval=20, repeat=False, repeat_delay=0)  # getting res of animation
    animation.save('animation.gif', writer='pillow', fps=24)  # save res as .gif
