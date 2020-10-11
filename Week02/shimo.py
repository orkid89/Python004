import requests
import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
import pytesseract


try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/')
    time.sleep(2)
    
    html = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')
    html.click()
    
    browser.find_element_by_xpath('//*[@id="root"]').send_keys('18511575501')
    browser.find_element_by_id('password').send_keys('zx891225')
    time.sleep(2)
    browser.find_element_by_xpath('//a[contains(@class,"sm-button submit sc-1n784rm-0 bcuuIb")]').click()
    
    #下载图片
    
    #获取小图片
    little_img = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[6]/div/div/div[1]/div[1]/div[2]')\
    .get_attribute("src")
    #获取大图片
    big_img = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]/img').\
    get_attribute("src")
    
    with open("code1.jpg", "wb") as f:
        
        f.write(base64.b64decode(little_img.split(',')[1]))
    
    with open("code2.jpg", "wb") as f:
        f.write(base64.b64decode(big_img.split(',')[1]))
        
    #灰度图片
    im1 = Image.open('code1.jpg')
    im2 = Image.open('code2.jpg')
    gray1 = im1.convert('L')
    gray.save('1_gray.jpg')
    im1.close()
    gray2 = im2.convert('L')
    gray.save('2_gray.jpg')
    im2.close()
    
    #图片二值化
    threshold=130
    table = []

    for i in range(256):
        if i < threshold:
            table.append(1)
        else:
            table.append(0)
    out = gray1.point(table,'1')  
    out.save('1_gray1.jpg')
    out = gray2.point(table,'1')  
    out.save('2_gray2.jpg')
    
    #识别小图上的文字
    try:
        op = {'language_type': 'CHN_ENG', 'detect_direction': 'true'}
        res = self.WCLIENT.basicAccurate(
        self.getFile('1_gray1.jpeg'), options=op)
        words = ''
        for item in res['words_result']:
            if item['words'].endswith('。'):
                words = words + item['words'] + '\r\n'
            else:
                 words = words + item['words']
        return words
    except:
        eturn 'error'
        
    # 识别下面大图中文字的坐标
    
    try:
        op = {'language_type': 'CHN_ENG', 'recognize_granularity': 'small'}
        res = self.WCLIENT.accurate(self.getFile('2_gray2.jpeg'), options=op)
        # 所有文字的位置信息
        allPosInfo = []
        # 需要的文字的位置信息
        needPosInfo = []
        for item in res['words_result']:
             allPosInfo.extend(item['chars'])
        # 筛选出需要的文字的位置信息
        for word in words:
            for item in allPosInfo:
                if word == item['char']:
                    needPosInfo.append(item)
        return needPosInfo
    except Exception as e:
            print(e)

    #点击文字
    needPosInfo.click()
    time.sleep(2)
    
    
    
    cookies = browser.get_cookies()

    time.sleep(3)
except Exception as e:
    print(e)
    
finally:
    browser.close()