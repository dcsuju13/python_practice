# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
from PIL import Image
'''
第 0005 题：
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
'''
filedir=r"./pic"
files=os.listdir(filedir)

path=os.getcwd()
count=0
for file in files:
    count=count+1
    if file.endswith(".jpg"):
        file=filedir+'/'+file
        im=Image.open(file)
        x,y=im.size
        cx=float(x)/1136
        cy=float(y)/640
        change=cx if cx>cy else cy
        im=im.resize((int(x/change),int(y/change)))
        im.save("{0}.jpg".format(count))