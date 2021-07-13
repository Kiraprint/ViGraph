import sys

# PySide6 (PyQt 5.0) used to GUI
import matplotlib
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QMovie, QPixmap
from matplotlib import pyplot as plt  # adding start plot

from graph import new_plot  # main task of app
from untitled import Ui_MainWindow

matplotlib.rcParams['figure.dpi']=100

# Main window of my app
class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # for init all staff from QMainWindow
        self.setupUi(self)  # for beauticode UI part forwarded to another file
        # so this line creates all items from revealed UI file

        self.setWindowIcon(QIcon('icon.png'))  # changing app icon

        self.Anim.clicked.connect(self.anim)  # connecting buttons with its functions
        self.Build.clicked.connect(self.build)

        plt.plot()  # creating start plot
        plt.savefig('yo.png')  # saving it
        self.graph.setPixmap(QPixmap('yo.png'))  # and we can see it in the app

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
            movie.setCacheMode(QMovie.CacheNone)
            movie.frameChanged.connect(self.stop)  # bcs of this gif doesn't loop
            self.graph.setMovie(movie)  # add our gif to the label
            self.graph.movie().start()  # starts and stops gif: we need only to see 1st cadre
            self.graph.movie().stop()

    def anim(self):  # start playing animation
        self.graph.movie().start()

    def stop(self):  # this stops our gif at the first/zero loop
        movie = self.graph.movie()
        if movie.currentFrameNumber() == movie.frameCount() - 1:
            movie.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())
