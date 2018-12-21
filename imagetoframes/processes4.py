import os
import cv2
import subprocess
import time
from multiprocessing import Process
start_time = time.time()

allvideos = []
cwd = '/home/venkatram/PycharmProjects/VidoAnalysis/imagetoframes/'
for i in os.listdir(cwd):
    if i.endswith('.mp4'):
        allvideos.append(i)
print(allvideos)

def get_frame_types(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types = out.replace('pict_type=','').split()
    return zip(range(len(frame_types)), frame_types)

def save_i_keyframes1(video_fn):
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


#2 functions

def get_frame_types2(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types2 = out.replace('pict_type=','').split()
    return zip(range(len(frame_types2)), frame_types2)

def save_i_keyframes2(video_fn):
    frame_types2 = get_frame_types2(video_fn)
    i_frames = [x[0] for x in frame_types2 if x[1]=='I']
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


#3rd functions

def get_frame_types3(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types3 = out.replace('pict_type=','').split()
    return zip(range(len(frame_types3)), frame_types3)

def save_i_keyframes3(video_fn):
    frame_types3 = get_frame_types3(video_fn)
    i_frames = [x[0] for x in frame_types3 if x[1]=='I']
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


#4th functions

def get_frame_types4(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types4 = out.replace('pict_type=','').split()
    return zip(range(len(frame_types4)), frame_types4)

def save_i_keyframes4(video_fn):
    frame_types4 = get_frame_types4(video_fn)
    i_frames = [x[0] for x in frame_types4 if x[1]=='I']
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


#main function

p1 = Process(target=save_i_keyframes1,args=(cwd+allvideos[0],))
p2 = Process(target=save_i_keyframes2,args=(cwd+allvideos[1],))
p3 = Process(target=save_i_keyframes3,args=(cwd+allvideos[2],))
p4 = Process(target=save_i_keyframes4,args=(cwd+allvideos[3],))


p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

p1 = Process(target=save_i_keyframes1,args=(cwd+allvideos[4],))
p2 = Process(target=save_i_keyframes2,args=(cwd+allvideos[5],))
p3 = Process(target=save_i_keyframes3,args=(cwd+allvideos[6],))
p4 = Process(target=save_i_keyframes4,args=(cwd+allvideos[7],))


p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()
print("--- %s seconds ---" % (time.time() - start_time))

