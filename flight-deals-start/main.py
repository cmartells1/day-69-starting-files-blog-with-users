#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

data_manager = DataManager()
destination_data = data_manager.get_price_data()

if destination_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for place in destination_data:
        place["iataCode"] = flight_search.get_destination_code(place["city"])


data_manager.price_data = destination_data
data_manager.update_price_data()