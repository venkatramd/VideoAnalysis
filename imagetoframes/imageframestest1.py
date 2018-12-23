from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys



class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Select Video', self)
        qbtn.clicked.connect(self.on_button_clicked)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(590, 400)

        label4 = QLabel('Click on below button to select a video', self)
        label4.move(420, 350)
        label4.setFont(QFont('Arial', 20))

        oImage = QImage("bbb.jpg")
        sImage = oImage.scaled(QSize(1300, 780))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Select Video')
        self.showMaximized()

    def on_button_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            try:
                f = open("storefilename.txt", mode="w", encoding='utf-8')
                # perform file operations
                with open("storefilename.txt", 'w', encoding='utf-8') as f:
                    f.write(fileName)
            finally:
                f.close()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())