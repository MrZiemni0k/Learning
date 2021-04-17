import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
# -------------------- 💡💻 GET ENVIRONMENT VARIABLES 💻💡 ---------------------
load_dotenv("C:/Users/MBloch/Desktop/PythonScripts/.env.txt")
# --------------------------- 💡💻 WEATHER API 💻💡 ----------------------------
WEBSITE = 'https://api.openweathermap.org/data/2.5/onecall'
MY_LAT = 52.17
MY_LON = 21.08
HOURS = 12
API_KEY = os.getenv('Weather_API_KEY')
parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'appid': API_KEY,
    'exclude': 'currently,daily,minutely'
}

will_rain = False

connection = requests.get(WEBSITE, parameters)
connection.raise_for_status()
data = connection.json()['hourly'][:HOURS]
for hour in data:
    if int(hour['weather'][0]['id']) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
# ---------------------- 💡💻 PYTHON ANYWHERE CLOUD 💻💡 -----------------------
# from twilio.http.http_client import TwilioHttpClient
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
# ---------------------------- 💡💻 TWILIO API 💻💡 ----------------------------
MY_SID = os.getenv('Twilio_MY_SID')
MY_TOKEN = os.getenv('Twilio_MY_TOKEN')
MY_PHONE = os.getenv('MY_PHONE')
MY_VPHONE = os.getenv('MY_VPHONE')

client = Client(MY_SID, MY_TOKEN)  # ,http_client=proxy_client) -ANYWHERE CLOUD
if will_rain:
    message = client.messages.create(
            to=MY_PHONE,
            from_=MY_VPHONE,
            body='Bring an ☂ - Within 12 hours it\'s going to rain')

    print(message.status)
