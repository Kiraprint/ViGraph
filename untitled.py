# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledTPvkhi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1068, 838)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_8 = QGridLayout(self.page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.graph = QLabel(self.page)
        self.graph.setObjectName(u"graph")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph.sizePolicy().hasHeightForWidth())
        self.graph.setSizePolicy(sizePolicy)
        self.graph.setMinimumSize(QSize(721, 711))
        self.graph.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.graph, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.y2l = QLabel(self.page)
        self.y2l.setObjectName(u"y2l")
        self.y2l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y2l, 9, 0, 1, 1)

        self.x3l = QLabel(self.page)
        self.x3l.setObjectName(u"x3l")
        self.x3l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x3l, 11, 0, 1, 1)

        self.x1 = QLineEdit(self.page)
        self.x1.setObjectName(u"x1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.x1.sizePolicy().hasHeightForWidth())
        self.x1.setSizePolicy(sizePolicy1)
        self.x1.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x1, 5, 1, 1, 1)

        self.y1l = QLabel(self.page)
        self.y1l.setObjectName(u"y1l")
        self.y1l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y1l, 6, 0, 1, 1)

        self.y3 = QLineEdit(self.page)
        self.y3.setObjectName(u"y3")
        sizePolicy1.setHeightForWidth(self.y3.sizePolicy().hasHeightForWidth())
        self.y3.setSizePolicy(sizePolicy1)
        self.y3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y3, 12, 1, 1, 1)

        self.x0l = QLabel(self.page)
        self.x0l.setObjectName(u"x0l")
        self.x0l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x0l, 2, 0, 1, 1)

        self.x0 = QLineEdit(self.page)
        self.x0.setObjectName(u"x0")
        sizePolicy1.setHeightForWidth(self.x0.sizePolicy().hasHeightForWidth())
        self.x0.setSizePolicy(sizePolicy1)
        self.x0.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x0, 2, 1, 1, 1)

        self.y1 = QLineEdit(self.page)
        self.y1.setObjectName(u"y1")
        sizePolicy1.setHeightForWidth(self.y1.sizePolicy().hasHeightForWidth())
        self.y1.setSizePolicy(sizePolicy1)
        self.y1.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y1, 6, 1, 1, 1)

        self.y3l = QLabel(self.page)
        self.y3l.setObjectName(u"y3l")
        self.y3l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y3l, 12, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 10, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 1, 1, 1)

        self.x2 = QLineEdit(self.page)
        self.x2.setObjectName(u"x2")
        sizePolicy1.setHeightForWidth(self.x2.sizePolicy().hasHeightForWidth())
        self.x2.setSizePolicy(sizePolicy1)
        self.x2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x2, 8, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 1, 1, 1)

        self.y2 = QLineEdit(self.page)
        self.y2.setObjectName(u"y2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.y2.sizePolicy().hasHeightForWidth())
        self.y2.setSizePolicy(sizePolicy2)
        self.y2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y2, 9, 1, 1, 1)

        self.x2l = QLabel(self.page)
        self.x2l.setObjectName(u"x2l")
        self.x2l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x2l, 8, 0, 1, 1)

        self.y0 = QLineEdit(self.page)
        self.y0.setObjectName(u"y0")
        sizePolicy1.setHeightForWidth(self.y0.sizePolicy().hasHeightForWidth())
        self.y0.setSizePolicy(sizePolicy1)
        self.y0.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y0, 3, 1, 1, 1)

        self.x1l = QLabel(self.page)
        self.x1l.setObjectName(u"x1l")
        sizePolicy1.setHeightForWidth(self.x1l.sizePolicy().hasHeightForWidth())
        self.x1l.setSizePolicy(sizePolicy1)
        self.x1l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x1l, 5, 0, 1, 1)

        self.x3 = QLineEdit(self.page)
        self.x3.setObjectName(u"x3")
        sizePolicy1.setHeightForWidth(self.x3.sizePolicy().hasHeightForWidth())
        self.x3.setSizePolicy(sizePolicy1)
        self.x3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.x3, 11, 1, 1, 1)

        self.y0l = QLabel(self.page)
        self.y0l.setObjectName(u"y0l")
        self.y0l.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.y0l, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.Build = QPushButton(self.page)
        self.Build.setObjectName(u"Build")
        sizePolicy1.setHeightForWidth(self.Build.sizePolicy().hasHeightForWidth())
        self.Build.setSizePolicy(sizePolicy1)
        self.Build.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.Build)

        self.Anim = QPushButton(self.page)
        self.Anim.setObjectName(u"Anim")
        self.Anim.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Anim.sizePolicy().hasHeightForWidth())
        self.Anim.setSizePolicy(sizePolicy1)
        self.Anim.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.Anim)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 2)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_11 = QGridLayout(self.page_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SetNoConstraint)
        self.graph_2 = QLabel(self.page_2)
        self.graph_2.setObjectName(u"graph_2")
        sizePolicy.setHeightForWidth(self.graph_2.sizePolicy().hasHeightForWidth())
        self.graph_2.setSizePolicy(sizePolicy)
        self.graph_2.setMinimumSize(QSize(721, 711))
        self.graph_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_9.addWidget(self.graph_2, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_5, 4, 1, 1, 1)

        self.y2l_2 = QLabel(self.page_2)
        self.y2l_2.setObjectName(u"y2l_2")
        self.y2l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.y2l_2, 9, 0, 1, 1)

        self.x3l_2 = QLabel(self.page_2)
        self.x3l_2.setObjectName(u"x3l_2")
        self.x3l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.x3l_2, 11, 0, 1, 1)

        self.R1 = QLineEdit(self.page_2)
        self.R1.setObjectName(u"R1")
        sizePolicy1.setHeightForWidth(self.R1.sizePolicy().hasHeightForWidth())
        self.R1.setSizePolicy(sizePolicy1)
        self.R1.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.R1, 5, 1, 1, 1)

        self.y1l_2 = QLabel(self.page_2)
        self.y1l_2.setObjectName(u"y1l_2")
        self.y1l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.y1l_2, 6, 0, 1, 1)

        self.a3 = QLineEdit(self.page_2)
        self.a3.setObjectName(u"a3")
        sizePolicy1.setHeightForWidth(self.a3.sizePolicy().hasHeightForWidth())
        self.a3.setSizePolicy(sizePolicy1)
        self.a3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.a3, 12, 1, 1, 1)

        self.x0l_2 = QLabel(self.page_2)
        self.x0l_2.setObjectName(u"x0l_2")
        self.x0l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.x0l_2, 2, 0, 1, 1)

        self.R0 = QLineEdit(self.page_2)
        self.R0.setObjectName(u"R0")
        sizePolicy1.setHeightForWidth(self.R0.sizePolicy().hasHeightForWidth())
        self.R0.setSizePolicy(sizePolicy1)
        self.R0.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.R0, 2, 1, 1, 1)

        self.a1 = QLineEdit(self.page_2)
        self.a1.setObjectName(u"a1")
        sizePolicy1.setHeightForWidth(self.a1.sizePolicy().hasHeightForWidth())
        self.a1.setSizePolicy(sizePolicy1)
        self.a1.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.a1, 6, 1, 1, 1)

        self.y3l_2 = QLabel(self.page_2)
        self.y3l_2.setObjectName(u"y3l_2")
        self.y3l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.y3l_2, 12, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_8, 10, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_9, 7, 1, 1, 1)

        self.r2 = QLineEdit(self.page_2)
        self.r2.setObjectName(u"r2")
        sizePolicy1.setHeightForWidth(self.r2.sizePolicy().hasHeightForWidth())
        self.r2.setSizePolicy(sizePolicy1)
        self.r2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.r2, 8, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_10, 13, 1, 1, 1)

        self.a2 = QLineEdit(self.page_2)
        self.a2.setObjectName(u"a2")
        sizePolicy2.setHeightForWidth(self.a2.sizePolicy().hasHeightForWidth())
        self.a2.setSizePolicy(sizePolicy2)
        self.a2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.a2, 9, 1, 1, 1)

        self.x2l_2 = QLabel(self.page_2)
        self.x2l_2.setObjectName(u"x2l_2")
        self.x2l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.x2l_2, 8, 0, 1, 1)

        self.a0 = QLineEdit(self.page_2)
        self.a0.setObjectName(u"a0")
        sizePolicy1.setHeightForWidth(self.a0.sizePolicy().hasHeightForWidth())
        self.a0.setSizePolicy(sizePolicy1)
        self.a0.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.a0, 3, 1, 1, 1)

        self.x1l_2 = QLabel(self.page_2)
        self.x1l_2.setObjectName(u"x1l_2")
        sizePolicy1.setHeightForWidth(self.x1l_2.sizePolicy().hasHeightForWidth())
        self.x1l_2.setSizePolicy(sizePolicy1)
        self.x1l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.x1l_2, 5, 0, 1, 1)

        self.r3 = QLineEdit(self.page_2)
        self.r3.setObjectName(u"r3")
        sizePolicy1.setHeightForWidth(self.r3.sizePolicy().hasHeightForWidth())
        self.r3.setSizePolicy(sizePolicy1)
        self.r3.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.r3, 11, 1, 1, 1)

        self.y0l_2 = QLabel(self.page_2)
        self.y0l_2.setObjectName(u"y0l_2")
        self.y0l_2.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_10.addWidget(self.y0l_2, 3, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_11, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_10)

        self.Build_2 = QPushButton(self.page_2)
        self.Build_2.setObjectName(u"Build_2")
        sizePolicy1.setHeightForWidth(self.Build_2.sizePolicy().hasHeightForWidth())
        self.Build_2.setSizePolicy(sizePolicy1)
        self.Build_2.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_3.addWidget(self.Build_2)

        self.Anim_2 = QPushButton(self.page_2)
        self.Anim_2.setObjectName(u"Anim_2")
        self.Anim_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Anim_2.sizePolicy().hasHeightForWidth())
        self.Anim_2.setSizePolicy(sizePolicy1)
        self.Anim_2.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_3.addWidget(self.Anim_2)


        self.gridLayout_9.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 2, 0, 1, 2)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_9.addWidget(self.label_10, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_7.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1068, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy3)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ViGraph", None))
        self.graph.setText("")
        self.y2l.setText(QCoreApplication.translate("MainWindow", u"Y2", None))
        self.x3l.setText(QCoreApplication.translate("MainWindow", u"X3", None))
        self.y1l.setText(QCoreApplication.translate("MainWindow", u"Y1", None))
        self.x0l.setText(QCoreApplication.translate("MainWindow", u"X0", None))
        self.y3l.setText(QCoreApplication.translate("MainWindow", u"Y3", None))
        self.x2l.setText(QCoreApplication.translate("MainWindow", u"X2", None))
        self.x1l.setText(QCoreApplication.translate("MainWindow", u"X1", None))
        self.y0l.setText(QCoreApplication.translate("MainWindow", u"Y0", None))
        self.Build.setText(QCoreApplication.translate("MainWindow", u"Build", None))
        self.Anim.setText(QCoreApplication.translate("MainWindow", u"Anim", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Descartes system", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"To change system click on the arrows", None))
        self.graph_2.setText("")
        self.y2l_2.setText(QCoreApplication.translate("MainWindow", u"a2", None))
        self.x3l_2.setText(QCoreApplication.translate("MainWindow", u"R3", None))
        self.y1l_2.setText(QCoreApplication.translate("MainWindow", u"a1", None))
        self.x0l_2.setText(QCoreApplication.translate("MainWindow", u"R0", None))
        self.y3l_2.setText(QCoreApplication.translate("MainWindow", u"a3", None))
        self.x2l_2.setText(QCoreApplication.translate("MainWindow", u"R2", None))
        self.x1l_2.setText(QCoreApplication.translate("MainWindow", u"R1", None))
        self.y0l_2.setText(QCoreApplication.translate("MainWindow", u"a0", None))
        self.Build_2.setText(QCoreApplication.translate("MainWindow", u"Build", None))
        self.Anim_2.setText(QCoreApplication.translate("MainWindow", u"Anim", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Polar system (R - length of vector, a - angle in radians)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"To change system click on the arrows", None))
    # retranslateUi

