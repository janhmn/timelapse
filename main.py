import time

from picamera2 import Picamera2

with Picamera2() as camera:
    # Optional: Set resolution
    camera.resolution = (1024, 768)

    # Start a preview (optional, helpful for positioning)
    camera.start_preview()

    # Camera warm-up time (essential for exposure/white balance)
    time.sleep(2)

    for i in range(10):
        time.sleep(10)
        camera.capture_file("src/image{0:04d}.jpg".format(i))
    # Capture the image
    camera.stop_preview()
