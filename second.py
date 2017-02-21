# -*- coding=utf8 -*-
import requests
import os
from bs4 import BeautifulSoup

all_url = "http://tieba.baidu.com/p/2166231880"
start_html = requests.get(all_url)  # response<>
Soup = BeautifulSoup(start_html.text, 'lxml')


img_url = Soup.find('div', class_='d_post_content_main').find_all('img')

for url in img_url:
    os.chdir("D:/sbym3//")
    img_url = url['src']
    img = requests.get(img_url)  # get 到基本的 HTML

    f = open(img_url[-6:-4]+'.jpg', 'ab')  # 神tm蠢 缺少实战
    f.write(img.content)
    f.close()





















