# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrushMateTM.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 90, 20, 671))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setBaseSize(QtCore.QSize(4, 510))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 741, 72))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Title = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Title.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.Title.setContentsMargins(0, 0, 0, 0)
        self.Title.setSpacing(0)
        self.Title.setObjectName("Title")
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.Title.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Title.addItem(spacerItem)
        self.titleLabel = QtWidgets.QLabel(self.layoutWidget)
        self.titleLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(36)
        font.setItalic(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setTextFormat(QtCore.Qt.RichText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.Title.addWidget(self.titleLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Title.addItem(spacerItem1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 76, 410))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.toolBar = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.toolBar.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.toolBar.setContentsMargins(0, 0, 0, 0)
        self.toolBar.setSpacing(7)
        self.toolBar.setObjectName("toolBar")
        self.mouseButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.mouseButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/mouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mouseButton.setIcon(icon)
        self.mouseButton.setIconSize(QtCore.QSize(30, 30))
        self.mouseButton.setObjectName("mouseButton")
        self.toolBar.addWidget(self.mouseButton)
        self.freehandButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.freehandButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/freehand.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.freehandButton.setIcon(icon1)
        self.freehandButton.setIconSize(QtCore.QSize(30, 30))
        self.freehandButton.setObjectName("freehandButton")
        self.toolBar.addWidget(self.freehandButton)
        self.eraserButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.eraserButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/eraser.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eraserButton.setIcon(icon2)
        self.eraserButton.setIconSize(QtCore.QSize(30, 30))
        self.eraserButton.setObjectName("eraserButton")
        self.toolBar.addWidget(self.eraserButton)
        self.shapesButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.shapesButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/shapes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shapesButton.setIcon(icon3)
        self.shapesButton.setIconSize(QtCore.QSize(30, 30))
        self.shapesButton.setObjectName("shapesButton")
        self.toolBar.addWidget(self.shapesButton)
        self.insertimgButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.insertimgButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/insert image icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insertimgButton.setIcon(icon4)
        self.insertimgButton.setIconSize(QtCore.QSize(30, 30))
        self.insertimgButton.setObjectName("insertimgButton")
        self.toolBar.addWidget(self.insertimgButton)
        self.stampButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.stampButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/stamp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stampButton.setIcon(icon5)
        self.stampButton.setIconSize(QtCore.QSize(30, 30))
        self.stampButton.setObjectName("stampButton")
        self.toolBar.addWidget(self.stampButton)
        self.paintbucketButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.paintbucketButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/paintbucket.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paintbucketButton.setIcon(icon6)
        self.paintbucketButton.setIconSize(QtCore.QSize(30, 30))
        self.paintbucketButton.setObjectName("paintbucketButton")
        self.toolBar.addWidget(self.paintbucketButton)
        self.paintbucketButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.paintbucketButton_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/addtext.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paintbucketButton_2.setIcon(icon7)
        self.paintbucketButton_2.setIconSize(QtCore.QSize(30, 30))
        self.paintbucketButton_2.setObjectName("paintbucketButton_2")
        self.toolBar.addWidget(self.paintbucketButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.toolBar.addItem(spacerItem2)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(100, 90, 661, 681))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "BrushMate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionFile.setText(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
