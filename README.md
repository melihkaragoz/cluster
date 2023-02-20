NOTE 
----------------------
access token's expire date is 2hr later from when it's created.
----------------------

installing
----------------------
pip3 install wget
pip3 install Pillow
----------------------

getting access token
---------------------
Format : 
curl -X POST --data "grant_type=client_credentials&client_id=<YOUR_CLIENT_ID>&client_secret=<YOUR_SECRET>" https://api.intra.42.fr/oauth/token

Example : 
curl -X POST --data "grant_type=client_credentials&client_id=u-s4t2ud-e6a9641743be40bf815edf146640a77e92c8d38dee9780bb49de2a74df3afa4e&client_secret=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" https://api.intra.42.fr/oauth/token
---------------------
