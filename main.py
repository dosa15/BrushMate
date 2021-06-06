from BrushMateTM import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from numba import njit
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
drawingPenSize = 1
changedPenSize = False
insertingImg = False
moveImg = False
movingImg = False
imageToMove = None
insertingText = False
floodFill = False
textboxContents = ""
cloneStamping = False


class GraphicsScene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self.setSceneRect(0, 0, 660, 680)
        self.setAllFirstClicksTrue()
        self.start = self.end = QPointF(-1, -1)
        self.color = Qt.black
        self.pen = QPen(self.color)
        self.pen.setCapStyle(Qt.RoundCap)
        self.eraser = QPen(Qt.color0, 25) # Color0 is automatically set as the color of the background
        self.eraser.setCapStyle(Qt.RoundCap)
        self.cloneImage = QImage()

    def setAllFirstClicksTrue(self):
        self.firstClickLine = True
        self.firstClickRect = True
        self.firstClickSquare = True
        self.firstClickCircle = True
        self.firstClickEllipse = True
        self.firstClickText = True
        self.firstClickStamp = True

    # @njit(nopython=True)
    def mousePressEvent(self, event):
        global freeHand, freeHandDraw, eraser, eraserDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, moveImg, movingImg, imageToMove, insertingText, floodFill

        if moveImg and imageToMove is not None:
            # self.setCursor(Qt.ArrowCursor)
            imgBounds = imageToMove.boundingRect().getCoords()
            x1, y1, x2, y2 = imgBounds
            currentPos = event.scenePos()
            if currentPos.x() > x1 and currentPos.x() < x2 and currentPos.y() > y1 and currentPos.y() < y2:
                if currentPos.x() < x1+10 and currentPos.x() > x2-10 and currentPos.y() < y1+10 and currentPos.y() > y2-10:
                    scaleImg = True
                else:
                    movingImg = True
                self.start = event.scenePos()
                # self.setCursor(Qt.OpenHandCursor)
        
        elif freeHand:
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
                self.addRect(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())), pen=self.pen)
                self.firstClickRect = True

        elif drawingSquares:
            if self.firstClickSquare:
                self.start = event.scenePos()
                self.firstClickSquare = False
            else:
                self.end = event.scenePos()
                if(abs(self.end.x() - self.start.x()) > abs(self.end.y() - self.start.y())):
                    self.end.setX(self.start.x() + self.end.y() - self.start.y())
                elif(abs(self.end.x() - self.start.x()) < abs(self.end.y() - self.start.y())):
                    self.end.setY(self.start.y() + self.end.x() - self.start.x())
                if(self.start.x() > self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y() > self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                self.addRect(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())), pen=self.pen)
                self.firstClickSquare = True

        elif drawingCircles:
            if self.firstClickCircle:
                self.start = event.scenePos()
                self.firstClickCircle = False
            else:
                self.end = event.scenePos()
                if(abs(self.end.x() - self.start.x()) > abs(self.end.y() - self.start.y())):
                    self.end.setX(self.start.x() + self.end.y() - self.start.y())
                elif(abs(self.end.x() - self.start.x()) < abs(self.end.y() - self.start.y())):
                    self.end.setY(self.start.y() + self.end.x() - self.start.x())
                if(self.start.x() > self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y() > self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                self.addEllipse(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())), pen=self.pen)
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
                self.addEllipse(QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y())), pen=self.pen)
                self.firstClickEllipse = True

        elif insertingText:
            global textboxContents
            self.addText(textboxContents).setPos(event.scenePos())
            #textBox.setPos(event.scenePos().x, event.scenePos.y)
            #textItem.setPos(self.start)

        elif cloneStamping:
            if self.firstClickStamp:
                self.start = event.scenePos()
                self.firstClickStamp = False
                self.secondClickStamp = True
            elif self.secondClickStamp:
                self.end = event.scenePos()
                if(self.start.x()>self.end.x()):
                    self.start.x,self.end.x=self.end.x,self.start.x
                if(self.start.y()>self.end.y()):
                    self.start.y,self.end.y=self.end.y,self.start.y
                selectedArea = QRectF(QPointF(self.start.x(), self.start.y()),QPointF(self.end.x(), self.end.y()))
                self.cloneImage = QImage(selectedArea.width(), selectedArea.height(), QImage.Format_ARGB32_Premultiplied)
                clonePainter = QPainter(self.cloneImage)
                cloneImageRect = self.cloneImage.rect().getRect()
                cloneImageRect = QRectF(*cloneImageRect)
                clonePainter.setRenderHint(QPainter.Antialiasing)
                self.render(clonePainter, cloneImageRect, selectedArea)
                clonePainter.end()
                self.secondClickStamp = False
            else:
                cloneImageItem = QGraphicsPixmapItem(QPixmap.fromImage(self.cloneImage))
                cloneImageItem.setPos(event.scenePos())
                self.addItem(cloneImageItem)
                self.firstClickStamp = True

        elif floodFill:
            self.start = event.scenePos()

            paintDevice = QPixmap(int(self.sceneRect().width()), int(self.sceneRect().height()))
            painter = QPainter(paintDevice)
            self.render(painter)
            pixelMap = paintDevice.toImage()

            buffer = []
            buffer.append([self.start.x(), self.start.y()])

            bgColor = pixelMap.pixelColor(int(self.start.x()), int(self.start.y()))
            try:
                pixelMap.setPixelColor(int(self.start.x()), int(self.start.y()), self.color)

                while len(buffer) > 0:

                    currentPixel = buffer.pop()
                    # print(currPixel)
                    currentX = currentPixel[0]
                    currentY = currentPixel[1]

                    if self.canFlood(pixelMap, currentX + 1, currentY, bgColor, self.color):
                        pixelMap.setPixelColor(int(currentX + 1), int(currentY), self.color)
                        buffer.append([int(currentX + 1), int(currentY)])

                    if self.canFlood(pixelMap, currentX, currentY + 1, bgColor, self.color):
                        pixelMap.setPixelColor(int(currentX), int(currentY + 1), self.color)
                        buffer.append([int(currentX), int(currentY + 1)])

                    if self.canFlood(pixelMap, currentX-1, currentY, bgColor, self.color):
                        pixelMap.setPixelColor(int(currentX-1), int(currentY), self.color)
                        buffer.append([int(currentX - 1), int(currentY)])

                    if self.canFlood(pixelMap, currentX, currentY-1, bgColor, self.color):
                        pixelMap.setPixelColor(int(currentX), int(currentY-1), self.color)
                        buffer.append([int(currentX), int(currentY - 1)])
                self.addPixmap(QPixmap(pixelMap))
            except:
                print(bgColor)
            painter.end()

        else:
            self.setAllFirstClicksTrue()


    def mouseMoveEvent(self, event):
        global freeHand, freeHandDraw, eraser, eraserDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, moveImg, movingImg, imageToMove, insertingText, floodFill

        if movingImg:
            self.end = event.scenePos()
            transformation = QTransform()
            transformation.translate(self.end.x() - self.start.x(), self.end.y() - self.start.y())
            imageToMove.setTransform(transformation)

        if freeHandDraw:
            self.end = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.pen)
            self.start = self.end

        if eraserDraw:
            self.end = event.scenePos()
            self.addLine(self.start.x(), self.start.y(), self.end.x(), self.end.y(), pen=self.eraser)
            self.start = self.end
        

    def mouseReleaseEvent(self, event):
        global freeHand, freeHandDraw, eraser, eraserDraw, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, moveImg, movingImg, imageToMove, insertingText, floodFill

        if movingImg:
            # transformation = QTransform()
            # transformation.translate(self.end.x() - self.start.x(), self.end.y() - self.start.y())
            # imageToMove.setTransform(transformation)
            # imageToMove.setPos(imageToMove.scenePos())
            print(imageToMove)
            print(self.start, self.end)
            # self.setCursor(Qt.CrossCursor)
            movingImg = False

        if freeHandDraw:
            freeHandDraw = False

        if eraserDraw:
            eraserDraw = False

    # class MovableImage(QGraphicsPixmapItem):

    #     def __init__(self, QPixmap, parent=None):
    #         super().__init__(QPixmap, parent=parent)
    #         self.setPos(100, 100)
    #         self.setAcceptHoverEvents(True)
    #         # self.group = QGraphicsItemGroup(scene=parent.scene)
    #         # self.group.setHandlesChildEvents(False)

    #     def hoverEnterEvent(self, event):
    #         self.setCursor(Qt.OpenHandCursor)
    #         super().hoverEnterEvent(event)

    #     def hoverLeaveEvent(self, event):
    #         self.setCursor(Qt.CrossCursor)
    #         super().hoverLeaveEvent(event)

    #     def mousePressEvent(self, event):
    #         print("works")
    #         super().mousePressEvent(event)

    #     def mouseMoveEvent(self, event):
    #         startPos = event.lastScenePos()
    #         updatedPos = event.scenePos()
    #         currentPos = self.scenePos()
    #         updatedX = updatedPos.x() - startPos.x() + currentPos.x()
    #         updatedY = updatedPos.y() - startPos.y() + currentPos.y()
    #         self.setPos(updatedX, updatedY)
    #         super().mouseMoveEvent(event)

    #     def mouseReleaseEvent(self, event):
    #         print("also works")
    #         super().mouseReleaseEvent(event)

    def insertNewImage(self):
        global imageToMove
        imagePath = QFileDialog.getOpenFileName(caption="Open File", directory="",filter="Images (*.jpg *.jpeg *.png)")
        # Load the image and resize it to fit the QGraphicsScene
        image = QPixmap.fromImage(QImage(imagePath[0]).scaled(int(100), int(100), aspectRatioMode=Qt.IgnoreAspectRatio))
        imageItem = QGraphicsPixmapItem(image)
        imageToMove = imageItem
        self.addItem(imageItem)

    def setPenColor(self, color):
        self.color = color
        self.pen.setColor(color)

    def setPenSize(self, size):
        self.pen.setWidth(size)
        self.eraser.setWidth(size)

    def canFlood(self, pixelMap, x, y, bgColor, fillColor):
        if x < 0 or x >= self.width() or y < 0 or y >= self.height() or pixelMap.pixelColor(int(x), int(y))!= bgColor or pixelMap.pixelColor(int(x), int(y)) == fillColor:
                return False
        return True



class BrushMateWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(BrushMateWindow, self).__init__(parent)
        self.setupUi(self)
        self.scene = GraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(Qt.white))
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.graphicsView.setInteractive(True)
        self.mouseButton.setChecked(True)
        self.mouseButton.clicked.connect(self.mouseClicked)
        self.freehandButton.clicked.connect(self.freehandClicked)
        self.eraserButton.clicked.connect(self.eraserClicked)
        self.assignShapesMenu()
        self.insertImgButton.clicked.connect(self.insertImgClicked)
        self.insertTextButton.clicked.connect(self.insertTextClicked)
        self.cloneStampButton.clicked.connect(self.cloneStampClicked)
        self.floodfillButton.clicked.connect(self.floodfillClicked)
        # self.mouseCursor.clicked.connect(self.mouseCursorClicked)
        self.sizeSliderButton.clicked.connect(self.sizeSliderClicked)
        self.colorPickerButton.clicked.connect(self.colorPickerClicked)

        self.graphicsView.setCursor(Qt.CrossCursor)

        self.retranslateMainUi(Ui_MainWindow)
        QMetaObject.connectSlotsByName(self)

        self.filename = None
        self.actionSave.triggered.connect(self.fileSave)
        self.actionSave_As.triggered.connect(lambda: self.fileSave(saveAs=True))

    def retranslateMainUi(self, MainWindow):
        _translate = QCoreApplication.translate
        self.actionSave.setShortcut(_translate("Ui_MainWindow", "Ctrl+S"))
        self.actionSave_As.setShortcut(_translate("Ui_MainWindow", "Ctrl+Shift+S"))

    def mouseClicked(self):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingText, moveImg
        self.uncheckAllButtons()
        self.mouseButton.setChecked(True)
        self.setAllFalse()
        moveImg = True

    def freehandClicked(self):
        global freeHand, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingText
        self.uncheckAllButtons()
        self.freehandButton.setChecked(True)
        self.setAllFalse()
        freeHand = True

    def eraserClicked(self):
        global freeHand, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingText
        self.uncheckAllButtons()
        self.eraserButton.setChecked(True)
        self.setAllFalse()
        eraser = True

    def assignShapesMenu(self):
        menu = QMenu(self.shapesButton, triggered=self.shapesClicked)
        for opt in ["", "Line", "Rectangle", "Square", "Circle", "Ellipse"]:
            menu.addAction(opt)
        self.shapesButton.setMenu(menu)

    @QtCore.pyqtSlot(QtWidgets.QAction)
    def shapesClicked(self, action):
        global freeHand, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingText
        self.uncheckAllButtons()
        self.shapesButton.setChecked(True)

        self.setAllFalse()
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
        global freeHand, freeHandDraw, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, insertingText, changedPenSize, floodFill, cloneStamping
        self.uncheckAllButtons()
        self.insertImgButton.setChecked(True)
        self.setAllFalse()
        self.scene.insertNewImage()
        self.insertImgButton.setChecked(False)

    def insertTextClicked(self):
        global freeHand, freeHandDraw, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, insertingText, changedPenSize, floodFill, cloneStamping
        self.uncheckAllButtons()
        self.insertTextButton.setChecked(True)
        self.setAllFalse()
        insertingText = True
        textboxContents, ok = QInputDialog.getText(self, 'Text Box', 'Insert Text')

    def cloneStampClicked(self):
        global freeHand, freeHandDraw, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, insertingText, changedPenSize, floodFill, cloneStamping
        self.uncheckAllButtons()
        self.cloneStampButton.setChecked(True)
        self.setAllFalse()
        cloneStamping = True

    def floodfillClicked(self):
        global freeHand, freeHandDraw, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, insertingText, changedPenSize, floodFill, cloneStamping
        self.uncheckAllButtons()
        self.floodfillButton.setChecked(True)
        self.setAllFalse()
        floodFill = True

    class MouseTracker(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.setGeometry(300, 300, 300, 200)
            self.label = QLabel(self)
            self.label.resize(200, 40)
            self.show()

        def mouseMoveEvent(self, event):
            self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))

    def mouseCursorClicked(self):
        self.setAllFalse()
        self.uncheckAllButtons()
        self.mouseCursor.setChecked(True)
        self.mouseTracker = self.MouseTracker()
        self.mouseTracker.show()

    class SizeSlider(QWidget):
        def __init__(self, size, parent = None):
            super().__init__(parent)
            self.setGeometry(QRect(500, 300, 500, 200))
            layout = QVBoxLayout()
            self.sizeTitle = QLabel("Pick size from 1 - 50") #\n(Click on the slider button again to confirm)")
            self.sizeTitle.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.sizeTitle)

            self.sizePicker = QSlider(Qt.Horizontal)
            self.sizePicker.setRange(1, 50)
            self.sizePicker.setValue(size)
            self.size = size
            self.sizePicker.setTickPosition(QSlider.TicksBelow)
            self.sizePicker.setTickInterval(1)
            self.sizePicker.valueChanged.connect(self.sizeChange)
            layout.addWidget(self.sizePicker)

            self.sizeValue = QLabel(str(self.size))
            self.sizeValue.setAlignment(Qt.AlignCenter)
            layout.addWidget(self.sizeValue)

            self.setLayout(layout)
            self.setWindowTitle("Pen Size")

        def sizeChange(self, value):
            global drawingPenSize
            drawingPenSize = value
            self.sizeValue.setText(str(value))

    def sizeSliderClicked(self):
        global changedPenSize, drawingPenSize
        self.setAllFalse()
        self.uncheckAllButtons()
        self.sizeSliderButton.setChecked(True)
        self.sizeSlider = self.SizeSlider(self.scene.pen.width())
        self.sizeSlider.show()
        changedPenSize = True

    def colorPickerClicked(self):
        global freeHand, freeHandDraw, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, insertingText, changedPenSize, floodFill, cloneStamping
        self.uncheckAllButtons()
        color = QColorDialog.getColor()
        self.scene.setPenColor(color)
        self.colorPickerButton.setChecked(True)
        self.setAllFalse()

    def uncheckAllButtons(self):
        self.mouseButton.setChecked(False)
        self.freehandButton.setChecked(False)
        self.eraserButton.setChecked(False)
        self.shapesButton.setChecked(False)
        self.insertImgButton.setChecked(False)
        self.insertTextButton.setChecked(False)
        self.cloneStampButton.setChecked(False)
        self.floodfillButton.setChecked(False)
        self.insertTextButton.setChecked(False)

    def setAllFalse(self):
        global freeHand, freeHandDraw, eraser, drawingLines, drawingRects, drawingSquares, drawingCircles, drawingEllipses, insertingImg, moveImg, insertingText, changedPenSize, floodFill, cloneStamping
        if changedPenSize:
            self.scene.setPenSize(drawingPenSize)
        freeHand = eraser = drawingLines = drawingRects = drawingSquares = drawingCircles = drawingEllipses = insertingImg = moveImg = insertingText = changedPenSize = floodFill = False

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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = BrushMateWindow()
    w.show()
    sys.exit(app.exec_())
