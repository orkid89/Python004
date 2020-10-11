学习笔记
1.MySQL
  1.1 链接本地数据库
      1.1.1 PATH="$PATH":/usr/local/mysql/bin #设置(local)环境变量(中间不能加空格），这种设置方法是本地环境变量，就是说每次退出终端再重启你都要重新输入这行命令；如何设置全局环境变量可参考1.1.2
      1.1.2 mysql -u root -p # 这是客户端连接mysql服务器的指令， -u后接用户名，默认用户名是root，-p表示输入密码,回车后提示输入密码，然后进入SQL
      1.1.3 show databases； # ”；“不能省略，可以查看所有本地数据库
      1.1.4 \q 或者 exit 可以退出sql
  1.2 创建一个本地数据库
      1.2.1 create database testdb;  #创建一个testdb 的数据库，分号不能省，在sql的模式下输入命令语句
      1.2.2 show databases;          #可以用此命令来查看创建的数据库是否成功
      1.2.3 use testdb;              #进入数据库
      1.2.4 show tables;             #查看数据库中的表
  1.3 创建一个数据表
      1.3.1 );退出SQL模式
      1.3.2 create table  例如：create table userinfo( id int, name varchar(100), room varchar(100), idcard varchar(100), phone varchar(100), rent int, startdate date);
      1.3.3 增加数据
            insert into userinfo(id,name,room,idcard,phone,rent,startdate) values(1,"Aice",001,001002,1371234124,2000,"2020-1-1");
  1.4 导入一个现有的数据库
      1.4.1
  1.5 设置配置文件 保存后缀ini
  1.6 读取SQL配置文件
       import os,configparser
       cur_path = os.path.dirname(os.path.realpath(__file__)) #读取配置文件目录
       configPath = os.path.join(cur_path,'config.ini')
       conf = configparser.Configparser() #读取配置文件
       conf.read(configPath)
       host = conf.get("host")
       
    
2.python连接SQL
  2.1 import pymysql
      
      
3.conda install fake-useragent 报错PackagesNotFoundError
 解决办法：1.输入anaconda search -t conda fake-useragent  查看fake-useragent 的所有包的版本
         2.anaconda show qian_bi/fake-useragent 查看包的具体信息，后面有安装的链接提醒
     
4.使用fake-useragent 报错 FakeUserAgentError('Maximum amount of retries reached')
 解决办法：下载： https://fake-useragent.herokuapp.com/browsers/0.1.11 并另存为：fake_useragent.json
 
5.



