import requests
from datetime import datetime

USERNAME = "cmartells"
TOKEN = "ndfsipjfpwion23pn3ikpenr2pn3k"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "ndfsipjfpwion23pn3ikpenr2pn3k",
    "username": "cmartells",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# today = datetime(year=2022, month=8, day= 30)

# post_pixel_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "50"
# }
#
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)

today = datetime(year=2022, month=8, day= 30).strftime("%Y%m%d")

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_pixel_data = {
    "quantity": "13.3"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)