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
noofinApart=int(noofframes/4)

def firstprocess():
    for i in range(0,noofinApart):
        os.system("python text_recognition1.py --east frozen_east_text_detection1.pb --image framesextracted/" + allframes[i] + "")

def secondprocess():
    for j in range(noofinApart,2*noofinApart):
        os.system("python text_recognition2.py --east frozen_east_text_detection2.pb --image framesextracted/" + allframes[j] + "")

def thirdprocess():
    for k in range(2*noofinApart,3*noofinApart):
        os.system("python text_recognition3.py --east frozen_east_text_detection3.pb --image framesextracted/" + allframes[k] + "")

def fourthprocess():
    for l in range(3*noofinApart,noofframes):
        os.system("python text_recognition4.py --east frozen_east_text_detection4.pb --image framesextracted/" + allframes[l] + "")



p1=Process(target=firstprocess)
p2=Process(target=secondprocess)
p3=Process(target=thirdprocess)
p4=Process(target=fourthprocess)

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

#concatinatig two files into one file
file1 = "/home/venkatram/PycharmProjects/VidoAnalysis/result1.txt"
file2 = "/home/venkatram/PycharmProjects/VidoAnalysis/result2.txt"
file3 = "/home/venkatram/PycharmProjects/VidoAnalysis/result3.txt"
file4 = "/home/venkatram/PycharmProjects/VidoAnalysis/result4.txt"

filenames = [file1,file2,file3,file4]
with open('/home/venkatram/PycharmProjects/VidoAnalysis/finaloutput.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

#for image in (allframes):
#   os.system("python text_recognition.py --east frozen_east_text_detection.pb --image framesextracted/"+image+"")