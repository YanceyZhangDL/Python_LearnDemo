#! /usr/bin/env python
# -*- coding: utf-8 -*-

#模拟Unix中grep命令的操作。
#要求用户输入一个正则表达式
#统计出正则表达式匹配的文本行数

import re
count = 0
ffile = open('mbox.txt')
RegularExpr = raw_input('Enter a regular expression:')
for line in ffile:
	line = line.rstrip()
	#这个时候search的参数项不能加''
	if re.search(RegularExpr,line):
		count += 1
	#x = re.search('RegularExpr',line)
	#if len(x) > 0:
		#count += 1
print 'mbox.txt had %d lines that matched %s' % (count,RegularExpr)
