#!/usr/bin/env python
"""
This is a trivial example of how to use kismetclient in an application.
"""
from kismetclient import Client as KismetClient
from kismetclient import handlers

from pprint import pprint

import logging

import json
import requests
import random

log = logging.getLogger('kismetclient')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

endpoint_AP = "http://54.83.8.108:8080/AP/"
endpoint_BT = "http://54.83.8.108:8080/BT/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

maxentries = 0

address = ('127.0.0.1', 2501)
k = KismetClient(address)
k.register_handler('TRACKINFO', handlers.print_fields)


def handle_ssid(client, ssid, mac):
    global maxentries
    maxentries=maxentries+1
    
    print 'bssid spotted: "%s" with mac %s' % (ssid, mac)
    lon="-122.406" + str(random.randint(10,99))
    lat="37.765" + str(random.randint(10,99))


    data = {"name": ssid, "LON": lon, "LAT": lat, "essid": ssid, "type": "101"}	#data to be send to the server
    print data
    if maxentries<90:
    	r = requests.post(endpoint_AP, data=json.dumps(data), headers=headers)

def handle_bluetooth(client, bdaddr, firsttime, lasttime):
    print 'Bluetooth device spotted: "%s" First seen %s Last seen %s' % (bdaddr, firsttime, lasttime)
    data = 'Bluetooth device spotted: "%s" First seen %s Last seen %s' % (bdaddr, firsttime, lasttime)
    data = {"bdaddr": bdaddr, "LON": "-122.403999", "LAT":"37.777899","type": "102", "name": bdaddr}	#data to be send to the server
    print data
    r = requests.post(endpoint_BT, data=json.dumps(data), headers=headers)
 

def handle_GPS(client, lat, lon):
    print 'we are at "%s" "%s"' % (lat, lon)
    xlat=lat
    xlon=lon
	


k.register_handler('SSID', handle_ssid)
#k.register_handler('BTBBDEV', handle_bluetooth)
k.register_handler('GPS', handle_GPS)

try:
    while True:
        k.listen()
except KeyboardInterrupt:
    pprint(k.protocols)
    log.info('Exiting...')
