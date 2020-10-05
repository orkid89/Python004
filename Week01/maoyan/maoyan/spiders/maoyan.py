import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem
#from bs4 import BeautifulSoup as bs


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']
    
    def start_requests(self):
        
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url = url,callback=self.parse)

    def parse(self, response):
       # soup = bs(response.text, 'html.parser')
       # titl_list = soup.find_all('dd')[:10]
        
        #for i in title_list:
            
        #    item = MaoyanItem()
        #    title = i.find('a').find('span').text
         #   link = i.find('a').get('href')
          #  item['title'] = title
           # item['link'] = link
        for i in range(10):
            movie = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[i]')
            link = movie.xpath('./a/@href')
            
        yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)
        
    def parse2(self,response):
        item = response.meta['item']
        
        
        date_time = item.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]')
        movie_type = item.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]')
        
        items['date_time'] = date_time
        items['movie_type'] = movie_type
        
        yield item
