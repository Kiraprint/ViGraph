import sys

import matplotlib  # to using Qt5Agg
import numpy as np  # for evaluates
from PyQt5 import QtWidgets  # PyQt 5 used to GUI
from PyQt5.QtGui import QIcon  # for changing icon
from qt_material import apply_stylesheet  # to set not system style https://pypi.org/project/qt-material/#usage

from design import Ui_MainWindow  # import design file

matplotlib.use('Qt5Agg')  # says that we will be using matplotlib's qt widget for graphs


# Main window of my app
class MyWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # for init all staff from QMainWindow
        self.setupUi(self)  # for beauticode UI part forwarded to another file
        # so this line creates all items from revealed UI file

        # changing app icon
        self.setWindowIcon(QIcon('icon.png'))
        # connecting button with its functions
        self.Anim.clicked.connect(self.anim)
        # connecting button with its functions
        self.Build.clicked.connect(self.build)
        # connecting button with its functions
        self.polar.clicked.connect(self.to_polar_page)
        # connecting button with its functions
        self.Anim_2.clicked.connect(self.anim_2)
        # connecting button with its functions
        self.Build_2.clicked.connect(self.build_2)
        # connecting button with its functions
        self.descartes.clicked.connect(self.to_descartes_page)

    # start animation of graph in the descartes on clicking on button
    def anim(self):
        self.graph.anim()

    # start animation of graph in the polars on clicking on button
    def anim_2(self):
        self.graph_2.anim()

    # build animation of graph in the descartes on clicking on button
    def build(self):
        P = np.array([[self.x0.text(), self.y0.text()],  #
                      [self.x1.text(), self.y1.text()],
                      [self.x2.text(), self.y2.text()],
                      [self.x3.text(), self.y3.text()]],
                     dtype=np.dtype(float))
        self.graph.build(P)

    # build animation of graph in the polars on clicking on button
    def build_2(self):
        P = np.array([[self.r0.text(), self.a0.text()],
                      [self.r1.text(), self.a1.text()],
                      [self.r2.text(), self.a2.text()],
                      [self.r3.text(), self.a3.text()]],
                     dtype=np.dtype(float))
        self.graph_2.build(P)

    def to_polar_page(self):  # open polar form
        self.stackedWidget.setCurrentIndex(1)

    def to_descartes_page(self):  # open descartes form
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":  # starts app
    app = QtWidgets.QApplication([])  # create application
    apply_stylesheet(app, theme='dark_teal.xml')  # set custom theme
    widget = MyWidget()
    widget.show()  # show our main window

    sys.exit(app.exec())  # closing of app
