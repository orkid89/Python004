学习笔记
1.requests 使用
 1.1 get 
   1.1.1不带参数的get   requests.get('http://news.baidu.com/') 返回数据类型是<class 'requests.models.Response'>,请求成功返回200。
   1.1.2带参数的get    requests.get('http://news.baidu.com/',hesders=header,params={'key':'value'}) 返回数据类型是<class 'requests.models.Response'>
   例如：
    import requests
    url = "http://news.baidu.com/"
    newspage = requests.get(url,headers = header,params = {'class':'clearfix'}
    
 1.2 requests的其他使用方法
   1.2.1 requests.post --Get是从服务器上获取数据，Post是向服务器传送数据
   1.2.2 requests.put  --更新网页使用的
    
  1.3 requests的请求内容 
    newspage.encoding                       #获取当前的编码
    newspage.encoding = 'utf-8'             #设置编码
    newspage.text                           #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
    newspage.content                        #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
    newspage.headers                        #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
    newspage.status_code                     #响应状态码
    newspage.raw                             #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()   
    newspage.ok                              # 查看r.ok的布尔值便可以知道是否登陆成功
     #*特殊方法*#
    newspage.json()                         #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
    newspage.raise_for_status()             #失败请求(非200响应)抛出异常
    
   1.4 requests设置超时
    requests.get('url',timeout=1)  

2.正则表达式的基础使用

  2.1 re.search       扫描整个字符串找到匹配样式的第一个位置，并返回一个匹配对像
      re.match        如果string开始的0或者多个字符匹配到正则表达式，就返回一个相对应的匹配对像
      re.fuallmatch   如果整个string匹配到正则表达式，就返回一个相对应的匹配对像
      re.spilt        用pattern分开string
      re.findall      对string返回一个不重复的pattern的匹配列表
      re.finditer     pattern在string里所有非重复匹配，返回一个迭代器iterator保存了对象，查找所有的副词及其位置
      
text = '''<a id="tab-login" class="tab-login" href="javascript:void(0);" onclick="return false" mon="m=53&a=3"></a>'''
  2.2 匹配案例
      re.findall(r'tab',text)               -- ['tab', 'tab']
      re.findall(r'(tab)',text)             -- ['tab', 'tab']
      re.findall(r'[tab]',text)             -- ['a', 't', 'a', 'b', 'a', 't', 'a', 'b', 'a', 'a', 't', 't', 'a', 'a', 'a']
      re.findall(r'id=(.*) class',text)     --['"tab-login"']
      re.findall(r'id="(.*?)"',text)        --['tab-login']
      re.findall('id="(.*)-login"',text)    --['tab-login" class="tab']
      re.match(r"^[a2-9tjqk]{5}$","akt5k")  --akt5k #^匹配字符串的开头,$匹配字符串尾或者在字符串尾的换行符的前一个字符,{5}对其之前的正则式指定匹配 5 个重复,[a2-9tjqk]表示匹配字母a,t,j,q,k和数字2-9中的任意一个字符。
      re.match(r"\W(.)\1\W", " ff ")        --'  ff  ' #\W匹配空格，(.)匹配任意一个字符，\1表示特殊序列
      
      
    2.2.1 ?<=
      re.search(r'(?<=abc)def','abcdefghik')  -- ?<=只能匹配出’abc'后面的'def' 
      re.search(r'(?<=tab)-log',text)   --(-log)
      re.search(r'(?<=tab).\w+',text)  --(.login)
      re.search(r'(?<=tab-)\w+',text)  --(login)
      
    2.2.2 (?p<name>...)
      re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")   -- Malcolm  Reynolds
      
      
3.BeautifulSoup

      
        
