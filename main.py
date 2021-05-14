from BrushMateTM import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, random

freeHand = False
freeHandDraw = False
eraser = False
eraserDraw = False
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
        self.pen.setCapStyle(Qt.RoundCap)
        self.eraser = QPen(Qt.color0, 25) # Color0 is automatically set as the color of the background
        self.eraser.setCapStyle(Qt.RoundCap)

    def setAllFirstClicksTrue(self):
        self.firstClickLine = True
        self.firstClickRect = True
        self.firstClickSquare = True
        self.firstClickCircle = True
        self.firstClickEllipse = True

    def mousePressEvent(self, event):
        global freeHand, freeHandDraw, eraser, eraserDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses

        if freeHand:
            freeHandDraw = True
            self.start = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.start.x(), self.start.y(), pen=self.pen)

        elif eraser:
            eraserDraw = True
            self.start = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.start.x(), self.start.y(), pen=self.eraser)

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
                self.firstClickSquare = False
            else:
                self.end = event.scenePos()
                if(self.start.x() > self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y() > self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                if(self.end.x() - self.start.x() > self.end.y() - self.start.y()):
                    self.end.setX(self.end.x + self.end.y - self.start.y)
                if(self.end.x() - self.start.x() < self.end.y() - self.start.y()):
                    self.end.setY(self.end.y + self.end.x - self.start.y)
                if(self.end.x() - self.start.x() == self.end.y() - self.start.y()):
                    self.addRect(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())))
                self.firstClickSquare = True

        elif drawingCircles:
            if self.firstClickCircle:
                self.start = event.scenePos()
                self.firstClickCircle = False
            else:
                self.end = event.scenePos()
                if(self.start.x() > self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y() > self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                if(self.end.x() - self.start.x() > self.end.y() - self.start.y()):
                    self.end.setX(self.end.x + self.end.y - self.start.y)
                if(self.end.x() - self.start.x() < self.end.y() - self.start.y()):
                    self.end.setY(self.end.y + self.end.x - self.start.y)
                if(self.end.x() - self.start.x() == self.end.y() - self.start.y()):
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
        global freeHand, freeHandDraw, eraser, eraserDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses

        if freeHandDraw:
            self.end = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.pen)
            self.start = self.end
        
        if eraserDraw:
            self.end = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.eraser)
            self.start = self.end

    def mouseReleaseEvent(self, event):
        global freeHand, freeHandDraw, eraser, eraserDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses

        if freeHandDraw:
            freeHandDraw = False
        
        if eraserDraw:
            eraserDraw = False

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class BrushMateWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(BrushMateWindow, self).__init__(parent)
        self.setupUi(self)
        self.scene = GraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(Qt.white))
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
        self.insertImgButton.clicked.connect(self.insertImgClicked)

        self.graphicsView.setCursor(Qt.CrossCursor)

        self.retranslateUi(Ui_MainWindow)
        QMetaObject.connectSlotsByName(self)

        self.filename = None
        self.actionSave.triggered.connect(self.fileSave)
        self.actionSave_As.triggered.connect(lambda: self.fileSave(saveAs=True))

        self.w = None  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        self.actionSave.setShortcut(_translate("Ui_MainWindow", "Ctrl+S"))
        self.actionSave_As.setShortcut(_translate("Ui_MainWindow", "Ctrl+Shift+S"))

    def mouseClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.mouseButton.setChecked(True)
        self.setallFalse()


    def freehandClicked(self):
        global freeHand, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.freehandButton.setChecked(True)
        self.setallFalse()
        freeHand = True


    def eraserClicked(self):
        global freeHand, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        self.uncheckAllButtons()
        self.eraserButton.setChecked(True)
        self.setallFalse()
        eraser = True


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
        
        imagePath = QFileDialog.getOpenFileName(caption="Open File", directory="",filter="Images (*.jpg *.jpeg *.png)")
        # Load the image and resize it to fit the QGraphicsScene
        image = QPixmap.fromImage(QImage(imagePath[0]).scaled(int(self.scene.width()), int(self.scene.height()), aspectRatioMode=Qt.KeepAspectRatio))
        self.scene.addPixmap(image)


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
        global freeHand, freeHandDraw, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses
        freeHand = eraser = drawingLines = drawingRects = drawingSquares = drawingCircles = drawingEllipses = False


    def fileSave(self, saveAs=False):
        area = self.scene.sceneRect()
        image = QImage(area.width(), area.height(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(image)
        imageRect = image.rect().getRect()
        imageRect = QRectF(*imageRect)
        painter.setRenderHint(QPainter.Antialiasing)
        self.scene.render(painter, imageRect, area)
        painter.end()

        if self.filename == None or saveAs:
            getFile, ok = QInputDialog.getText(self, 'Save As', 'Enter the name of your BrushMate project (.jpg, .jpeg, .png):')
            if ok:
                getFile = getFile.split('.')
                self.filename = getFile[0]
                if len(getFile) > 1 and getFile[1] in ("jpg", "jpeg", "png"):
                    self.filename += "." + getFile[1]
                else:
                    self.filename += ".jpeg"

        if self.filename is not None:
            image.save(self.filename)
            print("saved as " + self.filename)
        # fileInfo = QFormLayout()
        # queryLabel = QLabel('Enter the name of your BrushMate file:')
        # file = QLineEdit()
        # filetype = QComboBox()
        # filetype.addItems([".jpg", ".jpeg", ".png"])
        # filetype.currentIndexChanged.connect(self.chooseFileType)

        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())
