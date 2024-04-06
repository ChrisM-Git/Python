#challenge
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

import requests
from datetime import datetime
import smtplib
import time

email = "email4chrism@gmail.com"
password = "yourgmailpassword"



MY_LAT = 45.543282  # Your latitude
MY_LONG = -122.834129 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.

def overhead ():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #take your lat/long values and compare it to iss  + or - 5 degrees
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True



def night ():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now >= sunset and time_now <= sunrise:
        return True

#repeat to keep checking
while True:
    time.sleep(60) # slow the while loop down to execute every 60 seconds
    if overhead and night: # if ISS is over your lat,long and its nighttime, send email
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email,password)
        connection.sendmail (
            from_addr=email,
            to_addrs=email,
            msg=("subject: look up \n\n The ISS is above you in the sky!")
        )








