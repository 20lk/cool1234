import os
from time import sleep
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (2028, 1520)  # Half the maximum resolution
camera.start_preview()