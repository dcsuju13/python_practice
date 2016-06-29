# -*- coding: utf-8 -*-
__author__ = 'Administrator'
'''
第 0010 题：
使用 Python 生成类似于下图中的字母验证码图片
'''
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random


def rcolor(op):
    if op==1:
        r=random.randint(100,255)
        g=random.randint(100,255)
        b=random.randint(100,255)
    else:
        r=random.randint(30,90)
        g=random.randint(30,90)
        b=random.randint(30,90)

    res=(r,g,b)
    return res

def rfont():
    return chr(random.randint(65,90))


def main():
    width=240
    height=60
    im=Image.new('RGB',(width,height),(255,255,255))
    font=ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',40)
    draw=ImageDraw.Draw(im)
    for i in range(width):
        for j in range(height):
            draw.point((i,j),fill=rcolor(1))

    for i in range(4):
        draw.text((i*60,0),rfont(),font=font,fill=rcolor(2))
    im.filter(ImageFilter.BLUR)
    im.save("check.jpg")

if __name__=="__main__":
    main()
