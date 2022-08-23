import requests

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast"
api_key = "c39c44dfe468a5e4a83640c1e27119a5"


MY_LAT = 53.544388
MY_LONG = -113.490929

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
# weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if(will_rain):
    print("Bring an umbrella")
# print(weather_data["hourly"][0]["weather"][0]["id"])