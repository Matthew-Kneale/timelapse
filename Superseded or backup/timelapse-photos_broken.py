#timelapse photos 20210614
# start at 7am
 
from picamera import PiCamera
from os import system
import datetime
from time import sleep

#variables
threePM = 0
tlhours = 11 #set this to the number of hours you wish to run your timelapse camera - 7am - 6pm
minutesinterval = 30 #number of minutes delay between each photo taken
numphotos = int((tlhours*3600)/(minutesinterval*60) #number of photos to take
#print("number of photos to take = ", numphotos)



# check time
dateraw = datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
print("RPi started taking photos for your timelapse at: " + datetimeformat)

camera = PiCamera()
camera.resolution = (3280, 2464)

for i in range(numphotos):
    dateraw= datetime.datetime.now()
    datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M") # check time for photo file name
    camera.capture('/home/pi/Pictures/Timelapse/{}.jpg'.format(datetimeformat))
    if threePM == 8:
        camera.capture('/home/pi/Pictures/Timelapse/3pm/{}.jpg'.format(datetimeformat))
    sleep(minutesinterval*60)
    threePM += 1
    
# check time
dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
print("RPi finished taking photos for your timelapse at: " + datetimeformat)




