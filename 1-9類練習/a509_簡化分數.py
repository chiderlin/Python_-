# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:17:32 2020

@author: user
"""
def compute(p,q):
    gcd=1
    k=2
    if p>0 and q>0:
        while p>=k and q>=k:
            if p%k==0 and q%k==0:
                gcd=k
            k+=1
        return gcd
    
x,y = eval(input())
m,n = eval(input())
p = x*n+m*y
q = y*n
g=compute(p,q)
print("{:d}/{:d} + {:d}/{:d} = {:d}/{:d}".format(x,y,m,n,p//g,q//g))
