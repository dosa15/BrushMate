from BrushMateTM import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random

drawingLines = False
drawingRects = False
drawingCircles = False

class GraphicsScene(QGraphicsScene):
    
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(0, 0, 660, 680)
        self.firstClickLine = True
        self.firstClickRect = True
        self.firstClickCircle = True
        self.start = self.end = QPointF(-1, -1)
        print(parent)

    def mousePressEvent(self, event):        
        global drawingLines, drawingRects, drawingCircles
        if drawingLines:
            self.pen = QPen(Qt.black)
            if self.firstClickLine:
                self.start = event.scenePos()
                self.firstClickLine = False
            else:
                self.end = event.scenePos()
                drawSomething = QGraphicsLineItem(QLineF(self.start, self.end))
                drawSomething.setPen(self.pen)
                self.addItem(drawSomething)
                self.firstClickLine = True
                
        else:
            self.firstClickLine = True
            self.firstClickRect = True
            self.firstClickCircle = True


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
        self.scene = GraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.assignShapesMenu()


    def assignShapesMenu(self):
        menu = QMenu(self.shapesButton, triggered=self.shapesClicked)
        for opt in ["", "Line", "Rectangle", "Circle"]:
            menu.addAction(opt)
        self.shapesButton.setMenu(menu)
    
    @QtCore.pyqtSlot(QtWidgets.QAction)
    def shapesClicked(self, action):
        global drawingLines, drawingRects, drawingCircles
        if not action.text():
            drawingLines = drawingRects = drawingCircles = False
        elif action.text() == "Line":
            drawingLines = True
            drawingRects = False
            drawingCircles = False
        elif action.text() == "Rectangle":
            drawingLines = False
            drawingRects = True
            drawingCircles = False
        elif action.text() == "Circle":
            drawingLines = False
            drawingRects = False
            drawingCircles = True
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())

