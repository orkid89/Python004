from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd

url = "https://maoyan.com/films?showType=3"
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
    AppleWebKit/537.36 (KHTML, like Gecko)'
header = {}

header['user-agent'] = user_agent

response = requests.get(url, headers=header)

bs_info = bs(response.text,'html.parser')

data = bs_info.find_all('dd')[:10]

movielist = []

for dd in data:
    movie_name = dd.find('span', attrs={"class": "name"}).text
    movie_type = dd.find("div", attrs={"class": 'movie-hover-info'}).select("div")[1].get_text().\
    replace('类型:', '').replace(' ', '').replace('\n', '')
    movie_time = dd.find("div", attrs={"class": 'movie-hover-info'}).select("div")[3].get_text().\
    replace('上映时间:', '').replace(' ', '').replace('\n', '')
    
    slist = [movie_name,movie_type,movie_time]
    
    movielist.appent(slist)
    
    movie = pd.DataFrame(data = movielist)

    movie.to_csv('./movie1.csv',encoding='utf8',index=False,header=False)

    
