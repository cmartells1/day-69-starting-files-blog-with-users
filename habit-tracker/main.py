import requests

USERNAME = "cmartells"
TOKEN = "ndfsipjfpwion23pn3ikpenr2pn3k"

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
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)