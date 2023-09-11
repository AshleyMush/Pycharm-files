import requests
from datetime import datetime

date_info = datetime.now()
#___________________Formatting the date
date = date_info.strftime("%Y%m%d")

USERNAME = "ashleytanaka"
TOKEN = "Ashley1998"
GRAPHID = "mygraph1"

#Setting up a user account
pixela_endpoint = "https://pixe.la//v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"



}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphs_config = {
    "id": GRAPHID ,
    "name": "python_graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"


}

headers = {
    "X-USER-TOKEN": TOKEN

}

# response = requests.post(url=graph_endpoint, json=graphs_config, headers=headers)
# print(response.text)

#____________________Posting a pixel______________

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_params = {
    "date": date,
    "quantity": "15",


}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)


#_____________________Put pixel (update)_____________________#
pixel_UPDATE_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{date}"


pixel_params_UPDATE = {
    "quantity": input("How many hours did you study?"),


}


# response = requests.put(url=pixel_UPDATE_endpoint, json=pixel_params_UPDATE, headers=headers)

#______________DELETING A PIXEL__________
response = requests.delete(url=pixel_UPDATE_endpoint, headers=headers)


print(response.text)





