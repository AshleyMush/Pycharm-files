import requests
from datetime import  datetime
My_lat = 51.752022
My_long = -1.257677

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
# lattitude = data["iss_position"]["latitude"]
#
# longitude  = data["iss_position"]['longitude']
#
# iss_position = (longitude, lattitude)
# print(iss_position)

parameters = {
    "lat": My_lat,
    "long": My_long,
    "formatted": 0



}

sunrise_sunset_API = "https://api.sunrise-sunset.org/json"
response = requests.get(sunrise_sunset_API, params=parameters )
print(response)

#Convert data to json

data = response.json()
sunrise = data["results"]["sunset"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]
timenow = datetime.now()
print(timenow)

print(f"sunrise hour:{sunrise}\n ")
print(f"sunset hour:{sunset}")

#Separating the data 2023-07-10T20:19:18+00:00
# print(f"without splitting:      {sunrise}")#Initial run

# print(f"after split(T) :    {sunrise.split('T')}")  #after split(T) ['2023-07-10', '20:19:18+00:00']

#We want to further split the time to look like the datetime module
# print(f"after split :    {sunrise.split('T')[1].split(':')[0]}")


