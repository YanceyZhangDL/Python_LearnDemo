#!/usr/bin/env python
#coding:utf-8

####################################################
# Copyrignt (py) YanceyZ. All rights reserved.
#
# Author: YanceyZ
# Mail: yanceyzhang2013@gmail.com
# Description:
#################################################### 

#import sys
import traceback
try:
	score = raw_input("Enter Score:")
	score = float(score)#不加类型转换还不行了。。
	if score > 1.0 or score < 0.0:
		print "Bad score.\nPlease input from 0.0 to 1.0"
	elif score <= 1 and score >= 0.9:
		print "A"
	elif score < 0.9 and score >=0.8:
		print "B"		
	elif score < 0.8 and score >=0.7:
		print "C"
	elif score < 0.7 and score >=0.6:
		print "D"
	elif score >= 0 and score <0.6:
		print "F"
except:
	print "Please input a number!"
	traceback.print_exc()
