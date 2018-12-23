#calculating time
import time
start_time = time.time()
import os
import shutil

for root, dirs, files in os.walk('python /home/venkatram/PycharmProjects/VidoAnalysis/framesextracted/'):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))

import os
os.system("python /home/venkatram/PycharmProjects/VidoAnalysis/imagetoframes/imageframestest1.py")
os.system("python /home/venkatram/PycharmProjects/VidoAnalysis/imagetoframes/imageframestest2.py")
os.system("python /home/venkatram/PycharmProjects/VidoAnalysis/indexfile.py")

print("--- %s seconds ---" % (time.time() - start_time))

