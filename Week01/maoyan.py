from bs4 import BeautifulSoup as bs
import requests
import re,csv
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko)'
header = {'user-agent':user_agent}
myurl = 'https://maoyan.com/films?showType=3'
response = requests.get(myurl,headers = header)

bs_info = bs(response.text,'html.parser')

for tags in bs_info.find_all('div', attr = {'class':'movie-item-hover'}):
    for atag in tags.find_all('a',):
        name = atag.find('span',class_='name')
        time_ = atag.find('span',class_='hover-tag')
        type_ = atag.find('span',class_='hover-tag')
        with open("movie.csv", "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow({'movie_name':name,'movie_time':time_,'movie_type':type_})

#           