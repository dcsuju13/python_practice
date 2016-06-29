# -*- coding: utf-8 -*-
__author__ = 'Administrator'

'''
第 0004 题：
任一个英文的纯文本文件，统计其中的单词出现的个数
'''

word=[]
res={}
with open("test.txt","r") as f:
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

for key,value in res.items():
    print(key,value)

