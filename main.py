from BrushMateTM import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random

drawingLines = False

class GraphicsScene(QGraphicsScene):
    
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        
        global drawingLines
        
        self.setSceneRect(0, 0, 660, 680)
        self.firstClick = True
        self.start = self.end = QPointF(0, 0)
        print(parent)

    def mousePressEvent(self, event):        
        # if drawingLines:
        self.pen = QPen(Qt.black)
        if self.firstClick:
            self.start = event.scenePos()
            self.firstClick = False
        else:
            self.end = event.scenePos()
            drawSomething = QGraphicsLineItem(QLineF(self.start, self.end))
            drawSomething.setPen(self.pen)
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
        super(BrushMateWindow, self).__init__(parent)
        self.setupUi(self)
        
        global drawingLines
        
        self.scene = GraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # If the 'shapes' Button is pressed, enable drawing lines, else disable drawing lines
        if self.shapesButton.isFlat():
            self.shapesButton.setFlat(True)
            drawingLines = True
        else:
            self.shapesButton.setFlat(False)
            drawingLines = False


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())

