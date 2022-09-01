import requests
from datetime import datetime

APP_ID ="e0a3d083"
API_KEY = "86b2af44ca159c559e598dfc127c504c"

GENDER = "male"
WEIGHT = 181.43
HEIGHT = 175.26
AGE = 36

headers = {
    "x-app-id":APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_query = input("Tell me which exercise you did: ")
print(exercise_query)

exercise_params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
# print(result['exercises'][0]['user_input'])
print(result)
today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheety_endpoint = "https://api.sheety.co/7095f78aba4405d785c4613307c47b46/chris'sWorkouts/workouts"

for exercise in result['exercises']:
    sheety_entries = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories" : exercise['nf_calories']

        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_entries)

    print(sheety_response.text)

