import requests
import datetime as dt

MY_LAT = -18.0449
MY_LONG = 6.8557

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
# print(data)

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

print(longitude, latitude)

def is_iss_overhead():
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise, sunset)

time_now = dt.datetime.now()
print(time_now.hour)

def is_night():
    if time_now.hour > sunset or time_now.hour < sunrise:
        return True
    else:
        return False

if is_iss_overhead() and is_night():
    print("Send an email to the user")
else:
    print("Not night")




