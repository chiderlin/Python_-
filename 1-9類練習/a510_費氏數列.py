# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:19:25 2020

@author: user
"""

def compute(a):
    n1=0
    n2=1
    s=str(n1)+" "+str(n2)
    for i in range(3,a+1):
        n3=n2+n1
        s+=" "+str(n3)
        n1=n2
        n2=n3
    return s

num=int(input())
print(compute(num))