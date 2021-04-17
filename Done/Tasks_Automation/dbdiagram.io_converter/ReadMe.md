# Stock News Alert SMS

Sends sms messeges with 3 newest news articles to an user if intraday 
exchange of stock of his choice was down or up for more than 5%.

## Details:

Using AlphaAdvantage API checks % change of stock price. 
Using NewsApi module gets 3 news articles about the stock.
If intraday change % was more than 5% then user will get news articles via 
sms message using Twilio Client. 

## Level:
    Intermediate+

## Built with
* Python
    - Module
        - [requests](https://pypi.org/project/requests/)
        - [os](https://docs.python.org/3/library/os.html)
        - [dotenv](https://pypi.org/project/python-dotenv/)
        - [twilio.rest](https://www.twilio.com/docs/usage/api)
        - [newsapi](https://newsapi.org/docs/client-libraries/python)
* API
    - [Twilio](https://www.twilio.com/docs/api)
    - [NewsApi](https://newsapi.org/docs/)

### Visualisation

![](Stock.gif)
