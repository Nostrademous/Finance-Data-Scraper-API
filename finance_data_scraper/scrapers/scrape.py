#!/usr/bin/python3

from scrapers import cache
from requests import get
from lxml import html

def scrape_page(url):
    """
    Scrapes a web page given a url and returns an HTML tree representation.
    This will check for a cachced version of the page before scraping and will attempt to cache
    after scraping
    :param url: A string of the url of the requested web page
    :return: html tree structure based on the html markup of the scraped website
    """
    cached_page = cache.get(url)

    if cached_page:
        return html.fromstring(cached_page)
    else:
        page = get(url, headers={'User-Agent': 'Firefox/12.0'})

        cache.set(url, page.text)

        return html.fromstring(page.text)
