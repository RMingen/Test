import re
from selenium import webdriver
from bs4 import BeautifulSoup
# import pymongo

browser = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe')
url = 'https://movie.douban.com/subject/1292052/'  #模拟进入豆瓣top250单个电影页面 eg：'肖申克的救赎'
browser.get(url)
url2 = browser.find_element_by_id('comments-section')
url2.find_elements_by_class_name('pl')[0].click()  #点击'全部 259403 条'进入全部热评页面

html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
comments = soup.find_all(class_='comment-item')
rer = r'<a class="".*?>(.*?)</a>.*?<span class="comment-time".*?>(.*?)</span>.*?<span class="short">(.*?)</span>'
for item in comments[:10]:  #对comments列表进行切片处理，只取前十热评
    comment1 = re.findall(rer, str(item), re.S)
    for comment in comment1:
        # print(comment[0], str(comment[1]).replace('\n', '').replace(' ', ''), comment[2])
        name = comment[0]
        time = str(comment[1]).replace('\n', '').replace(' ', '')
        word = comment[2]

        # 存入数据库
        # client = pymongo.MongoClient(host='localhost', port=27017)
        # db = client.text
        # collection = db.movies
        # movie = {'name': name, 'time': time, 'word': word}
        # result = collection.insert_one(movie)
        # print(result)
