import requests

# sunrise and sunset

parameters = {
    "lat": 51.5074,
    "lng": -0.1278,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)