# this is the "app/robo_advisor.py" file

import requests 
import json

# function to convert float or int to usd-formatted str
# credit to shopping cart project 
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# info outputs 
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)
# print(type(response)) #> <class "requests.models.Response">
# print(response.status_code)m #> 200
# print(response.text) #> type str


parsed_response = json.loads(response.text)
# converting type string to dictionary so we can work with the text
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"] # time series daily 

# assume that the latest day is first 
dates = list(tsd.keys())

latest_day = dates[0]

latest_closed = tsd[latest_day[0]]["4. close"]


# high_prices = [1, 2, 3, 4]
# maximum of high prices
# recent_high = max(high_prices)

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
# takes the maximum of the high prices
recent_low = min(low_prices)
# takes the minimum of the low prices

breakpoint()
#
# info outputs 
#


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
# date time module from last project 
#
#
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
# string interpolation using format string
# could also use concatenation
print(f"LATEST CLOSE: {to_usd(float(latest_closed))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
