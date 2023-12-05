# WEB_SCRAPPING: is extracting DATA from a website
# We'll send a request to that URL will want to scrap
# And get a response bck which data we need
# We need two Python Libraries:
# 1: Requests: used for sending request
# 2: BeautifulSoup: Used in extracting and receiving the data we need.
# bs4 as recognised by the window's machine.

import requests
from bs4 import BeautifulSoup

url = "https://nambativep.github.io/"
r = requests.get(url)
r