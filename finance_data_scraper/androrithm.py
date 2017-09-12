from datetime import datetime
from requests import get
from scrapers import finviz, stocktwits, zacks

def get_eod_data():
    symbols = ["VSM"]

    eod_data = {}

    sDate = f"{datetime.now():_%Y%m%d}"
    
    for symbol in symbols:
        data = finviz.get_all_statistics(symbol)
        data["bull"], data["bear"] = stocktwits.get_sentiment(symbol)
        data["zacks"] = zacks.get_rating(symbol)
        
        eod_data[symbol] = data
        
    return eod_data

if __name__ == "__main__":
    data = get_eod_data()
    
    print(data)
