# -*- coding: utf-8 -*-
__author__ = 'Administrator'
'''
第 0008 题：
一个HTML文件，找出里面的正文。
第 0009 题：
一个HTML文件，找出里面的链接。
'''
import urllib.request
from bs4 import BeautifulSoup

def downloader(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    return html


def FindHref(html):
    soup=BeautifulSoup(html,"html.parser",from_encoding='utf-8')
    data=soup.find_all('a')
    print("href:")
    for item in data:
        print(item['href'],item.get_text())


def FindBody(html):
    soup=BeautifulSoup(html,"html.parser",from_encoding="gbk")
    data=soup.find_all('div', class_="d_post_content j_d_post_content  clearfix")
    print("body:")
    for item in data:
        print(item.get_text())


if __name__=="__main__":
    url="http://tieba.baidu.com/p/4033241072"
    html=downloader(url)
    FindBody(html)
    FindHref(html)