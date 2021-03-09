# this is the "app/robo_advisor.py" file
import csv
import json 
import os

from dotenv import load_dotenv
from getpass import getpass 
import requests 
import datetime

load_dotenv() # loads content of the .env file into the script's environment (e.g. the secret key)
# credit to https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/packages/dotenv.md

# function to convert float or int to usd-formatted str
# credit to shopping cart project 
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# info outputs 
#

user_symbol = input("Please enter a valid stock ticker, between 1-5 characters long: ")

contains_digit = False
for character in user_symbol:
    if character.isdigit():
        contains_digit = True
if contains_digit == False:
    pass 
else:
    print("OOPS! That doesn't look like a correct stock ticker. ")
    exit()

ticker = user_symbol
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") # was previously "demo"
# will read key from .env file 
# print(api_key) # would not want to do this and expose the key 

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"

response = requests.get(request_url)
# print(type(response)) #> <class "requests.models.Response">
# print(response.status_code)m #> 200
# print(response.text) #> type str
parsed_response = json.loads(response.text)
# converting type string to dictionary so we can work with the text

error_message = "Error Message"
if error_message in parsed_response:
    print("Sorry we could not find any trading data for that symbol. Please try again. ")
    exit()
else:
    pass 

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

if float(latest_closed) <= 1.18*recent_low:
    recommended_choice = "BUY"
else:
    recommended_choice = "DO NOT BUY"


if recommended_choice == "BUY":
    recommended_reason = "The stock's latest closing price is less than 18% of the recent low. "
else:
    recommended_reason = "The stock's latest closing price is greater than 18% of the recent low. "


print("-------------------------")
print(f"Selected Stock Symbol: {ticker}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
# date time module from Shopping Cart project
# credit to https://www.programiz.com/python-programming/time
import time
# allows us to use time. functions 
named_tuple = time.localtime() 
# get struct_time
time_string = time.strftime("%Y-%m-%d, %H:%M:%S", named_tuple)
run_time_date = datetime.datetime.now()
print("Run at: " + run_time_date.strftime("%I:%M %p") + " on " + run_time_date.strftime("%B %d") + ", " + run_time_date.strftime("%Y"))
print("-------------------------")
print(f"Latest data from: {last_refreshed}")
# string interpolation using format string
# could also use concatenation
print(f"Latest Closing Price: {to_usd(float(latest_closed))}")
print(f"Recent High: {to_usd(float(recent_high))}")
print(f"Recent Low: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"Recommendation: {recommended_choice}")
print(f"Recommendation Reason: {recommended_reason}")
print("-------------------------")
print(f"Recommendation Reason: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

