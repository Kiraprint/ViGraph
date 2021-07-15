import numpy as np


def from_polar(p_pts):  # translate points in polar system to descartes
    r = p_pts[:, 0]
    phi = p_pts[:, 1]
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return np.array([x, y]).T


def bezi(P, t):  # core function that evaluate curves
    MB = np.matrix([
        [3, -6, 3, 0],  # https://en.wikipedia.org/wiki/Bézier_curve
        [-1, 3, -3, 1],
        [-3, 3, 0, 0],
        [1, 0, 0, 0]
    ])
    xx, yy = np.meshgrid(np.arange(3, -1, -1), t)  # powers of t
    xx = np.matrix(xx)
    yy = np.matrix(yy)
    T_mat = np.power(yy, xx)  # yy in power of xx
    B = T_mat * MB * P  # get coords
    return B  # returns coords
