# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:42:19 2020

@author: user
"""


m=eval(input())
if 8000<=m<18000:
    print("{:.1f}".format(m*0.95))
elif 18000<=m<28000:
    print("{:.1f}".format(m*0.9))
elif 28000<=m<38000:
    print("{:.1f}".format(m*0.8))
elif m>=38000:
    print("{:.1f}".format(m*0.7))