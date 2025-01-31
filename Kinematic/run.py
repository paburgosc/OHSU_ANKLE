import time
from threading import Thread
import os

def startprgm(i):
    print ("Running thread %d" % i)
    if (i == 0):
        time.sleep(1)
        print('Running: main1.py')
        os.system("sudo /home/pi/.pyenv/versions/3.6.6/bin/python main1.py")
        time.sleep(10)
    elif (i == 1):
        print('Running: readeulercallable.py')
        time.sleep(10)
        os.system("sudo /home/pi/.pyenv/versions/3.6.6/bin/python readeulercallable.py")
    else:
        pass

for i in range(2):
    t = Thread(target=startprgm, args=(i,))
    t.start()
