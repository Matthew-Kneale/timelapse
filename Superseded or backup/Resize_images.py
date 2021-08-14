from PIL import Image

basewidth = 300
img = Image.open("/home/pi/Pictures/image000000.jpg")
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save("/home/pi/Pictures/image000000_Resize.jpg")
