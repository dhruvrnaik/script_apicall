# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import requests
app = Flask(__name__)
@app.route('/')
def param():
	lon = request.args.get("lon")
	lat = request.args.get("lat")
	loc = lat+","+lon
#Hospital
	url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+loc+"&rankby=distance&type=hospital&key=AIzaSyClvOa41RlvjTGJrdpHo3pxnHm00MRR27w"
	response = requests.get(url)
	data = response.json()
	for i in range(10):
		x = data["results"][i]["name"]
		if ("hospital" in x or "Hospital" in  x) :
			place_id = data["results"][i]["place_id"]
			break
	url2 = "https://maps.googleapis.com/maps/api/place/details/json?placeid="+place_id +"&key=AIzaSyClvOa41RlvjTGJrdpHo3pxnHm00MRR27w"
	dets = requests.get(url2)
	info = dets.json()
	try:
		phone = info["result"]["formatted_phone_number"]
	except :
		phone = "112"
	address = info["result"]["formatted_address"]
	name = info['result']['name']

	#Police Station
	url3 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+loc+"&rankby=distance&type=police&key=AIzaSyClvOa41RlvjTGJrdpHo3pxnHm00MRR27w"
	response = requests.get(url3)
	data2 = response.json()
	for i in range(10):
		x = data2["results"][i]["name"]
		if ("police" in x or "Police" in  x) :
			place_id2 = data2["results"][i]["place_id"]
			break
	url4 = "https://maps.googleapis.com/maps/api/place/details/json?placeid="+place_id2 +"&key=AIzaSyClvOa41RlvjTGJrdpHo3pxnHm00MRR27w"
	dets2 = requests.get(url4)
	info2 = dets2.json()
	try:
		phone2 = info2["result"]["formatted_phone_number"]
	except :
		phone2 = "100"
	address2 = info2["result"]["formatted_address"]
	name2 = info2['result']['name']

	dic = {"Kerela":"dgp.pol@kerala.gov.in;Not available",
	"Chennai":"cop@vsnl.net;@chennaipolice_",
	"Tamil Nadu":"dgp@tn.gov.in;Not Available",
	"Hyderabad":"contact@hyd.tspolice.gov.in;@hydcitypolice",
	"Bengaluru":"compolbcp@ksp.gov.in;@BlrCityPolice",
	"Karnataka":"ksdgp@bgl.vsnl.net.in;Not Available",
	"Mumbai":"cp.mumbai@mahapolice.gov.in:@MumbaiPolice",
	"Maharashtra":"dgpms.mumbai@mahapolice.gov.in;@DGPMaharashtra",
	"Kolkata":"splcp1 kolkatapolice.gov.in;@KolkataPolice",
	"West Bengal":"Not Available;@WBPolice",
	"New Delhi":"cp.bsbassi@nic.in;@DelhiPolice"}
	mail = "Not Available"
	for key in dic.keys():
		if key in address:
			mail = dic[key]

	return (name+";"+address+";"+phone+";"+name2+";"+address2+";"+phone2+";"+mail)
