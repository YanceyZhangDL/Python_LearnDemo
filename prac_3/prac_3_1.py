#!/usr/bin/env python
#coding:utf-8

####################################################
# Copyrignt (py) YanceyZ. All rights reserved.
#
# Author: YanceyZ
# Mail: yanceyzhang2013@gmail.com
# Description:
#################################################### 
try:
	hours=raw_input("Enter Hours:")
	rate =raw_input("Enter Rate:")
	if hours>40:
		pay=40.0*float(rate)+(float(hours)-40.0)*float(rate)*1.5
	else:
		pay=hours * rate
	print "Pay:",pay
except:
	print "Error,Pleasr enter numeric input"


