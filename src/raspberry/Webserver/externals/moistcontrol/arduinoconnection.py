#from network import WLAN
import json
import requests

class ArduinoConnection:
    #def __init__(self):
    #wlan = WLAN(mode=WLAN.STA)
    #wlan.connect("Isabels iPhone", auth=(net.sec, "ifpejnn09q53y"), timeout=5000)

	def getValue(self):
		r = requests.get('https://172.20.10.3/getValues.json')
		print(r.text)

