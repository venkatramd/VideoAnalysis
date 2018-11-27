import os
os.system("python text_recognition.py --east frozen_east_text_detection.pb --image images/example_02.jpg")
files = []
cwd = os.getcwd()+"/images/"
print(cwd)
for i in os.listdir(cwd):
    if i.endswith('.jpg') or i.endswith('.png'):
        files.append(i)
print(files)