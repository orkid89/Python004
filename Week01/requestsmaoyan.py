from bs4 import BeautifulSoup as bs
import requests
import re

url = "https://maoyan.com/films?showType=3"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
    AppleWebKit/537.36 (KHTML, like Gecko)'
header = {}
header['user-agent'] = user_agent
response = requests.get(url, headers=header).text

news_bs = bs(response,'html.parser')

for urg in news_bs.find_all('dd'):
    for href in urg.find('a'):
        href_url = requests.get(url)
        print(href_url)