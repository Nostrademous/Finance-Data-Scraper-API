#!/usr/bin/python3

from scrapers.scrape import scrape_page
# if you want to use this scraper without the RESTful api webservice then
# change this import: from scrape import scrape_page


BASE_URL = "http://stocktwits.com/symbol/"
BULLISH_SENTIMENT_XPATH = '//*[@id="sentiment-chart"]/div/ul/li[1]/span/text()'
BEARISH_SENTIMENT_XPATH = '//*[@id="sentiment-chart"]/div/ul/li[2]/span/text()'

def get_bullish_sentiment(ticker_symbol, page=None):
    """
    Gets the bullish sentiment of the target ticker symbol
    :param ticker_symbol: The ticker symbol of the interested stock (e.g., "AAPL", "GOOG", "MSFT")
    :param page: html tree structure based on the html markup of the scraped website
    :return: a string of the percentage of bullish sentiment as listed on a stock's StockTwit's page
    """
    if page is None:
        page = scrape_page(BASE_URL + ticker_symbol)

    sentiment = page.xpath(BULLISH_SENTIMENT_XPATH)

    if not sentiment:
        return None
    else:
        return sentiment[0].replace("\n", "").replace("%", "")

def get_bearish_sentiment(ticker_symbol, page=None):
    """
    Gets the bearish sentiment of the target ticker symbol
    :param ticker_symbol: The ticker symbol of the interested stock (e.g., "AAPL", "GOOG", "MSFT")
    :param page: html tree structure based on the html markup of the scraped website
    :return: a string of the percentage of bearish sentiment as listed on a stock's StockTwits page
    """
    if page is None:
        page = scrape_page(BASE_URL + ticker_symbol)

    sentiment = page.xpath(BEARISH_SENTIMENT_XPATH)

    if not sentiment:
        return None
    else:
        return sentiment[0].replace("\n", "").replace("%", "")

def get_sentiment(ticker_symbol, page=None):
    """
    Gets both the bullish and bearish sentiment of the target ticker symbol
    :param ticker_symbol: The ticker symbol of the interested stock (e.g., "AAPL", "GOOG", "MSFT")
    :param page: html tree structure based on the html markup of the scraped website
    :return: a tuple of strings containing both the bullish and bearish sentiment as listed on a stock's
    StockTwits page
    """
    if page is None:
        page = scrape_page(BASE_URL + ticker_symbol)

    bullish_sentiment = get_bullish_sentiment(ticker_symbol, page)

    if bullish_sentiment:
        return bullish_sentiment, get_bearish_sentiment(ticker_symbol, page)
    else:
        return None, None

if __name__ == "__main__":
    # Test cases
    print(get_sentiment("GOOG"))
