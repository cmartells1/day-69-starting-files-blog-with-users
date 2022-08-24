import requests
from twilio.rest import Client

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"
api_key = "c39c44dfe468a5e4a83640c1e27119a5"
account_sid = "ACdcf18e261639dc91a6da0288ee00e9d2"
auth_token = "34f55bba1a21ef00008c83e258184b9b"

MY_LAT = 64.3
MY_LONG = 30.8

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:5]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True

if(will_rain):
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Bring an umbrella",
            from_='+18302713512',
            to='+1 780 288 2401'
            )
    print(message.status)