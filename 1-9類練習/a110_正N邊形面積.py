# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:51:23 2020

@author: user
"""
import math
n=eval(input())
s=eval(input())
area=(n*s**2)/(4*math.tan(math.pi/n))
print("Area = {:.4f}".format(area))