#calculating time
import time
start_time = time.time()

import os
os.system("python /home/venkatram/PycharmProjects/VidoAnalysis/imagetoframes/imagetoframes.py")
os.system("python /home/venkatram/PycharmProjects/VidoAnalysis/indexfile.py")

print("--- %s seconds ---" % (time.time() - start_time))

