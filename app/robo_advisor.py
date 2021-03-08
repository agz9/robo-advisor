# this is the "app/robo_advisor.py" file

import csv
import json
import os
# keep modules before packages 
import requests 

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
latest_closed = tsd[latest_day]["4. close"]


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

# breakpoint()
#
# info outputs 
#

#csv_file_path = "data/prices.csv" # a relative file path 
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
# credit to https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md
# uses the os module 
# .. helps navigate up one directory to the root 
# enables us to standardize paths across operating systems 

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: 
# "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames = csv_headers)
    # need to get a list of headers from the original url 
    writer.writeheader() # uses fieldnames set above
    for date in dates:
    # some looping here to write each row 
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": "date",
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
            })

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


