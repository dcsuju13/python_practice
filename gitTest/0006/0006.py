# -*- coding: utf-8 -*-
__author__ = 'Administrator'

'''
第 0006 题：
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
import os

def countWords(filename):
    word=[]
    res={}
    with open(filename,"r") as f:
        content=f.read()
        word=content.split(' ')
        for it in word:
            if not it.strip():
                continue
            it=it.replace('"','')
            it=it.replace("'",'')
            it=it.replace(".",'')
            it=it.replace("?",'')
            it=it.lower()
            if it in res.keys():
                res[it]=res[it]+1
            else:
                res[it]=1
    maxv=0;
    for key,value in res.items():
        if value>maxv:
            maxv=value
            reskey=key
    return reskey

if __name__=="__main__":
    files=os.listdir()
    for file in files:
        if file.endswith(".txt"):
            keyword=countWords(file)
            print(keyword)




