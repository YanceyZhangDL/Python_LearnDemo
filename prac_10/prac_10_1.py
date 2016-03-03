#! /usr/bin/env python
# -*- coding: utf-8 -*-

#使用字典来创建一个直方图,统计每个邮箱发出的邮件数量,然后输出字典。
#读取与解析出以“From”开头的行,取出符合条件的行中的邮箱。
#使用字典统计出每个人的邮件数。
#当所有的数据读取完毕,从字典中创建一个元组(count,email)列表,然后对列表进行反向排序,打印出提交最多的用户。

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

lst = list()
for email,count in counts.items():
 	lst.append((count,email))
lst.sort(reverse=True)
key,val=lst[0]
print val,key