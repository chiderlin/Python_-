# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:54:53 2020

@author: user
"""


a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print(a+b+c)
else:
    print("Invalid")