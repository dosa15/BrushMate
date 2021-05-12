from BrushMateTM import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random

freeHand = False
freeHandDraw = False
drawingLines = False
drawingRects = False
drawingSquares = False
drawingCircles = False
drawingEllipses = False

class GraphicsScene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(0, 0, 660, 680)
        self.setAllFirstClicksTrue()
        self.start = self.end = QPointF(-1, -1)
        self.pen = QPen(Qt.black)

    def setAllFirstClicksTrue(self):
        self.firstClickLine = True
        self.firstClickRect = True
        self.firstClickSquare = True
        self.firstClickCircle = True
        self.firstClickEllipse = True

    def mousePressEvent(self, event):
        global freeHand, freeHandDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses

        if freeHand:
            freeHandDraw = True
            self.start = event.scenePos()

        elif drawingLines:
            if self.firstClickLine:
                self.start = event.scenePos()
                self.firstClickLine = False
            else:
                self.end = event.scenePos()
                self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.pen)
                self.firstClickLine = True

        elif drawingRects:
            if self.firstClickRect:
                self.start = event.scenePos()
                self.firstClickRect = False
            else:
                self.end = event.scenePos()
                if(self.start.x()>self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y()>self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                self.addRect(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())))
                self.firstClickRect = True

        elif drawingSquares:
            if self.firstClickSquare:
                self.start = event.scenePos()
                self.firstClickRect = False
            else:
                self.end = event.scenePos()
                if(self.start.x() == self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y() == self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                self.addRect(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())))
                self.firstClickSquare = True

        elif drawingCircles:
            if self.firstClickCircle:
                self.start = event.scenePos()
                self.firstClickCircle = False
            else:
                self.end = event.scenePos()
                if(self.start.x() == self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y() == self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                self.addEllipse(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())))
                self.firstClickCircle = True

        elif drawingEllipses:
            if self.firstClickEllipse:
                self.start = event.scenePos()
                self.firstClickEllipse = False
            else:
                self.end = event.scenePos()
                if(self.start.x()>self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y()>self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                self.addEllipse(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())))
                self.firstClickEllipse = True

        else:
            self.setAllFirstClicksTrue()


    def mouseMoveEvent(self, event):
        global freeHand, freeHandDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses

        if freeHandDraw:
            self.end = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.pen)
            self.start = self.end

    def mouseReleaseEvent(self, event):
        global freeHand, freeHandDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses

        if freeHandDraw:
            freeHandDraw = False


class BrushMateWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(BrushMateWindow, self).__init__(parent)
        self.setupUi(self)
        self.scene = GraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.mouseButton.setChecked(True)
        self.mouseButton.clicked.connect(self.mouseClicked)
        self.freehandButton.clicked.connect(self.freehandClicked)
        self.eraserButton.clicked.connect(self.eraserClicked)
        self.assignShapesMenu()
        self.insertImgButton.clicked.connect(self.insertImgClicked)
        self.insertTextButton.clicked.connect(self.insertTextClicked)
        self.cloneStampButton.clicked.connect(self.cloneStampClicked)
        self.floodfillButton.clicked.connect(self.floodfillClicked)


    def mouseClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.mouseButton.setChecked(True)
        self.setallFalse()


    def freehandClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.freehandButton.setChecked(True)
        self.setallFalse()

        if freeHand:
            freeHand = False
        else:
            freeHand = True


    def eraserClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.eraserButton.setChecked(True)
        self.setallFalse()


    def assignShapesMenu(self):
        menu = QMenu(self.shapesButton, triggered=self.shapesClicked)
        for opt in ["", "Line", "Rectangle", "Square", "Circle", "Ellipse"]:
            menu.addAction(opt)
        self.shapesButton.setMenu(menu)

    @QtCore.pyqtSlot(QtWidgets.QAction)
    def shapesClicked(self, action):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.shapesButton.setChecked(True)

        self.setallFalse()
        if action.text() == "Line":
            drawingLines = True
        elif action.text() == "Rectangle":
            drawingRects = True
        elif action.text() == "Square":
            drawingSquares = True
        elif action.text() == "Circle":
            drawingCircles = True
        elif action.text() == "Ellipse":
            drawingEllipses = True


    def insertImgClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.insertImgButton.setChecked(True)
        self.setallFalse()


    def insertTextClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.insertTextButton.setChecked(True)
        self.setallFalse()


    def cloneStampClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.cloneStampButton.setChecked(True)
        self.setallFalse()


    def floodfillClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.floodfillButton.setChecked(True)
        self.setallFalse()


    def uncheckAllButtons(self):
        self.mouseButton.setChecked(False)
        self.freehandButton.setChecked(False)
        self.eraserButton.setChecked(False)
        self.shapesButton.setChecked(False)
        self.insertImgButton.setChecked(False)
        self.insertTextButton.setChecked(False)
        self.cloneStampButton.setChecked(False)
        self.floodfillButton.setChecked(False)

    def setallFalse(self):
        freeHand = drawingLines = drawingRects = drawingSquares = drawingCircles = drawingEllipses = False


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())
