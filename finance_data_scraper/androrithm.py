import threading
import queue

import json
from datetime import datetime
from requests import get
from scrapers import finviz, stocktwits, zacks

exitFlag = 0
eod_data = {}

global workQueue, queueLock

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      get_symbol_data(self.name, self.q)
      print ("Exiting " + self.name)

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

def get_symbol_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            symbol = q.get()
            queueLock.release()

            try:
                print ("%s processing %s - %d symbols remain" % (threadName, symbol, workQueue.qsize()))
                data = finviz.get_all_statistics(symbol)
                data["zacks"] = zacks.get_rating(symbol)
                data["bull"], data["bear"] = stocktwits.get_sentiment(symbol)
                
                queueLock.acquire()
                eod_data[symbol] = data
                queueLock.release()
            except:
                print("Exception occurred: ", symbol)
        else:
            queueLock.release()
            time.sleep(1)    
    return data

def get_eod_data(symbols):
    global workQueue
    global queueLock
    
    threadList = ["Thr1", "Thr2", "Thr3", "Thr4", "Thr5", "Thr6", "Thr7", "Thr8", "Thr9", "Thr10"]
    queueLock = threading.Lock()
    workQueue = queue.Queue(6000)
    threads = []
    threadID = 1

    # Create new threads
    for tName in threadList:
       thread = myThread(threadID, tName, workQueue)
       thread.start()
       threads.append(thread)
       threadID += 1

    # Fill the queue
    queueLock.acquire()
    for symbol in symbols:
       workQueue.put(symbol)
    queueLock.release()

    # Wait for queue to empty
    while not workQueue.empty():
        pass

    # Notify threads it's time to exit
    exitFlag = 1

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print ("Exiting Main Thread")

if __name__ == "__main__":
    tickers = read_stock_tickers()
    
    get_eod_data(tickers)

    sDate = f"{datetime.now():%Y_%m_%d}"
    write_json_to_file(sDate + ".json", eod_data)
