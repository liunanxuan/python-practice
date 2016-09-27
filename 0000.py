#-*- coding:utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
jpeg = './shuai.png'
#设定Imnage Font 和字体大小
font = ImageFont.truetype('simsun.ttc',30)
#打开需要渲染的图片
img = Image.open(jpeg, mode="r")
width,height = img.size
#将img obj传入ImageDraw Draw中
draw = ImageDraw.Draw(img)
#绘画字体
draw.text( (width*0.8,height*0.1), u'帅',(255,0,0),font=font)
#保存图片
img.save('paint_shuai.png','png')