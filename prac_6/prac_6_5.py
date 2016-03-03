#!/usr/bin/env python
#coding:utf-8

####################################################
# Copyrignt (py) YanceyZ. All rights reserved.
#
# Author: YanceyZ
# Mail: yanceyzhang2013@gmail.com
# Description:
#################################################### 

strr = 'X-DSPAM-Confidence:  0.8475'

num = strr.find(':')
#float_num = float((strr[num:]).strip())
float_num = strr[num+1:]
print "The original string:",float_num
#print "The converted string:",float_num.strip(' ')
float_num = float(float_num.strip())
print "The float number is %g " % float_num

