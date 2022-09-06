#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

ORIGIN_CITY_CODE = "YEG"

data_manager = DataManager()
destination_data = data_manager.get_price_data()

if destination_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for place in destination_data:
        place["iataCode"] = flight_search.get_destination_code(place["city"])

    data_manager.price_data = destination_data
    data_manager.update_price_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


flight_search = FlightSearch()
flight_search.check_flights(ORIGIN_CITY_CODE,"YVR",tomorrow, six_month_from_today)