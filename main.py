from BrushMateTM import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys, random


class BrushMateWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        brush = QtGui.QBrush(QtCore.Qt.white)
        self.scene.setBackgroundBrush(QtBrush=brush, QColor=QtCore.Qt.white)
        # self.pen = QtGui.QPen(QtCore.Qt.green)
        # self.scene.addRect(QtCore.QRectF(0, 0, 100, 200), QtGui.QPen(QtCore.Qt.blue), QtGui.QBrush(QtCore.Qt.green))
    
    # def paintEvent(self, e):
    #     qp = QPainter()
    #     qp.begin(self)
    #     self.drawPoints(qp)
    #     qp.end()

    # def drawPoints(self, qp):
    #     qp.setPen(Qt.red)
    #     size = self.size()

    #     if size.height() <= 1 or size.height() <= 1:
    #         return

    #     for i in range(1000):
    #         x = random.randint(1, size.width() - 1)
    #         y = random.randint(1, size.height() - 1)
    def paintEvent(self, event):
        painter = QPainter()
        painter.setPen(QtGui.QPen(Qt.green,  8, Qt.DashLine))
        painter.drawEllipse(40, 40, 400, 400)
        # return super().paintEvent(self, QPaintEvent)
    


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main_1_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

