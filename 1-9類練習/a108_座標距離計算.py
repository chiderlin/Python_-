# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:34:50 2020

@author: user
"""


x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
d=((x1-x2)**2+(y1-y2)**2)**0.5
print("( {} , {} )".format(x1,y1))
print("( {} , {} )".format(x2,y2))
print("Distance = {}".format(d))