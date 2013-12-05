#!/usr/bin/env python
#coding=utf-8
import math

a = open('num.txt','r')
li = a.read().split()
#li=a.readlines()
num = [int(i) for i in li]
a.close()

def test(num):
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            return True
    return False

for i in num:
    if test(i) == True:
        print (i)
