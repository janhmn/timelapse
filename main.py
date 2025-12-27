import time

from picamera2 import Picamera2

with Picamera2() as camera:
    # Optional: Set resolution
    camera.start()

    # Camera warm-up time (essential for exposure/white balance)
    time.sleep(2)

    for i in range(480):
        print(i)
        camera.capture_file("src/image{0:04d}.jpg".format(i))
        time.sleep(29)
