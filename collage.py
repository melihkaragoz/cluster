import os
from PIL import Image

os.system("ls photos/*.jpg > ./photos/urls")
f = open("./photos/urls","r")
d = f.read()
d = d.split("\n")
d.pop(-1)
print(d)
new_image = Image.new('RGB',(2*200, 200))
width = 0
for url in d:
	image1 = Image.open(f"{url}")
	image1 = image1.resize((200, 200))
	new_image.paste(image1,(width,0))
	width += 200

new_image.save("kolaj.jpg","JPEG")
new_image.show()
