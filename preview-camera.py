from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.start_preview()
camera.start_preview(fullscreen=False,window=(0,-1500,3280, 2464))
sleep(3600)
camera.stop_preview()

