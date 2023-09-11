import requests


api_key = "34G2CWF5SJ5KWI9S"
COMPANY_NAME = "Tesla Inc"

class Stock_Price:
    def __init__(self,STOCK):

        self.SME_endpoint = "https://www.alphavantage.co/query"
        self.SME_params = {
            "function":"TIME_SERIES_DAILY",
            "symbol":STOCK,
            "apikey": api_key,

        }
        self.response = requests.get(self.SME_endpoint,params=self.SME_params)
        self.response.raise_for_status()
        self.data = self.response.json()

        self.daily_data = self.data["Time Series (Daily)"]

        #Add all the data into lists
        self.date_list = [key for key, value in self.data["Time Series (Daily)"].items()]
        self.closing_value_list=[value['4. close'] for key, value in self.data["Time Series (Daily)"].items()]

        self.yesterday_closing_STOCK_PRICE = float(self.closing_value_list[0])
        self.day_before_closing_STOCK_PRICE = float(self.closing_value_list[1])

    def Cal_difference(self):    #Calculating the difference
        self.difference = self.yesterday_closing_STOCK_PRICE - self.day_before_closing_STOCK_PRICE
        percentage = round(self.difference / self.yesterday_closing_STOCK_PRICE * 100)
        return percentage

        # print(f"the difference is ${difference}")
        # print(f"the percentage in the difference is %{percentage}")
        #
        # if percentage == 5:
        #     #TODO ADD NEWS HERE
        #     print("Get news")
        # elif percentage == -5:
        #     print("Get news")
