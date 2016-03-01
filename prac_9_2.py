#! /usr/bin/env python
# -*- coding: utf-8 -*-

#按照接收的星期时间对邮件进行分类。

#首先,找出以From开头的文本行,
#然后,取出符合条件的每一行中的第三个单词,使用一个计数器统计一周中每一天邮件被接收的次数。
#在程序的末尾,输出字典的内容(不要求次序)。

try:
	filename = raw_input('Enter a file name:')
	ffile = open(filename)
except:
	print "Please input a right file name!"
	exit()
counts = dict()
for line in ffile:
	if line.startswith('From '):
		#print line 
		words = line.split() #默认用空格将一行的字符分隔开
		print words[2]
		if words[2] not in counts:#这句话注意！！！！
			counts[words[2]] = 1
		else:
			counts[words[2]] += 1
print counts