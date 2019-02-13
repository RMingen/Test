from urllib import request
import time
import re
from bs4 import BeautifulSoup


# 运行不能正常循环
def get_movie_html():
    for page in range(10):
        value = page*25
        url = 'https://movie.douban.com/top250?start=%s&filter=' % str(value)

        url = request.urlopen(url)
        time.sleep(3)
        html = url.read()
        html1 = str(html, encoding='utf-8')
        # 获取每个电影的链接
        rer = r'<div class="hd">.*?<a href="(.*?)" class="">'
        urls = re.findall(rer, html1, re.S)
        return urls


def get_movies_comments(urls):
    url1 = [i + 'comments?status=P'for i in urls]
    for url2 in url1:
        url3 = request.urlopen(url2)
        time.sleep(3)
        html2 = url3.read()
        movie = str(html2, encoding='utf-8')
        return movie


def get_comment(movie):
    soup = BeautifulSoup(movie, 'lxml')
    comments = soup.find_all(class_='comment-item')
    rer = r'<a class="".*?>(.*?)</a>.*?<span class="comment-time".*?>(.*?)</span>.*?<span class="short">(.*?)</span>'
    x = 1
    for item in comments[:10]:  # 对comments列表进行切片处理，只取前十热评
        comment1 = re.findall(rer, str(item), re.S)
        for comment in comment1:
            print(x, comment[0], str(comment[1]).replace('\n', '').replace(' ', ''), comment[2])
            x += 1


if __name__ == '__main__':
    urls1 = get_movie_html()
    movies = get_movies_comments(urls1)
    get_comment(movies)
