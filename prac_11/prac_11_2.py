#! /usr/bin/env python
# -*- coding: utf-8 -*-

#使用正则表达式的findall()函数抽取每一行中的数字
#计算并输出数字的平均值

import re
summ = 0
ave = 0
count = 0
ffile = raw_input('Enter file:')
hand = open(ffile)
for line in hand:
	line.rstrip()
	t = re.findall('[0-9][0-9]*[0-9.][0-9]*[0-9]',line)
	#t = re.findall(': ([0-9][0-9.]*)',line)
	if len(t)>0:
		for i in t:
			summ += float(i)
			count += 1
ave = summ / count
print ave
		
