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

log = logging.getLogger('kismetclient')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

endpoint_AP = "http://54.83.8.108:8080/AP"
endpoint_BT = "http://54.83.8.108:8080/BT"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

address = ('127.0.0.1', 2501)
k = KismetClient(address)
k.register_handler('TRACKINFO', handlers.print_fields)


def handle_ssid(client, ssid, mac):
    print 'ssid spotted: "%s" with mac %s' % (ssid, mac)
    print(data)

    

def handle_bluetooth(client, bdaddr, firsttime, lasttime):
    print 'Bluetooth device spotted: "%s" First seen %s Last seen %s' % (bdaddr, firsttime, lasttime)
    data = 'Bluetooth device spotted: "%s" First seen %s Last seen %s' % (bdaddr, firsttime, lasttime)
    data = {"bdaddr": bdaddr, "LON": "-122.403999", "LAT":"37.777899"}	#data to be send to the server
    print data
    r = requests.post(endpoint_BT, data=json.dumps(data), headers=headers)




#k.register_handler('SSID', handle_ssid)
k.register_handler('BTBBDEV', handle_bluetooth)

try:
    while True:
        k.listen()
except KeyboardInterrupt:
    pprint(k.protocols)
    log.info('Exiting...')
