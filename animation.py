from PySide6 import QtWidgets, QtCore, QtGui


class Graph(QtWidgets.QLabel):
    def __init__(self):
        super(Graph, self).__init__()

        trashGif = open('animation.gif', 'rb').read()
        self.gifByteArray = QtCore.QByteArray(trashGif)
        self.gifBuffer = QtCore.QBuffer(self.gifByteArray)
        self.movie = QtGui.QMovie()
        self.movie.setFormat('GIF')
        self.movie.setDevice(self.gifBuffer)
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.setMovie(self.movie)
        self.movie.jumpToFrame(0)


