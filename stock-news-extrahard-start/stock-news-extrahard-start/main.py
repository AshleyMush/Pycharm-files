import requests
from datetime import datetime

date_time = datetime.today()
date_only = date_time.date()
print(date_only)


api_key = "34G2CWF5SJ5KWI9S"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#____________End_points_Stock_________________
SME_endpoint = "https://www.alphavantage.co/query"
SME_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey": api_key,

}

#________________End_Points_News__________

News_endpoint = "https://www.alphavantage.co/query"

# New_Params = {
#     "function":"NEWS_SENTIMENT",
#     "tickers":"stock",
#     "topics":"finance"
#     "time_from": f""
#     "time_to" : f""
#
#
#
#
# }





#________________Requests_______________
response = requests.get(SME_endpoint,params=SME_params)
response.raise_for_status()
data = response.json()
print(data)

daily_data = data["Time Series (Daily)"]

#Add all the data into lists
date_list = [key for key, value in data["Time Series (Daily)"].items()]
closing_value_list=[value['4. close'] for key, value in data["Time Series (Daily)"].items()]

yesterday = date_list[0]
day_beforre_yesterday = date_list[1]
print(yesterday)

yesterday_closing_STOCK_PRICE = float(closing_value_list[0])
day_before_closing_STOCK_PRICE = float(closing_value_list[1])

#Calculating the difference
difference = yesterday_closing_STOCK_PRICE - day_before_closing_STOCK_PRICE
percentage = abs(round(difference / yesterday_closing_STOCK_PRICE * 100))

print(f"the difference is ${difference}")
print(f"the percentage in the difference is %{percentage}")

if percentage == 5:
    #TODO ADD NEWS HERE
    print("Get news")
elif percentage == -5:
    print("Get news")


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}'
# r = requests.get(url)


# # print(data["Time Series (Daily)"])
#
# daily_data = data["Time Series (Daily)"]
#
#
# data_list = []
# for key, value in data["Time Series (Daily)"].items():
#     # print(key)
#     data_list.append(key)
#
# today_date = data_list[0]
# yesterday_date = data_list[1]
#
# today_closing_price = daily_data[today_date]["4. close"]
# print(int(today_closing_price))

    # data_list.append(key, value)

#TODO:
"""

#Class Stock_prices:
    attribute: stock price
    
    method:Get stock prices 
    method: compare  closing price of  yesterday's  stock to today's
"""
"""
    
Class news:
    attribute:headline
    
    method: fetch the latest news
            if stock_price_difference > 10%
            
class sms sender:
    attribute; stock_price_alert
    
    method:message = "stock_price diff abd percent | revelant news"
    -




"""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

