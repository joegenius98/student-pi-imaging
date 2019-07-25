import os
import datetime
from datetime import tzinfo
import math
from picamera import PiCamera
from time import sleep
import time


# Enter the path where the raspberry pi will store its file
RASPI_PATH = ""

INTERVAL = 5# the time interval (in seconds) between pictures
SESSION_LENGTH = 600# the duration of the script
PHOTOS = SESSION_LENGTH / INTERVAL

# camera = PiCamera()
# camera.start_preview()


# Have the camera take pictures at the specified interval until the session is over
with PiCamera() as camera:
    camera.start_preview()
    try:
        for i, filename in enumerate(camera.capture_continuous('image{counter}.jpg')):
            print(filename)
            time.sleep(INTERVAL)
            if i == PHOTOS - 1:
                break
    finally:
        camera.stop_preview()


camera.stop_preview()
#hi
