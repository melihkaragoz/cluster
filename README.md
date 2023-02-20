create "photos" folder
----------------------
pip3 install wget
pip3 install Pillow
----------------------

get accessToken

curl -X POST --data "grant_type=client_credentials&client_id=<YOUR_CLIENT_ID>&client_secret=<YOUR_SECRET>" https://api.intra.42.fr/oauth/token
