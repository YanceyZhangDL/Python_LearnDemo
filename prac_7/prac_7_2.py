#!/usr/bin/env python
#coding:utf-8

####################################################
# Copyrignt (py) YanceyZ. All rights reserved.
#
# Author: YanceyZ
# Mail: yanceyzhang2013@gmail.com
# Description:
#################################################### 

name = raw_input('Enter file name:')
try:
    fhand = open(name)
except:
    print "I can't find it.\nAre you kidding me?!!!"
    print "Hah,give you an easter egg for your sickness!"
    exit()
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        iter=line.find(':')
        print 'float number:',line[iter+1:]
        count = count + 1
print 'count:',count
