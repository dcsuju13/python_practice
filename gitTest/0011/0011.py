# -*- coding: utf-8 -*-
__author__ = 'Administrator'
'''
第 0011 题：
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''


def check(word,list):
    if word in list:
        print("freedom...")
    else:
        print("human rights...")

def replaceWord(s,wordlist):
    s1=s.replace('.','')
    words=s1.split(" ")
    for word in words:
        if word in wordlist:
            s=s.replace(word,'*'*len(word))
    return s



def getWords(filename):
    wordlist=[]
    with open(filename,"r") as f:
        lines=f.readlines()
        for line in lines:
            line=line.replace('\n','')
            line=line.strip()
            wordlist.append(line)
    return wordlist



if __name__=="__main__":
    filename='word.txt'
    wordlist=getWords(filename)
    word=input('请输入单词：')
    while word!='exit':
        #check(word,wordlist)
        s=replaceWord(word,wordlist)
        print(s)
        word=input('请输入单词：')
    print("exit...")