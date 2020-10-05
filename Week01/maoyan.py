import scrapy
from maoyan.items import MaoyanItem
from bs4 import BeautifulSoup as bs

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']
    
    def start_request(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url,callback=self.parse)
        
    def parse(self, response):
        
        items = []
        soup = bs(response.text,'html.parse')
        title_list = soup.find_all('dd')[:10] 
        
        for i in title_list:
            item = MaoyanItem()
            title = title_list[1].find('a').find('span').text
            date_time = title_list[1].find('a').find('span').text
            movie_type = title_list[1].find('a').find('span').text
            
            items['title'] = title
            items['date_time'] = date_time
            items['movie_type'] = movie_type
        
        yield item
