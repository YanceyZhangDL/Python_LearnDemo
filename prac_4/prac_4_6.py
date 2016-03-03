#!/usr/bin/env python
#coding:utf-8

####################################################
# Copyrignt (py) YanceyZ. All rights reserved.
#
# Author: YanceyZ
# Mail: yanceyzhang2013@gmail.com
# Description:
#################################################### 

def computepay():
    hours = float(raw_input("Enter Hours:"))
    Rate  = float(raw_input("Enter Rate:"))
    pay = hours * Rate
    print "Pay:",pay

computepay()
