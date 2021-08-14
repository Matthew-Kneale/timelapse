from PIL import Image
import pathlib
maxsize = (512, 512)
for input_img_path in pathlib.Path("/home/pi/Pictures/").iterdir():
    output_img_path = str(input_img_path).replace("/home/pi/Pictures/","/home/pi/Pictures/Reduced")
    with Image.open(input_img_path) as im:
        im.thumbnail(maxsize)
        im.save(output_img_path, "JPEG", dpi=(300,300))
        print(f"processing file {input_img_path} done...")
