#! /usr/bin/env python
# -*- coding: utf-8 -*-

#读取words.txt中单词
#将它们作为键存储在字典中(不需要关心键对应的值)
#使用in操作符快速判断某一字符串是否存在于字典中
print "I'm Back!"
fhand = open('words.txt')
#首先必须先定义一个空字典
dict_eng = dict()
for line in fhand:
	dict_eng[line.strip()] = ' '																
print dict_eng
word = raw_input("Please input a word:")
if word in dict_eng:
	print 'True'
else:
	print 'False'