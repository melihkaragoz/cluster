import json,os,wget
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
users = ["mkaragoz","makbulut","mdiraga"]
available = []
os.chdir("./photos")
for user in users:
	os.system(f"curl  -H 'Authorization: Bearer 32fc7cf76c4104584a85f0230e6db08d906ce659ec232d86a490eda003229782' 'https://api.intra.42.fr/v2/users/{user}/' > res.json")
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

for u in available:
	wget.download(f"{u['img']}")
