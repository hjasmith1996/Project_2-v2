from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

from main_classes import *
from common_functions import *





wikipedia_xpaths = Wikipedia_Xpath_selection
this_months_dictionary = {'months_rank_list' : [], 'months_exchange_list' : [], 'months_location_list' : [], 'months_market_cap_list' : [], 'months_trade_volume_list' : [], 'current_column' : [], 'table_header_children' : []}
exchange_URL = 'https://en.wikipedia.org/w/index.php?title=List_of_stock_exchanges&action=history'
weather_URL = 'https://www.wunderground.com/history'
certain_stock_exchange_url = 'https://en.wikipedia.org/w/index.php?title=List_of_stock_exchanges&oldid=1040911711'
x = our_parameters.return_URL_sleeping_list()



url_scraper = Location_Url_Scrape(sleeping_amounts = our_parameters.return_URL_sleeping_list())
driver = webdriver.Chrome('chromedriver.exe')
location_urls = []
url_scraper.complete_url_scrape(driver = webdriver.Chrome('chromedriver.exe'), list_of_locations = ['New York', 'Tokyo', 'Amsterdam', 'Berlin', 'Madrid'], location_urls = [])
