import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWN_Endpoint  = "http://api.openweathermap.org/data/2.5/onecall"
api_key = "dc7181e72ff0ed23810e1c3a650acfaf"

account_sid = "ACf1aea8af91ad1760cf4b303f18324862"
auth_token = "a1b09a95390b317165e018084a2d90a6"  # NEW AUTH TOKEN AVAILABLE IN THE TWILIO PAGE

weather_params = {
    "lat": 17.686815,
    "lon": 83.218483,
    "appid": api_key,
    "exclude": "minutely,daily,current"
}

response = requests.get(OWN_Endpoint, params = weather_params)
response.raise_for_status()
print(response.status_code)

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)


print(weather_data["hourly"][0]['weather'][0]['id'])

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    print("make sure to carry an umbrella")
    proxy_client = TwilioHttpClient()
    try:
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    except KeyError:
        pass
    client = Client(account_sid, auth_token , http_client=proxy_client)
    message = client.messages \
        .create(
        body="It is going to rain today_ make sure to carry an umbrerlla :) 🍇",
        from_= "+12058289438",
        to='+91 YOUR TWILIO NUMBER',
    )
    print(message.status)

else:
    print("The weather looks fine today")
    proxy_client = TwilioHttpClient()
    try:
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    except KeyError:
        pass
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's not raining for sure 😎 😎 🥵",
        from_="+12058289438",
        to='+91 YOUR TWILIO NUMBER',
    )
    print(message.status)
