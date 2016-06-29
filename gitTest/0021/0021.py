# -*- coding: utf-8 -*-
__author__ = 'Administrator'
'''
第 0021 题：
通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

•阅读资料 用户密码的存储与 Python 示例


•阅读资料 Hashing Strings with Python


•阅读资料 Python's safest method to store and retrieve passwords from a database


'''
import os
from hashlib import sha256
from hmac import HMAC


def encrypt_password(password,salt=None):
    if salt is None:
        salt=os.urandom(8)#生成8字节随机salt
    assert 8==len(salt)
    #assert isinstance(salt, str)
    #if isinstance(password, unicode):
    password.encode('utf-8')
    assert isinstance(password, str)
    result=password

    for i in range(10):
        result=HMAC(b'result',salt,sha256).digest()
    return salt+result

def check(hashed,password):
    return hashed==encrypt_password(password,hashed[0:8])



if __name__=="__main__":
    password=input('请输入密码：')
    result=encrypt_password(password)
    print("result={0}".format(result))
    print(check(result,password))