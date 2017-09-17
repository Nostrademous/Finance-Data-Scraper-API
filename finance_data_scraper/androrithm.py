import json
from datetime import datetime
from requests import get
from scrapers import finviz, stocktwits, zacks

def read_stock_tickers():
    stock_list = []
    f = open("stock_tickers.txt", "r")

    for line in f:
        #print(line, end='')
        stock_list.append(line.strip())

    f.close()
    return stock_list

def write_json_to_file(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=2)

def get_eod_data(symbols):
    eod_data = {}

    cnt = len(symbols)
    count = 1
    for symbol in symbols:
        print("Acquiring Following Ticker: ", symbol, "%d out of %d" % (count, cnt))

        try:
            data = finviz.get_all_statistics(symbol)
            data["zacks"] = zacks.get_rating(symbol)
            data["bull"], data["bear"] = stocktwits.get_sentiment(symbol)

            eod_data[symbol] = data
        except:
            print("Exception occurred: ", symbol)
        finally:
            count += 1
        
    return eod_data

if __name__ == "__main__":
    tickers = read_stock_tickers()
    
    data = get_eod_data(tickers)

    sDate = f"{datetime.now():%Y_%m_%d}"
    write_json_to_file(sDate + ".json", data)
