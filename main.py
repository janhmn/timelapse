import time

from picamera import PiCamera

camera = PiCamera()

for i in range(10):
    time.sleep(10)
    camera.capture("src/image{0:04d}.jpg".format(i))
