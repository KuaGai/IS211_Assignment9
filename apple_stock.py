#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This module generates Apple's stock

import urllib.request, urllib.error, urllib.parse
import json
from bs4 import BeautifulSoup

'''For some reason the nasdaq link (https://www.nasdaq.com/market-activity/stocks/aapl/historical)
will not pull the stock data. The script runs without any erros but does not show data.
I had to use the YAHOO stock link instead.'''

url ='http://finance.yahoo.com/quote/AAPL/history?ltr=1'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")


def appleStock():
    rows = soup.find_all('tr')
    for i in rows:
        try:
            date = i.contents[0].get_text()
            close = i.contents[5].get_text()
            json_string = {"Date": date, "Close_Price": close}
            print((json.dumps(json_string)))
        except:
            continue
    return


if __name__ == "__main__":
    appleStock()
