import requests

SHEETY_ENDPOINT = "https://api.sheety.co/7095f78aba4405d785c4613307c47b46/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.price_data = {}


    def get_price_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()["prices"]
        self.price_data = data
        return data

    def update_price_data(self):
        for city in self.price_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json= new_data
            )

            print(response.text)