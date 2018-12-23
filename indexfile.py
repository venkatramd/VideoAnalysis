import os
from multiprocessing import Process


allframes = []
cwd = os.getcwd()+"/framesextracted/"
print(cwd)
for i in os.listdir(cwd):
    if i.endswith('.jpg') or i.endswith('.png'):
        allframes.append(i)
print(allframes)
noofframes=(len(allframes))

#all partitions of frames for each process where part1 means until part1 but part1 is not considered
#no of frames in each part

def firstprocess():
    for i in range(0,int(noofframes/2)):
        os.system("python text_recognition1.py --east frozen_east_text_detection1.pb --image framesextracted/" + allframes[i] + "")

def secondprocess():
    for j in range(int(noofframes/2),noofframes):
        os.system("python text_recognition2.py --east frozen_east_text_detection2.pb --image framesextracted/" + allframes[j] + "")


p1=Process(target=firstprocess)
p2=Process(target=secondprocess)

p1.start()
p2.start()

p1.join()
p2.join()

#concatinatig two files into one file
file1 = "/home/venkatram/PycharmProjects/VidoAnalysis/result1.txt"
file2 = "/home/venkatram/PycharmProjects/VidoAnalysis/result2.txt"

filenames = [file1,file2]
with open('/home/venkatram/PycharmProjects/VidoAnalysis/finaloutput.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

#for image in (allframes):
#   os.system("python text_recognition.py --east frozen_east_text_detection.pb --image framesextracted/"+image+"")