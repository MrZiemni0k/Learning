from dotenv import load_dotenv
from newsapi import NewsApiClient
from twilio.rest import Client
import os
import requests
# -------------------- 💡💻 GET ENVIRONMENT VARIABLES 💻💡 ---------------------
load_dotenv("C:/Users/MBloch/Desktop/PythonScripts/.env.txt")
# ------------------------- 💡💻 ALPHAVANTAGE API 💻💡 -------------------------
STOCK = "AMC"
ALPHA_WEBSITE = 'https://www.alphavantage.co/query'
ALPHA_API_KEY = os.getenv('Alphavantage_API_KEY')
ALPHA_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_API_KEY
    }

connection = requests.get(ALPHA_WEBSITE, ALPHA_parameters)
connection.raise_for_status()
stock_data = list(connection.json()['Time Series (Daily)'].items())[:2]
# ----------------------------- 💡💻 NEWS API 💻💡 -----------------------------
NEWS_API_KEY = os.getenv('News_API_KEY')
COMPANY_NAME = "AMC Entertainment Holdings Inc"
news_date_from = stock_data[1][0]

newsapi = NewsApiClient(api_key=NEWS_API_KEY)
all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      from_param=news_date_from,
                                      language='en',
                                      sort_by='publishedAt')
top_articles = all_articles['articles'][:3]
# ---------------------- 💡💻 PYTHON ANYWHERE CLOUD 💻💡 -----------------------
# from twilio.http.http_client import TwilioHttpClient
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
# ---------------------------- 💡💻 TWILIO API 💻💡 ----------------------------
MY_SID = os.getenv('Twilio_MY_SID')
MY_TOKEN = os.getenv('Twilio_MY_TOKEN')
MY_PHONE = os.getenv('MY_PHONE')
MY_VPHONE = os.getenv('MY_VPHONE')


def prepare_news():
    message_text = ''
    for news in top_articles:
        message_text += news['title'] + '\n' + news['description'] + '\n\n'
    return message_text


def send_sms():
    client = Client(MY_SID, MY_TOKEN)  # ,http_client=proxy_client)
    client.messages.create(
            to=MY_PHONE,
            from_=MY_VPHONE,
            body=(f'{STOCK}: {emoji_msg}{abs(stock_day_change)}%\n'
                  f'{prepare_news()}')
            )


# ----------------------- 💡💻 COMPARE DAILY TRADES 💻💡 -----------------------
stock_day_change = round(
        (
                (float(stock_data[0][1]['4. close']) /
                 float(stock_data[1][1]['4. close']) - 1
                 ) * 100), 2
        )
# EMOJI FOR Message
if stock_day_change < 0:
    emoji_msg = '🔻'
elif stock_day_change > 0:
    emoji_msg = '🔺'
if abs(stock_day_change) > 5:
    send_sms()
