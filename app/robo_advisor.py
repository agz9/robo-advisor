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

latest_closed = parsed_response["Time Series (Daily)"]["2019-02-20"]["4. close"]

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
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
