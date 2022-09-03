import requests

TEQUILA_API_KEY = "tDX4BmzE8R0JsIe7IMNyoFRZFr7GA7Ko"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.


    def get_destination_code(self, city_name):
       header = {
           "apikey": TEQUILA_API_KEY
       }

       tequila_params = {
           "term":city_name,
           "location_types" : "city"
       }

       response = requests.get(url=TEQUILA_ENDPOINT, params=tequila_params, headers=header)
       data = response.json()["locations"]
       iata_code = data[0]['code']
       return iata_code