# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 733)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 691))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.graph.setText("")
        self.graph.setObjectName("graph")
        self.horizontalLayout.addWidget(self.graph)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(739, -1, 251, 521))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.x1l = QtWidgets.QLabel(self.formLayoutWidget)
        self.x1l.setObjectName("x1l")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.x1l)
        self.x1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.x1.setObjectName("x1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.x1)
        self.y1l = QtWidgets.QLabel(self.formLayoutWidget)
        self.y1l.setObjectName("y1l")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.y1l)
        self.y1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.y1.setObjectName("y1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.y1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.x2l = QtWidgets.QLabel(self.formLayoutWidget)
        self.x2l.setObjectName("x2l")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.x2l)
        self.x2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.x2.setObjectName("x2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.x2)
        self.y2l = QtWidgets.QLabel(self.formLayoutWidget)
        self.y2l.setObjectName("y2l")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.y2l)
        self.y2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.y2.setObjectName("y2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.y2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.x3l = QtWidgets.QLabel(self.formLayoutWidget)
        self.x3l.setObjectName("x3l")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.x3l)
        self.x3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.x3.setObjectName("x3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.x3)
        self.y3l = QtWidgets.QLabel(self.formLayoutWidget)
        self.y3l.setObjectName("y3l")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.y3l)
        self.y3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.y3.setObjectName("y3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.y3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.x4l = QtWidgets.QLabel(self.formLayoutWidget)
        self.x4l.setObjectName("x4l")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.x4l)
        self.x4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.x4.setObjectName("x4")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.x4)
        self.y4l = QtWidgets.QLabel(self.formLayoutWidget)
        self.y4l.setObjectName("y4l")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.y4l)
        self.y6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.y6.setObjectName("y6")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.y6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.d1l = QtWidgets.QLabel(self.formLayoutWidget)
        self.d1l.setObjectName("d1l")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.d1l)
        self.d1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.d1.setObjectName("d1")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.d1)
        self.d2l = QtWidgets.QLabel(self.formLayoutWidget)
        self.d2l.setObjectName("d2l")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.d2l)
        self.d2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.d2.setObjectName("d2")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.d2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(739, 519, 251, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.x1l.setText(_translate("MainWindow", "x1"))
        self.y1l.setText(_translate("MainWindow", "y1"))
        self.x2l.setText(_translate("MainWindow", "x2"))
        self.y2l.setText(_translate("MainWindow", "y2"))
        self.x3l.setText(_translate("MainWindow", "x3"))
        self.y3l.setText(_translate("MainWindow", "y3"))
        self.x4l.setText(_translate("MainWindow", "x4"))
        self.y4l.setText(_translate("MainWindow", "y4"))
        self.d1l.setText(_translate("MainWindow", "d1"))
        self.d2l.setText(_translate("MainWindow", "d2"))
        self.pushButton_2.setText(_translate("MainWindow", "Build"))
        self.pushButton.setText(_translate("MainWindow", "Anim"))
