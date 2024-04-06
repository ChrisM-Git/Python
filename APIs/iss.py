import requests
from datetime import datetime

# this api requires a location for it to return a result on the iss satellite position

#define parameters, a dictionary would be good for this
lat = 45.543280
lng = -122.834130
parameters = {
  # these dictionaries need to match the expected input to the API, ISS api expects an lat and lng input
  # go to latlong.net to get your lat and lng values
  "lat" : lat,
  "lng" : lng,
  "formatted" : 0,  #change to 24 hr format
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters) #here is where we send our values to api

response.raise_for_status()
data = response.json()
print(data)
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]  #format output using split
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

timenow = datetime.now()
# datetime is in 24 hr format, api is in 12 hr format, change api to match 24 hr format
print(timenow.hour)
print("Sunrise:",sunrise)
print("Sunset:",sunset)
