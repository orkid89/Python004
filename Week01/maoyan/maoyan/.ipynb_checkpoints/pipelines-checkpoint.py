# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        title = itme['title']
        movie_type = item['movie_type']
        date_time = item['date_time']
        output = f'|{title}|\t|{movie_type}|\t|{date_time}|\n\n'
        with open('.maoyanmovie.csv','a+',encoding='uft-8') as article:
            article.write(output)
            article.close()
        
        return item
