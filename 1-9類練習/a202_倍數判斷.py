# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:11:02 2020

@author: user
"""
x=eval(input())
if x%3==0 and x%5==0:
    print("{:d} is a multiple of 3 and 5.".format(x))
elif x%5==0:
    print("{:d} is a multiple of 5.".format(x))
elif x%3==0:
    print("{:d} is a multiple of 3.".format(x))
else:
    print("{:d} is not a multiple of 3 or 5.".format(x))