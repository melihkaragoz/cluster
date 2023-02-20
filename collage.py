import os
from PIL import Image

pc_width = 2560
pc_height = 1600
os.system("ls photos/*.jpg > ./photos/urls")
f = open("./photos/urls","r")
d = f.read()
d = d.split("\n")
d.pop(-1)
print(d)
new_image = Image.new('RGB',(pc_width, pc_height))
width = 0
height = int(pc_width/6)
for url in d:
	image1 = Image.open(f"{url}")
	image1 = image1.resize(size=[int(pc_width/6), int(pc_width/6)])
	new_image.paste(image1,(width,(int(pc_height/2)-int(pc_width/12))))
	if (width + 800 >= pc_width):
		width = 0
		height += int(pc_width/6)
	else:
		width += int(pc_width/6)

new_image.save("collage.jpg","JPEG")
os.system("bash ./changeBackground.sh")
