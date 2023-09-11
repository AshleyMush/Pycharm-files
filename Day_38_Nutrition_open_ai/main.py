import requests
from datetime import datetime
import os



GENDER = 'male'
WEIGHT_KG =83.5
HEIGHT_CM = 170
AGE = 26


#____________________________ENV Variables_________________________________#
"""
go to main> edit config> Env var


"""
TOKEN = os.environ.get("TOKEN","Token doe'st exist")
APP_ID = os.environ.get("APP_ID", "Please double check your App ID")
API_KEY = os.environ.get("API_KEY", "Please check your API key and try again")


SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT", "Check your end point")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

#_____________Sheety api

date_info = datetime.now()
#___________________Formatting the date
DATE = date_info.strftime("%d%m%Y")

timeinfo = date_info.time()
TIME= timeinfo.strftime("%X")





#Posting a row
for exercise in result['exercises']:
    sheety_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise['nf_calories']
        }

     }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheety_params)

    # _________________Sheety Authentication___________
    bearer_header = {
        "Authorization": F"Bearer {TOKEN}"

    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheety_params, headers=bearer_header)


# {'exercises':
#               [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 30.02, 'met': 9.8, 'nf_calories': 409.42, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None
#  }]}




