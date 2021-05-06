"""Although this program is meant to run when the iss is just above your head and it is night 
just for running this program we have taken our latitute and longitude as near the iss orbits
for checking you can run the script in cloud to get a smtp message when the iss is close"""



import requests
from datetime import datetime
import smtplib
import time

# MY_LAT = 17.677709  # Your latitude
# MY_LONG = 83.248488  # Your longitude


MY_EMAIL = your_email
PASSWORD = your_password
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude)
print(iss_longitude)


MY_LAT = iss_latitude -2  # Your latitude
MY_LONG = iss_longitude +2  # Your longitude
# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_time = time_now.hour
print(hour_time)


def check_sat():
    # MY_LAT = 24.6588  # 17.677709  # Your latitude
    # MY_LONG = 124.118
    # if MY_LAT -5 and iss_longitude + count == MY_LONG:
    #         if iss_latitude - count == MY_LAT and iss_longitude - count == MY_LONG:
    #             is_near = True
    #             print("near me")
    # print("not near")
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        # print(is_near)
        print("checktrue")
        return True


while True:
    # time.sleep(60)
    if check_sat():
        print("checking 1")
        # if sunrise >= hour_time >= sunset:  # uncomment this code if you want this to run when it is night
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=MY_EMAIL, msg=f"Subject:LOOK UP!")
                print("sent")
    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
