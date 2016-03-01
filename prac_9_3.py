#! /usr/bin/env python
# -*- coding: utf-8 -*-

#使用字典来创建一个直方图,统计每个邮箱发出的邮件数量,然后输出字典。

try:
	filename = raw_input('Enter a file name:')
	ffile = open(filename)
except:
	print "Please input a right file name!"
	exit()
counts = dict()
for line in ffile:
	if line.startswith('From:'):
		#print line 
		words = line.split() #默认用空格将一行的字符分隔开
		print words[1]
		if words[1] not in counts:#这句话注意！！！！
			counts[words[1]] = 1
		else:
			counts[words[1]] += 1
print counts