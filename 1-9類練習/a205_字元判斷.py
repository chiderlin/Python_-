# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:17:51 2020

@author: user
"""


n=input()
if n.isalpha():
    print("{} is an alphabet.".format(n))
elif n.isdigit():
    print("{} is a number.".format(n))
else:
    print("{} is a symbol.".format(n))