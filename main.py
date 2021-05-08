from BrushMateTM import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random


class GraphicsScene(QGraphicsScene):
    
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(0, 0, 660, 680)
        self.pen = QPen(Qt.black)
        self.firstClick = True
        self.start = self.end = QPointF(0, 0)

    def mousePressEvent(self, event):
        if self.firstClick:
            self.start = event.pos()
            print("Start:", self.start)
            self.firstClick = False
        else:
            self.end = event.pos()
            print("End:", self.end)
            drawSomething = QGraphicsLineItem(QLineF(self.start, self.end))
            drawSomething.setPen(self.pen)
            print(drawSomething)
            self.addItem(drawSomething)
            self.firstClick = True

    # def mouseMoveEvent(self, event):
    #     self.cursorCurrentPosition = event.scenePos()
    #     current = QtCore.QPointF(self.cursorCurrentPosition.x(),self.cursorCurrentPosition.y())
    #     link = QtGui.QGraphicsLineItem(QtCore.QLineF(self.start, current))
    #     link.setPen(self.pen)
    #     self.scene.addItem(link)


class BrushMateWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.scene = GraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        
    '''
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(200,200)
        self.setMinimumSize(200,200)
        self.painter = QPainter(self.myPixmap)
        self.pen = QPen(Qt.black)
        self.painter.setPen(self.pen)
        self.painter.fillRect(0,0,200,200, Qt.white)
        self.graphicsView.setPixmap(self.myPixmap)
        self.last = None

    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.drawLine(self.last, event.pos())
            self.last = event.pos()
            self.graphicsView.setPixmap(self.myPixmap)
            self.update()

    def mousePressEvent(self, event):
        self.last = event.pos()

    def mouseReleaseEvent(self, event):
        self.last = None

    def updateSize(self, width, height):
        pm = QPixmap(width, height)
        pm.fill(Qt.white)
        old = self.myPixmap
        self.myPixmap = pm
        self.pen = QPen(Qt.black)
        self.painter = QPainter(pm)
        self.painter.drawPixmap(0,0,old)
        self.graphicsView.setPixmap(pm)

    def resizeEvent(self, event):
        if event.oldSize().width() > 0:
            self.updateSize(event.size().width(), event.size().height())
    '''


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())

