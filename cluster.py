import json,os,wget
import ssl

accessToken = "90b9270743f040399efb572dbd71522df41622ab517d59cb20906bcbaf65ad6d"
ssl._create_default_https_context = ssl._create_unverified_context
users = []
available = []
fr = open("friends.txt","r")
while (1):
	us = fr.readline().split("\n")[0]
	if (us != ''):
		users.append(us)
	else:
		fr.close()
		break
os.mkdir("photos")
os.chdir("./photos")
try:
	for user in users:
		os.system(f"curl  -H 'Authorization: Bearer {accessToken}' 'https://api.intra.42.fr/v2/users/{user}/' > res.json")
		f = open("res.json","r")
		data = json.load(f)
		d = data["location"]
		img = data["image"]["link"]
		dict = {
			"user" : user,
			"location" : d,
			"img" : img
		}
		if (d != None):
			available.append(dict)
except:
	print(" -- Token expired !! -- ")

for u in available:
	wget.download(f"{u['img']}")

os.chdir("../")
os.system("python3 collage.py")
