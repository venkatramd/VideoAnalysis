import os
import cv2
import subprocess
import time
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

for v in allvideos:
    print(cwd+v)
    save_i_keyframes(cwd+v)

print("--- %s seconds ---" % (time.time() - start_time))

