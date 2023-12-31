#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
destination_data = data_manager.get_price_data()

if destination_data[0]["iataCode"] == "":
    for place in destination_data:
        place["iataCode"] = flight_search.get_destination_code(place["city"])

    data_manager.price_data = destination_data
    data_manager.update_price_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in destination_data:
    flight = flight_search.check_flights(ORIGIN_CITY_CODE, destination["iataCode"], tomorrow, six_month_from_today)
    if flight is None:
        continue

    if flight.price < destination_data[destination]["price"]:
       users = data_manager.get_customer_emails()
       emails = [row["email"] for row in users]
       names = [row["firstName"] for row in users]

       message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

       if flight.stop_overs > 0:
           message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

           link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

           notification_manager.send_emails(emails, message, link)


        # flight.price < destination["lowestPrice"]:
        # notification_manager.send_sms(f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.departure_date} to {flight.return_date}")
