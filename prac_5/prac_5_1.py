#!/usr/bin/env python
#coding:utf-8

####################################################
# Copyrignt (py) YanceyZ. All rights reserved.
#
# Author: YanceyZ
# Mail: yanceyzhang2013@gmail.com
# Description:
#################################################### 
while True:
    try:
        summ = 0
        iterr = 0
        num = raw_input("Enter a number:")
        while num != "done":
             num = float(num)
             summ += num
             iterr += 1
             num = raw_input("Enter a number:")
        print "总和：",summ,"个数:",iterr,"平均值:",summ/iterr        
        break
    except:
        print "Error：请输入数字"
'''
summ = 0
iterr = 0
num = raw_input("Enter a number:")
while num != "done":  #这里不能用is not，is是看两个标识符是不是引自同一对象
    num = float(num)
    summ += num
    iterr += 1
    num = raw_input("Enter a number:")
print "总和：",summ,"个数:",iterr,"平均值:",summ/iterr
'''
