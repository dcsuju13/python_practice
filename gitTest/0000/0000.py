# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from PIL import Image,ImageColor,ImageDraw,ImageFont

image=Image.open('n16.jpg')

font=ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',40)
draw=ImageDraw.Draw(image)
draw.text((550,0),'99+',font=font,fill="#ffffff")

image.save('new.jpg','jpeg')

