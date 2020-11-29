# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:01:46 2020

@author: user
"""
def compute(x,y):
    for i in range(1,y+1):
        if x%i==0 and y%i==0:
            sum=i
    return sum

x,y=eval(input())
print(compute(x,y))