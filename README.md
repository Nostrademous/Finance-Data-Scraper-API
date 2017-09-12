Finance Data Scraper API
======
**Finance Data Scraper API** is a web-based RESTFul API that scrapes various financial websites.
It is written in Python 3 and mainly  uses flask, tornado, requests, and lxml

#### Support for
* finviz.com
* StockTwits.com sentiment
* Zacks.com rating and peers

Installation
-----------
```
$ git clone https://github.com/Nostrademous/Finance-Data-Scraper-API.git
$ pip install -r requirements.pip
$ python setup.py install
```

Usage
-----
For the CLI Variant run androrithm: (Currently In Development)
```
$ python androrithm.py
```

For the RESTful Interface Variant run the webserver:
```
$ python webserver.py
Starting ... go get that alpha!
```

Then fire up your favorite browser, curl, or send a HTTP GET request from your app:
```
$ curl http://localhost:8080/finance/finviz/statistics/AAPL
```

Expect a 200 OK Response with a body containing JSON result like this:
```
{
  "52W High": "-13.02%",
  "52W Low": "18.49%",
  "52W Range": "88.99 - 121.23",
  "ATR": "1.53",
  "Avg Volume": "33.22M",
  "Beta": "1.23",
  "Book/sh": "23.25",
  "Cash/sh": "11.20",
  "Change": "2.24%",
  "Current Ratio": "1.30",
  "Debt/Eq": "0.67",
  "Dividend": "2.28",
  "Dividend %": "2.16%",
  "EPS (ttm)": "8.56",
  "EPS Q/Q": "-23.00%",
  "EPS next 5Y": "7.85%",
  "EPS next Q": "1.64",
  "EPS next Y": "7.70%",
  "EPS past 5Y": "33.60%",
  "EPS this Y": "42.80%",
  "Earnings": "Jul 26 AMC",
  "Employees": "110000",
  "Forward P/E": "11.85",
  "Gross Margin": "39.50%",
  "Income": "47.80B",
  "Index": "DJIA S&P500",
  "Insider Own": "0.10%",
  "Insider Trans": "-24.75%",
  "Inst Own": "58.20%",
  "Inst Trans": "-2.54%",
  "LT Debt/Eq": "0.54",
  "Market Cap": "581.32B",
  "Oper. Margin": "28.50%",
  "Optionable": "Yes",
  "P/B": "4.54",
  "P/C": "9.41",
  "P/E": "12.31",
  "P/FCF": "15.30",
  "P/S": "2.64",
  "PEG": "1.57",
  "Payout": "24.70%",
  "Perf Half Y": "4.03%",
  "Perf Month": "-2.31%",
  "Perf Quarter": "8.91%",
  "Perf Week": "-2.13%",
  "Perf YTD": "1.88%",
  "Perf Year": "-5.70%",
  "Prev Close": "103.13",
  "Price": "105.44",
  "Profit Margin": "21.70%",
  "Quick Ratio": "1.30",
  "ROA": "16.00%",
  "ROE": "37.90%",
  "ROI": "28.30%",
  "RSI (14)": "48.13",
  "Recom": "1.80",
  "Rel Volume": "1.35",
  "SMA20": "-2.04%",
  "SMA200": "4.05%",
  "SMA50": "1.99%",
  "Sales": "220.29B",
  "Sales Q/Q": "-14.60%",
  "Sales past 5Y": "29.10%",
  "Short Float": "0.96%",
  "Short Ratio": "1.56",
  "Shortable": "Yes",
  "Shs Float": "5.39B",
  "Shs Outstand": "5.51B",
  "Target Price": "123.66",
  "Volatility": "1.97% 1.25%",
  "Volume": "45,002,637"
}
```
Or perhaps you just want Volume and Volatility:
```
$ curl http://localhost:8080/finance/finviz/statistics/AAPL?fields=Volume,Volatility
```
```
{
  "Volatility": "1.97% 1.25%",
  "Volume": "45,002,637"
}
```
Here is an example of getting StockTwits sentiment:
```
$ curl http://localhost:8080/finance/stocktwits/sentiment/AAPL
```
```
{
  "bearish": "42",
  "bullish": "58"
}
```
### Disclaimer
The scrapers are at the mercy of the respective financial websites as they may update their
style sheets, layout, or even place the desired information behind pay-walls; they are bound
to break eventually. This project will try to keep the scrapers up-to-date but no guarantees.

**Use at your own risk!*** This project or its contributors are not responsible for any abuse or
violations of Terms of Service with any financial websites.

## License
MIT
