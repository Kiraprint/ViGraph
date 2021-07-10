import sys

# PySide6 (PyQt 5.0) used to GUI
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QMovie

from untitled import Ui_MainWindow


# Main window of my app
class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # for init all staff from QMainWindow
        self.setupUi(self)  # for beuticode UI part forwarded to another file
                            # so this line creates all items from revealed UI file

        self.setWindowIcon(QIcon('icon.png')) # changing app icon

        movie = QMovie('animation.gif')
        movie.setCacheMode(QMovie.CacheNone)
        movie.frameChanged.connect(self.stop)
        self.graph.setMovie(movie)
        self.pushButton_2.clicked.connect(self.anim)

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
