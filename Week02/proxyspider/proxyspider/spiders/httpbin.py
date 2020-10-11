import scrapy
#export http_proxy='http://52.179.231.206:80'
#setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
#通过Requests.meta['proxy']读取 http_proxy 环境变量加载代理

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)
