from picamera import PiCamera
from os import system
import datetime
from time import sleep

tlminutes = 600 #10 hours - set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 1800 #30 minutes - number of seconds delay between each photo taken
#fps = 30 #frames per second timelapse video
numphotos = int((tlminutes*60)/secondsinterval) #number of photos to take
print("number of photos to take = ", numphotos)

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
print("RPi started taking photos for your timelapse at: " + datetimeformat)

camera = PiCamera()
camera.resolution = (3280, 2464)

for i in range(numphotos):
    dateraw= datetime.datetime.now()
    datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M") # check time for photo file name
    camera.capture('/home/pi/Pictures/Timelapse/{}.jpg'.format(datetimeformat))
    if i == 8:
        camera.capture('/home/pi/Pictures/Timelapse/3pm/{}.jpg'.format(datetimeformat))
    sleep(secondsinterval)
print("Done taking photos.")
