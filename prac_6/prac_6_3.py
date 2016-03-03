#!/usr/bin/env python
#coding:utf-8

####################################################
# Copyrignt (py) YanceyZ. All rights reserved.
#
# Author: YanceyZ
# Mail: yanceyzhang2013@gmail.com
# Description:
#################################################### 

def count(word,character):
    count = 0
    for letter in word:
        if letter == character:
            count = count + 1
    print count 

count('banana','a')
count('elephant','e')
