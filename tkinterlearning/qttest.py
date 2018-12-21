import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
       QWidget.__init__(self)
       self.setGeometry(100,100,600,900)

       oImage = QImage("venky2.png")
       sImage = oImage.scaled(QSize(300,900))                   # resize Image to widgets size
       palette = QPalette()
       palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
       self.setPalette(palette)

       self.label = QLabel('Test', self)                        # test, if it's really backgroundimage
       self.label.setGeometry(50,50,200,50)

       self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    oMainwindow.showMaximized()
    sys.exit(app.exec_())