#!/usr/bin/python

# thanks Loutor for idea !  https://www.loutor.org/2018/02/08/home-mode-avec-surveillance-station/

import json
import os
import requests
import sys
import time

NAS_HOST="locahost"
NAS_PORT="5000"
USERNAME="user"
PASSWORD="password"

# GET SID
res = requests.get("http://"+NAS_HOST+":"+NAS_PORT+"/webapi/auth.cgi?api=SYNO.API.Auth&method=Login&version=2&account="+USERNAME+"&passwd="+PASSWORD+"&session=SurveillanceStation&format=sid")
res_native = json.loads(res.text)
sid=str(res_native.get('data').get('sid'))
print(sid)
time.sleep(2)

# LIST CAMERA

res = requests.get("http://"+NAS_HOST+":"+NAS_PORT+"/webapi/entry.cgi?api=SYNO.SurveillanceStation.Camera&method=List&version=1&_sid="+sid)
res_native = json.loads(res.text)
camera=str(res_native.get('data').get('cameras'))
print(camera)

#CAMERA INFO (change cameraId by your camera ID)

res = requests.get("http://"+NAS_HOST+":"+NAS_PORT+"/webapi/entry.cgi?api=SYNO.SurveillanceStation.Camera&method=GetInfo&version=1&cameraIds=2&_sid="+sid)
res_native = json.loads(res.text)
print res_native['data']['cameras'][0]['enabled']

# ENABLE Camera

# curl -iv "http://nas:5000/webapi/entry.cgi?api=SYNO.SurveillanceStation.Camera&method=Enable&version=9&idList=2&_sid=xxxxxxxx"

# DISABLE Camera
# curl -iv "http://nas:5000/webapi/entry.cgi?api=SYNO.SurveillanceStation.Camera&method=Enable&version=9&idList=2&_sid=xxxxxxx"

