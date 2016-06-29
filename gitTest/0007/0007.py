# -*- coding: utf-8 -*-
__author__ = 'Administrator'
'''
第 0007 题：
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
'''
import os


def count(filename):
    a=0
    b=0
    c=0
    with open(filename,"r",encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            if not line.strip():
                c=c+1
            elif line.startswith("#") or line.startswith("'''") or line.endswith("'''"):
                b=b+1
            else:
                a=a+1
    return a,b,c


if __name__=="__main__":
    filedir=r"E:\pythonPra\spider"
    files=os.listdir(filedir)
    countA=0
    countB=0
    countC=0
    for file in files:
        if file.endswith(".py"):
            file=filedir+r"/"+file
            a,b,c=count(file)
            countA=a+countA
            countB=b+countB
            countC=c+countC

    print(countA)
    print(countB)
    print(countC)