# robo-advisor
Robo Advisor Project 

# "Robo Advisor" Project

## Prerequisites

  + [Dictionaries](/notes/python/datatypes/dictionaries.md)
  + [Web Requests Exercise](/exercises/web-requests.md)
  + [APIs](/notes/apis.md)
  + [Environment Variables](/notes/environment-variables.md)
  + Python 3.7
  + Anaconda 3.7 
  + Pip 

## Installation

Clone or download this repository (https://github.com/agz9/robo-advisor) on your computer, preferably onto the Desktop where it is easily accessed. Then navigate there from the command line: 

```sh
cd robo-advisor
```

Use Anaconda to create and activate a new virtual environment. Call it stocks-env, or something similar for easy reference.  

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env 
```

From inside of the virtual environment, stocks-env, install pip:
```sh
pip install -r requirements.txt  
```

## More Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API Key, create a new called ".env" (in your local repo, NOT your remote repo), and update the contents of the ".env" file to specify your real API Key:

    ALPHAVANTAGE_API_KEY="abc123"

Don't worry, the ".env" has already been [ignored](/.gitignore) from version control for you!

### Using Robo-Advisor 

From inside stocks-env (or whatever you decide to name the virtual environment), run the code using the following code:
```sh
python app/robo_advisor.py
```

The system should prompt the user to input a stock symbol (e.g. `"MSFT"`, `"AAPL"`, etc.). Before requesting data from the Internet, the system will first perform preliminary validations on user inputs. It will ensure stock symbols are a reasonable amount of characters in length and not numeric in nature.

If preliminary validations are not satisfied, the system will stop execution.

Otherwise, if preliminary validations are satisfied, the system will proceed to issue a GET request to the [AlphaVantage API](https://www.alphavantage.co/documentation/) to retrieve corresponding stock market data. If the stock symbol is not found or if there is an error message returned by the API server, the system will display a friendly error message and stop program execution.

After receiving a successful API response, the system will write historical stock prices to one or more CSV files located in the repository's "data" directory. 