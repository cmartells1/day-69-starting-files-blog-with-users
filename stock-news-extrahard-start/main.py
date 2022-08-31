import requests
import datetime
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "391M2B634DZFJFEA"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
TWILIO_SID = "ACdcf18e261639dc91a6da0288ee00e9d2"
TWILIO_TOKEN = "4772b933e4461387010bd3c8a1974854"

stock_parameters ={
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url=STOCK_API_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data.items()]
yesterday_closing = float(stock_data_list[0]["4. close"])
print(yesterday_closing)
day_before_yesterday_closing = float(stock_data_list[1]["4. close"])
print(day_before_yesterday_closing)
difference = float(yesterday_closing) - float(day_before_yesterday_closing)
up_down = None

if difference > 0:
    up_down = "↑"
else:
    up_down = "↓"

difference_percentage = round((difference / yesterday_closing ) * 100)

yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
if abs(difference_percentage) > 1:
    news_api = "a55f8a892fd24762961825115959ac29"
    news_api_endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": "Tesla",
        "from": yesterday,
        "apiKey":news_api
    }
    news_response = requests.get(url=news_api_endpoint, params=news_parameters)
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]

    formatted_articles = [f"{STOCK}: {up_down}{difference_percentage}% \nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    for article in formatted_articles:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body=article,
            from_='+18302713512',
            to='+1 780 288 2401'
        )

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

