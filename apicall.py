import requests
import json
#Hospital
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=13.351467,74.792691&rankby=distance&type=hospital&key=AIzaSyClvOa41RlvjTGJrdpHo3pxnHm00MRR27w"
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
except Error:
	phone = None
address = info["result"]["formatted_address"]
name = info['result']['name']

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

print(name+";"+address+";"+phone+mail)