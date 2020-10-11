import scrapy
from scrapy.selector import Selector
from maoyan02.items import Maoyan02Item

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan02'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']
    
    def start_requests(self):
        
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url = url,callback=self.parse)

    def parse(self, response):
       
        for i in range(10):
            movie = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[i]')
            link = movie.xpath('./a/@href')
            
        yield scrapy.Request(url=link,meta={'item':item},callback=self.parse2)
        
    def parse2(self,response):
        item = response.meta['item']
        
        try:
            movie_title = item.xpath('/html/body/div[3]/div/div[2]/div[1]/h1')
            date_time = item.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]')
            movie_type = item.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]')
        except Exception:
            print('Download Error')
            
        items['date_time'] = date_time
        items['movie_type'] = movie_type
        
        yield item
