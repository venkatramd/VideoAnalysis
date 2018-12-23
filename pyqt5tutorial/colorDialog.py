import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.setWindowTitle(self.title)


        button = QPushButton('Open color dialog', self)
        button.setToolTip('Opens color dialog')
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        openColorDialog(self)


def openColorDialog(self):
    color = QColorDialog.getColor()

    if color.isValid():
        print(color.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
