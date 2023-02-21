#NOTE
----------------------
1 - first you have to create a new 42Api App from "https://profile.intra.42.fr/oauth/applications/new", then you can get your secret_key and UID here for generate access token.<br>
2 - don't forget to refresh your access token in every 2hr, because access token's expire date is 2hr later from when it's created.<br>
3 - don't forget to change "collage.jpg" file's path in changeBackground.sh. The .jpg file will be created in cluster directory when you run cluster.py<br>
4 - run './generateAccessToken' after setting your user_id and secret_token field in 'generateAccessToken.sh', for generate new access token (for take user_id and secret_key go (1).step).<br>
5 - specify your pc's screen size values (width,height) in 'collage.py' script.<br>

#installing
----------------------
pip3 install wget<br>
pip3 install Pillow<br>
