# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:49:34 2020

@author: user
"""

a = int(input())
b = int(input())
count = 0
total = 0
for i in range(a,b+1):
    if i%4==0 or i%9==0:
        count+=1
        total+=i
        print("{:<4d}".format(i),end="")
    
        if count%10==0:
            print()
print()
print(count)
print(total)
