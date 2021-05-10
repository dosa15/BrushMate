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
drawingCircles = False

class GraphicsScene(QGraphicsScene):
    
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(0, 0, 660, 680)
        self.firstClickLine = True
        self.firstClickRect = True
        self.firstClickCircle = True
        self.start = self.end = QPointF(-1, -1)
        self.pen = QPen(Qt.black)

    def mousePressEvent(self, event):        
        global freeHand, freeHandDraw, drawingLines, drawingRects, drawingCircles
        
        if freeHand:
            freeHandDraw = True
            self.start = event.scenePos()

        if drawingLines:
            if self.firstClickLine:
                self.start = event.scenePos()
                self.firstClickLine = False
            else:
                self.end = event.scenePos()
                self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.pen)
                self.firstClickLine = True

        # if drawingRects:

        # if drawingCircles:
                
        else:
            self.firstClickLine = True
            self.firstClickRect = True
            self.firstClickCircle = True


    def mouseMoveEvent(self, event):
        global freeHand, freeHandDraw, drawingLines, drawingRects, drawingCircles

        if freeHandDraw:
            self.end = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.pen)
            self.start = self.end
    
    def mouseReleaseEvent(self, event):
        global freeHand, freeHandDraw, drawingLines, drawingRects, drawingCircles
        
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
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.mouseButton.setChecked(True)
        freeHand = drawingLines = drawingRects = drawingCircles = False


    def freehandClicked(self):
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.freehandButton.setChecked(True)
        drawingLines = drawingRects = drawingCircles = False

        if freeHand:
            freeHand = False
        else:
            freeHand = True


    def eraserClicked(self):
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.eraserButton.setChecked(True)
        freeHand = drawingLines = drawingRects = drawingCircles = False


    def assignShapesMenu(self):
        menu = QMenu(self.shapesButton, triggered=self.shapesClicked)
        for opt in ["", "Line", "Rectangle", "Circle"]:
            menu.addAction(opt)
        self.shapesButton.setMenu(menu)
    
    @QtCore.pyqtSlot(QtWidgets.QAction)
    def shapesClicked(self, action):
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.shapesButton.setChecked(True)
        freeHand = False
        
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


    def insertImgClicked(self):
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.insertImgButton.setChecked(True)
        freeHand = drawingLines = drawingRects = drawingCircles = False


    def insertTextClicked(self):
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.insertTextButton.setChecked(True)
        freeHand = drawingLines = drawingRects = drawingCircles = False


    def cloneStampClicked(self):
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.cloneStampButton.setChecked(True)
        freeHand = drawingLines = drawingRects = drawingCircles = False


    def floodfillClicked(self):
        global freeHand, drawingLines, drawingRects, drawingCircles
        self.uncheckAllButtons()
        self.floodfillButton.setChecked(True)
        freeHand = drawingLines = drawingRects = drawingCircles = False


    def uncheckAllButtons(self):
        self.mouseButton.setChecked(False)
        self.freehandButton.setChecked(False)
        self.eraserButton.setChecked(False)
        self.shapesButton.setChecked(False)
        self.insertImgButton.setChecked(False)
        self.insertTextButton.setChecked(False)
        self.cloneStampButton.setChecked(False)
        self.floodfillButton.setChecked(False)
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())

