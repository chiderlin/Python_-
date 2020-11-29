# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:18:45 2020

@author: user
"""

def compute(str,chr):
    return str.count(chr)

    
str=input()
chr=input()
print("{} occurs {} time(s)".format(chr,compute(str,chr)))

#def
#str.count(chr)
#compute(str,chr)