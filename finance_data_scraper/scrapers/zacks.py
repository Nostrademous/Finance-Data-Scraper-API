#!/usr/bin/python3

from scrapers.scrape import scrape_page
# if you want to use this scraper without the RESTful api webservice then
# change this import: from scrape import scrape_page

BASE_URL = "http://www.zacks.com/stock/quote/"
RATING_XPATH = '//*[@id="premium_research"]/div/table/tbody/tr[1]/td/strong/text()'
PEERS_XPATH = '//*[@id="stock_industry_analysis"]/table/tbody/tr/td[2]/a/span/text()'
STYLE_SCORES_XPATH = '//*[@id="premium_research"]/div/table/tbody/tr[3]/th/p/span/text()'
STYLES = ["Value", "Growth", "Momentum", "VGM"]
INDUSTRY_RANK_XPATH = '//*[@id="premium_research"]/div/table/tbody/tr[2]/td/a/text()'

def get_rating(ticker_symbol, page=None):
    """
    Gets the Zack's Rank Rating of the target ticker symbol
    :param ticker_symbol: The ticker symbol of the interested stock (e.g., "AAPL", "GOOG", "MSFT")
    :param page: html tree structure based on the html markup of the scraped website
    :return: String of Zack's Rank Rating as listed on a stock's Zacks page
    """
    if page is None:
        page = scrape_page(BASE_URL + ticker_symbol)

    rating = page.xpath(RATING_XPATH)

    if not rating:
        return "N/A"
    else:
        return rating[0]

def get_peers(ticker_symbol, page=None):
    """
    Gets the list of Top Peers for a stock as listed on the "Premium Research: Industry Analysis" section
    :param ticker_symbol: The ticker symbol of the interested stock (e.g., "AAPL", "GOOG", "MSFT")
    :param page: html tree structure based on the html markup of the scraped website
    :return: a list of the Top Peers as listed on a stock's "Premium Research: Industry Analysis" section
    on it's respective zacks page
    """
    if page is None:
        page = scrape_page(BASE_URL+ ticker_symbol)

    peers = page.xpath(PEERS_XPATH)

    if peers:
        try:
            peers.remove(ticker_symbol.upper())
        except:
            pass

        if peers:
            return peers
        else:
            return None
    else:
        return None

def get_style_scores(ticker_symbol, page=None):
    """
    Gets the Zacks' Style Scores of the target ticker symbol. There are 4 score categories Value, Growth, Momentum
    and VGM. Each category is given a grade from A - F.
    :param ticker_symbol: The ticker symbol of the interested stock (e.g., "AAPL", "GOOG", "MSFT")
    :param page: html tree structure based on the html markup of the scraped website
    :return: a dictionary containing all the Style Scores
    """
    if page is None:
        page = scrape_page(BASE_URL + ticker_symbol)

    scores = page.xpath(STYLE_SCORES_XPATH)

    if not scores:
        return None
    else:
        return dict(zip(STYLES, scores))

def get_industry_rank(ticker_symbol, page=None):
    """
    Gets the Zacks' Industry Rank of the target ticker symbol.
    :param ticker_symbol: The ticker symbol of the interested stock (e.g., "AAPL", "GOOG", "MSFT")
    :param page: html tree structure based on the html markup of the scraped website
    :return: a string of the industry rank 
    """
    if page is None:
        page = scrape_page(BASE_URL + ticker_symbol)

    industry_rank = page.xpath(INDUSTRY_RANK_XPATH)

    if not industry_rank:
        return None
    else:
        return industry_rank[0]

if __name__ == "__main__":
    # Test cases
    print (get_rating("AAPL"))
    print (get_peers("GOOG"))
