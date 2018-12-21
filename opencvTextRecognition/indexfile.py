import os
allframes = []
cwd = os.getcwd()+"/images/"
print(cwd)
for i in os.listdir(cwd):
    if i.endswith('.jpg') or i.endswith('.png'):
        allframes.append(i)
print(allframes)
for image in (allframes):
    os.system("python text_recognition.py --east frozen_east_text_detection.pb --image images/"+image+"")
