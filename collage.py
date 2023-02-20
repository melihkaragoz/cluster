import os
from PIL import Image


pc_width = 1120
pc_height = 880
os.system("ls photos/*.jpg > ./photos/urls")
f = open("./photos/urls","r")
d = f.read()
d = d.split("\n")
d.pop(-1)
print(d)
new_image = Image.new('RGB',(pc_width, pc_height))
width = 0
for url in d:
	image1 = Image.open(f"{url}")
	image1 = image1.resize(size=[int(pc_width/len(d)), 400])
	new_image.paste(image1,(width,0))
	width += int(pc_width/len(d))

new_image.save("kolaj.jpg","JPEG")
#os.system("bash ./changeBackground.sh")
