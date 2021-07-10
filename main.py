import sys

# PySide6 (PyQt 5.0) used to GUI
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QMovie, QPixmap
from matplotlib import pyplot as plt

from graph import new_plot
from untitled import Ui_MainWindow


# Main window of my app
class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # for init all staff from QMainWindow
        self.setupUi(self)  # for beauticode UI part forwarded to another file
        # so this line creates all items from revealed UI file

        self.setWindowIcon(QIcon('icon.png'))  # changing app icon


        self.Anim.clicked.connect(self.anim)
        self.Build.clicked.connect(self.build)
        plt.plot()
        plt.savefig('yo.png')
        self.graph.setPixmap(QPixmap('yo.png'))

    def build(self):
        movie = QMovie('animation.gif')
        movie.setCacheMode(QMovie.CacheNone)
        movie.frameChanged.connect(self.stop)
        self.graph.setMovie(movie)
        if all((self.x0.text(), self.y0.text(), self.x1.text(), self.y1.text(), self.x2.text(), self.y2.text(),self.x3.text(), self.y3.text())):
            P = np.array([[self.x0.text(), self.y0.text()],
                          [self.x1.text(), self.y1.text()],
                          [self.x2.text(), self.y2.text()],
                          [self.x3.text(), self.y3.text()]], dtype=np.dtype(float))
            new_plot(P)
            self.graph.movie().start()
            self.graph.movie().stop()

    def anim(self):
        self.graph.movie().start()

    def stop(self):
        movie = self.graph.movie()
        if movie.currentFrameNumber() == movie.frameCount() - 1:
            movie.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())
