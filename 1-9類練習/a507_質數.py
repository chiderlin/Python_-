# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:13:14 2020

@author: user
"""

def compute(n):
    if n<=1:
        return "Not Prime"
    for i in range(2,n):
        if n%i==0:
            return "Not Prime"
        else:
            return "Prime"
    
x=int(input())
print(compute(x))