import smtplib
import os
from twilio.rest import Client
import  requests

#--------------Twilio setup_____

account_sid = 'AC6f116151d21a4d82a76413bc5f07b6ca'
auth_token = 'b498a4bb728a1093d016af30fa804f80'

api_key = "0d75e43670b2ffca4032c37ae7d31c39"

MY_LAT = "19.076090"
MY_LONG = "72.877426"
# MY_LAT = 51.752022
# MY_LONG = -1.257677

OWM_End_point = "https://api.openweathermap.org/data/2.8/onecall"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude":"current,minutely,daily",




}

response = requests.get(OWM_End_point, params=weather_params)
response.raise_for_status()

data = response.json()
print(data)

# weather_id = data["hourly"][0]["weather"][0]["id"]
#
# print(weather_id) #00:00

# for hour in range(1,13):
#
#     print(hour)

will_rain = False

weather_slice =  data["hourly"][:12] #[START:STOP-1] len = 12
for hour_data in weather_slice:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Bring an umbrella⛈!',
        from_='+447883304338',
        to='+447478881797'
    )

    print(message.status)


# weather_IDs = []
# for hour in range(1,13):
#     weather_id = data["hourly"][hour]["weather"][0]["id"]
#
#     weather_IDs.append(weather_id)
# for id in weather_IDs:
#     if id <=  700:
#         print("Bring an Umbrella")
#
# print(weather_IDs)



# weather_IDs = [hour for  hour in range(13)]


#
# # OMW_End_point = "https://api.openweathermap.org/data/2.5/onecall"
# # weather_params = {
# #     "lat": MY_LAT,
# #     "lon": MY_LONG,
# #     "appid": api_key,
# #
# #
# #
# # }
# #
# # response = requests.get(OMW_End_point, params=weather_params)
#
# api = f"https://api.openweathermap.org/data/2.5/weather?lat=51.752022&lon=-1.257677&units=metric&appid={api_key}"
# response = requests.get(api)
#
#
#
# data = response.json()
#
# print(data)
#
#
#
