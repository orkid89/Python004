import scrapy
from scrapy.selector import Selector
from items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        items = items = MaoyanItem()
        i = 0
        
        while i<10:
            urls = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
            for url in urls:
                
                link = url.xpath('./a/@href')    
                items.append(link)
                
            i += 1  
            
        yield scrapy.Request(url=link,callback=self.parse2)
        
    def parse2(self,response):
        item = response.meta['item']
        items =[]
        
        title = item.xpath('/html/body/div[3]/div/div[2]/div[1]/h1')
        date_time = item.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]')
        movie_type = item.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]')
        
        items['title'] = title
        items['date_time'] = date_time
        items['movie_type'] = movie_type
        
        yield item
