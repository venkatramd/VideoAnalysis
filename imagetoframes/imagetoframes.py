import os
import cv2
import time
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

fileName = ""
filenamepassed = ""
class Example(QWidget):
    classfilename=""
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


app = QApplication(sys.argv)
ex = Example()
print("hello")
print(ex.classfilename)
sys.exit(app.exec_())





def get_frame_types(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types = out.replace('pict_type=','').split()
    return zip(range(len(frame_types)), frame_types)

def save_i_keyframes(video_fn):
    frame_types = get_frame_types(video_fn)
    i_frames = [x[0] for x in frame_types if x[1]=='I']
    if i_frames:
        basename = os.path.splitext(os.path.basename(video_fn))[0]
        cap = cv2.VideoCapture(video_fn)
        for frame_no in i_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            outname = basename+'_i_frame_'+str(frame_no)+'.jpg'
            cv2.imwrite("/home/venkatram/PycharmProjects/VidoAnalysis/framesextracted/"+outname+"", frame)
            print ('Saved: '+outname)
        cap.release()
    else:
        print ('No I-frames in '+video_fn)


#print(filenamepassed)
#main function
save_i_keyframes(filename)
print("mine is first")
print("this is the path passed"+fileName)