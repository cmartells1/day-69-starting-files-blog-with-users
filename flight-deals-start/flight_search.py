import requests
from flight_data import FlightData


TEQUILA_API_KEY = "tDX4BmzE8R0JsIe7IMNyoFRZFr7GA7Ko"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


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

       response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=tequila_params, headers=header)
       data = response.json()["locations"]
       iata_code = data[0]['code']
       return iata_code


    def check_flights(self, origin_code, destination_code, from_time, to_time):
        header = {
            "apikey": TEQUILA_API_KEY
        }

        query = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers= header, params=query)
        data = response.json()["data"][0]
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city} : ${flight_data.price}")
        return flight_data

