import requests
from datetime import datetime
import os


APP_ID = "a93a8c0c"
MY_GENDER = "male"
MY_WEIGHT = 80.23
MY_HEIGHT = 167.64
MY_AGE = 26
MY_QUERY = input("How was the exercise today ? : ")
TOKEN = os.environ['MY_TOKEN']
API_KEY = os.environ["MY_API_KEY"]
ENDPOINT_URL = os.environ["MY_ENDPOINT URL"]


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY

}
exercise_params = {
    "query": MY_QUERY,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE

}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_params, headers=headers)
print(response.text)
result = response.json()
print(result)

today = datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%X")
#
# exercise_name = result['exercises'][0]['user_input']
#
# exercise_time = result['exercises'][0]['duration_min']
#
# energy = result['exercises'][0]['nf_calories']

print(result["exercises"])


bearer_header = {
    "Authorization": f"Bearer {TOKEN}"
}

# sheet_add = []
for exercise in result["exercises"]:
    sheet_add = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise['user_input'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']

        }
    }
    # sheet_add.append(adding_a_sheet)
print(sheet_add)

add_to_sheet = requests.post(url=ENDPOINT_URL,
                             json=sheet_add,headers=bearer_header)
print(add_to_sheet.text)























# import requests
# from datetime import datetime
# import os
#
# GENDER = YOUR GENDER
# WEIGHT_KG = YOUR WEIGHT
# HEIGHT_CM = YOUR HEIGHT
# AGE = YOUR AGE
#
# APP_ID = os.environ["YOUR_APP_ID"]
# API_KEY = os.environ["YOUR_API_KEY"]
#
# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = os.environ["YOUR_SHEET_ENDPOINT"]
#
# exercise_text = input("Tell me which exercises you did: ")
#
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }
#
# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }
#
# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(result)
#
# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")
#
# for exercise in result["exercises"]:
#     sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
#
#     #No Auth
#     sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
#
#     #Basic Auth
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         auth=(
#             os.environ["USERNAME"],
#             os.environ["PASSWORD"],
#         )
#     )
#
#     #Bearer Token
#     bearer_headers = {
#     "Authorization": f"Bearer {os.environ['TOKEN']}"
#     }
#     sheet_response = requests.post(
#         sheet_endpoint,
#         json=sheet_inputs,
#         headers=bearer_headers
#     )
#
#     print(sheet_response.text)
