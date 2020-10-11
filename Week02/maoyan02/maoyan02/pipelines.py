# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import sqlconfig

with open('/Users/xuezhong/Python004/Week02/maoyan02/maoyan02/sqlconfig.txt','r') as f:
    a = f.read()
 #创建一个数据表
sql_1 = creat table moiveinfo (movie_title varchar(100),date_time varchar(100),movie_type varchar(100))
    
class Maoyan02Pipeline:
    def __init__(self):
         #连接数据库
        self.conn = pymysql.connect(
        host = re.findall(r'host = (.*)',a),
        port = prot = re.findall(r'port = (.*)',a),
        user = user = re.findall(r'user = (.*)',a),
        password = password = re.findall(r'password = (.*)',a),
        db = re.findall(r'db = (.*)',a),
        charst = 'utf8mb4')
        #建立游标
        self.cur = conn.cursor()
        #运行SQL
        self.cur.execute(sql_1)
    
    def process_item(self, item, spider):
        title = itme['title']
        movie_type = item['movie_type']
        date_time = item['date_time']
        #增添数据
        sql_2 = insert into moiveinfo(movie_title,date_time,movie_type) values(%s,%d,%s) %(title,date_time,movie_type)
        self.cur.execute(sql_2)
        
        #关闭游标
        self.cur.close()
        #关闭数据库
        self.conn.close()
        
        return item


