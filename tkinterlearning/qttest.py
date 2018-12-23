from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)

        self.label = QLabel()
        self.label.setText("Click on the below button to select a video")
        self.label.move(30,30)
        self.label.setAlignment(Qt.AlignTop)
        layout.addWidget(self.label)

        groupbox = QGroupBox("thusadabfk cn jdanfkja ")
        groupbox.setLayout(layout)

        self.button = QPushButton("Select  a  Video")
        self.button.clicked.connect(self.on_button_clicked)
        self.button.move(450,350)
        self.button.resize(45,45)
        layout.addWidget(self.button)


        oImage = QImage("bbb.jpg")
        sImage = oImage.scaled(QSize(1300,780))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.show()

    def on_button_clicked(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
            "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)


app = QApplication(sys.argv)
screen = Window()
screen.showMaximized()
sys.exit(app.exec_())