import matplotlib
import numpy as np
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

from graph import bezi, from_polar

matplotlib.use('Qt5Agg')


# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self, polar=False):
        self.fig = Figure()
        # if it's polar page we need to set polar projection
        if polar:
            self.axes = self.fig.add_subplot(111, projection='polar')
        else:
            self.axes = self.fig.add_subplot(111)
            # adds major gridlines
            self.axes.grid(alpha=0.5)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Policy.Expanding,
                             QtWidgets.QSizePolicy.Policy.Expanding)
        Canvas.updateGeometry(self)


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, polar=False):
        QtWidgets.QWidget.__init__(self, parent)  # Inherit from QWidget
        self.canvas = MplCanvas(polar)  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()  # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.polar = polar
        self.xdata, self.ydata, self.rdata, self.adata = None, None, None, None  # x- and y- datas for descartes
        # other - for polars
        self.P = None  # saving our core points
        self.timer = None  # later we will be needed this timer
        self.t = 0  # set "index" for start cadre of animation

    def build_plot(self):  # building plot
        self.canvas.axes.cla()  # Clear the canvas before (re)drawing
        if self.polar:
            self.canvas.axes.plot(self.adata, self.rdata, 'r')  # draw plot in polars
            self.canvas.axes.scatter(self.P[:, 1], self.P[:, 0], color='000000', marker='o', s=100)  # draw core points
        else:
            self.canvas.axes.plot(self.xdata, self.ydata, 'r')  # draw plot in descartes
            self.canvas.axes.scatter(self.P[:, 0], self.P[:, 1], color='000000', marker='o', s=100)  # draw core points
            # adds major gridlines
            self.canvas.axes.grid(alpha=0.5)
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

    def update_plot(self):  # function for animating plot
        i = self.t
        self.canvas.axes.cla()  # Clear the canvas.
        if self.polar:
            self.canvas.axes.plot(self.adata, self.rdata, 'r', marker='s', markevery=[i * 10], markerfacecolor='blue',
                                  markersize=10)  # create our curve in polars with marker - needed blue square
            self.canvas.axes.scatter(self.P[:, 1], self.P[:, 0], color='000000', marker='o', s=100)  # draw core points
        else:
            self.canvas.axes.plot(self.xdata, self.ydata, 'r', marker='s', markevery=[i * 10], markerfacecolor='blue',
                                  markersize=10)  # create our curve with marker - needed blue square
            self.canvas.axes.scatter(self.P[:, 0], self.P[:, 1], color='000000', marker='o', s=100)  # draw core points
            # adds major gridlines
            self.canvas.axes.grid(alpha=0.5)
        # Trigger the canvas to update and redraw.
        self.canvas.draw()
        self.t += 1  # to the next cadre
        if self.t == 100:  # if there's 100 of them - our square got to the last point
            self.stopped()  # stopping animation
            self.build(self.P)  # rebuilding our graph

    def build(self, P):  # P is NOT formatted ro descartes
        TAU = np.linspace(0, 1, 1000)  # 1000 points in our curve
        if self.polar:
            bezik = bezi(from_polar(P), TAU)  # create curve and return values in all points of TAU
            X, Y = bezik[:, 0], bezik[:, 1]
            self.adata = np.arctan(Y / X)  # angles
            self.rdata = np.sqrt(np.square(X) + np.square(Y))  # lenghts
        else:
            bezik = bezi(P, TAU)  # create curve and return values in all points of TAU
            self.xdata = bezik[:, 0]
            self.ydata = bezik[:, 1]

        self.P = P
        self.build_plot()

    def anim(self, polar=False):  # regulate the work of animation
        if (not polar and self.x and self.y) \
                or (polar and self.rdata and self.adata):  # if any of the data is ready
            # Setup a timer to trigger the redraw by calling update_plot.
            self.timer = QtCore.QTimer()
            self.timer.setInterval(50)
            self.timer.timeout.connect(self.update_plot)
            self.timer.start()

            self.t = 0  # resetting index

    def stopped(self):  # stop animation with stopping timer
        self.timer.stop()
        self.t = 0
