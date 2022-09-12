import requests

SHEETY_ENDPOINT = "https://api.sheety.co/4bf543ec77fec1ec8137a28626db6b34/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/4bf543ec77fec1ec8137a28626db6b34/flightDeals/users"
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.customer_data = None
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

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

