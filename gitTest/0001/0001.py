# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from random import choice

'''
第 0001 题：
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''


def CreateNumber(res,char):
    s=''
    for i in range(6):
        s+=choice(char)
    if s not in res:
        res.add(s)


if __name__=="__main__":
    res=set()
    char=[]
    for i in range(26):
        char.append(chr(ord('a')+i))
        char.append(chr(ord('A')+i))
    while len(res)<200:
        CreateNumber(res,char)
    with open('data.txt','w') as f:
        for item in res:
            f.writelines(item+'\n')


