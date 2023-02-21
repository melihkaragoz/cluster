import json,os,wget
import ssl
from time import sleep

while(1):
	os.system("rm photos/*.jpg")
	t = open("token.txt","r")
	try:
		tokenFile = json.load(t)
		accessToken = tokenFile["access_token"]
	except:
		print("token is invalid, running 'generateAccessToken.sh' script, please wait...")
		os.system("./generateAccessToken")
		continue

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
	try:
		os.mkdir("photos")
	except:
		pass
	os.chdir("./photos")
	try:
		for user in users:
			sleep(0.3)
			os.system(f"curl  -H 'Authorization: Bearer {accessToken}' 'https://api.intra.42.fr/v2/users/{user}/' > res.json")
			f = open("res.json","r")
			data = json.load(f)
			try:
				d = data["location"]
			except:
				print("Token expired, please run the 'generateAccessToken.sh' script with your user_id and secret_key.")
				exit()
			img = data["image"]["link"]
			dict = {
				"user" : user,
				"location" : d,
				"img" : img
			}
			if (d != None):
				available.append(dict)
	except:
		print(" -- An error occured !! for help : mkaragoz at 42/Istanbul -- ")

	for u in available:
		wget.download(f"{u['img']}")

	os.chdir("../")
	os.system("python3 collage.py")
	sleep(600)
