import sys

import matplotlib
import numpy as np
from PyQt6 import QtWidgets  # PyQt 6.1.2 used to GUI
from PyQt6.QtGui import QIcon, QMovie, QPixmap
from matplotlib import pyplot as plt  # adding start plot
from qt_material import apply_stylesheet  # set not system style

from graph import new_plot  # main task of app
from untitled import Ui_MainWindow

matplotlib.rcParams['figure.dpi'] = 100


# Main window of my app
class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # for init all staff from QMainWindow
        self.setupUi(self)  # for beauticode UI part forwarded to another file
        # so this line creates all items from revealed UI file

        self.setWindowIcon(QIcon('icon.png'))  # changing app icon

        self.Anim.clicked.connect(self.anim)  # connecting buttons with its functions
        self.Build.clicked.connect(self.build)
        self.polar.clicked.connect(self.to_polar_page)

        self.Anim_2.clicked.connect(self.anim_2)
        self.Build_2.clicked.connect(self.build_2)
        self.descartes.clicked.connect(self.to_descartes_page)

        plt.plot()  # creating start plot
        plt.savefig('yo.png')  # saving it
        self.graph.setPixmap(QPixmap('yo.png'))  # and we can see it in the app

        plt.axes(projection='polar')
        plt.plot()  # creating start plot
        plt.savefig('yo.png')  # saving it
        self.graph_2.setPixmap(QPixmap('yo.png'))  # and we can see it in the app

    def build(self):  # builds our graph with animation

        if all((self.x0.text(), self.y0.text(), self.x1.text(), self.y1.text(),
                self.x2.text(), self.y2.text(), self.x3.text(), self.y3.text())):
            P = np.array([[self.x0.text(), self.y0.text()],
                          [self.x1.text(), self.y1.text()],
                          [self.x2.text(), self.y2.text()],
                          [self.x3.text(), self.y3.text()]], dtype=np.dtype(float))
            new_plot(P)  # creating graph in .gif with new data
            movie = QMovie('animation.gif')  # every click recreates new gif
            # with new graph and ready for playing animation

            movie.frameChanged.connect(self.stop)  # bcs of this gif doesn't loop
            self.graph.setMovie(movie)  # add our gif to the label
            self.graph.movie().start()  # starts and stops gif: we need only to see 1st cadre
            self.graph.movie().stop()

    def build_2(self):
        if all((self.r0.text(), self.a0.text(), self.r1.text(), self.a1.text(),
                self.r2.text(), self.a2.text(), self.r3.text(), self.a3.text())):
            P = np.array([[self.a0.text(), self.r0.text()],
                          [self.a1.text(), self.r1.text()],
                          [self.a2.text(), self.r2.text()],
                          [self.a3.text(), self.r3.text()]], dtype=np.dtype(float))
            new_plot(P, polar=True)  # creating graph in .gif with new data
            movie = QMovie('animation.gif')  # every click recreates new gif
            # with new graph and ready for playing animation

            movie.frameChanged.connect(self.stop)  # bcs of this gif doesn't loop
            self.graph_2.setMovie(movie)  # add our gif to the label
            self.graph_2.movie().start()  # starts and stops gif: we need only to see 1st cadre
            self.graph_2.movie().stop()

    def anim(self):  # start playing animation
        self.graph.movie().start()

    def anim_2(self):
        self.graph_2.movie().start()

    def stop(self):  # this stops our gif at the first/zero loop
        movie = self.graph.movie()
        movie_2 = self.graph_2.movie()
        if movie.currentFrameNumber() == movie.frameCount() - 1:
            movie.stop()
        if movie_2.currentFrameNumber() == movie_2.frameCount() - 1:
            movie_2.stop()

    def to_polar_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def to_descartes_page(self):
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')
    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())
