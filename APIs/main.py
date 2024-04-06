import requests
#get data we want from the endpoint

apiresponse = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(apiresponse.status_code)
# error codes in html 1xx - Hold on 2xx = Here you go 3xx Go Away, 4xx you messed up, 5xx website messed up
# if apiresponse.status_code != 200:
#   raise Exception("The resouce does not exist")
# elif apiresponse.status_code == 401:
#   raise Exception("You are not authorized to aceess this resource")

# instead of typing out all the error codes for html and send a message, here is an easier method:
apiresponse.raise_for_status() # sends all html codes and errors

data = apiresponse.json() # this is the data from API call
print(data)
#get specific data
longtitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

#create a tuple with coordinates

iss_position = (longtitude, latitude)
print("Latitude and Longitude:", iss_position)

