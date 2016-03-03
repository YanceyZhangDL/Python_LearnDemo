#!/usr/bin/env python
#coding:utf-8

from PIL import Image 
from pylab import *

#读取图像到数组中
#im = array(Image.open('/home/zyq/pic/Z2.jpg'))
im = array(Image.open('Z2.jpg'))

imshow(im)

x=[100,100,400,400]
y=[200,500,200,500]

plot(x,y,'r*')

plot(x[:2],y[:2])

title('Plotting:"my little bone mua"')

show()
