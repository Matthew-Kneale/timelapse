#video maker 20210609
 

from os import system
import datetime
from time import sleep

fps = 30 #frames per second timelapse video

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")

print("Please standby as your timelapse video is created.")

system('ffmpeg -r {} -f image2 -s 3280x2464 -nostats -loglevel 0 -pattern_type glob -i "/home/pi/Pictures/*.jpg" -vcodec libx264 -crf 25  -pix_fmt yuv420p /home/pi/Videos/{}.mp4'.format(fps, datetimeformat))
#system('rm /home/pi/Pictures/*.jpg')
print('Timelapse video is complete. Video saved as /home/pi/Videos/{}.mp4'.format(datetimeformat))
