# -*- coding: utf-8 -*-
__author__ = 'Administrator'
'''
第 0013 题：
用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
'''

import urllib.request
import urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup
import re

def login():
    #主页地址
    urlhome="http://www.baidu.com"
    #通过f12查找token得到的中间预登陆的跳转网页（不知道为什么和网上帖子监视的url不一样）
    urltoken="https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt=1466425058227&class=login&gid=18DA095-8844-4A57-86E3-37F56687617D&logintype=dialogLogin&callback=bd__cbs__fptuhz"
    #登录post地址
    urllogin="https://passport.baidu.com/v2/api/?login"

    #一般获取网页内容直接urlopen即可，但是有些网站需要登录，就需要cookie
    cj=http.cookiejar.CookieJar()#声明cookiejar对象实例来保存cookie
    #创建cookie处理器，并用处理器来构建opener
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    #为了伪装成浏览器进行访问，加入头部
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko')]
    #同urlopen
    resp=opener.open("http://www.baidu.com")#为了获取BAIDUID
    print(resp.read())

    resp=opener.open(urltoken)#获取Token
    d=resp.read()
    matchval=re.search('"token" : "(\d+)"',resp.read().decode('utf-8'))#正则表达式查找token
    if matchval:
        tokenval=matchval.group('tokenval')
        print("step2:"+tokenval)

    data={
        'username':"SUJU幸福",
        'password':"sjonly13..",
        'token':matchval

    }
    postdata=urllib.parse.urlencode(data).encode('utf-8')#编码post数据
    op=opener.open(urllogin,data=postdata)#提交表单登录
    html=op.read()
    print(html)


def loadpic(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html,"html.parser",from_encoding='utf-8')
    data=soup.find_all('img',class_="BDE_Image")
    nextpage=soup.find('a',text="下一页")['href']
    for img in data:
        response=urllib.request.urlopen(img['src'])
        html=response.read()
        name=img['src'].split('/')[-1]
        with open(name,"wb") as f:
            f.write(html)
    #nextpage
    if nextpage:
        nextpage="http://tieba.baidu.com"+nextpage
        loadpic(nextpage)



if __name__=="__main__":
    login()
    '''
    url="http://tieba.baidu.com/home/main?id=af8c53554a55d0d2b8a37907&fr=userbar"#登录贴吧个人主页验证
    response=urllib.request.urlopen(url)
    html=response.read()
    print(html.decode('GBK'))
    '''
    url="http://tieba.baidu.com/p/4379542413"
    loadpic(url)



