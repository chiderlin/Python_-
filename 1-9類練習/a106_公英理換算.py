# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:41:01 2020

@author: user
"""
x=eval(input())
y=eval(input())
z=eval(input())

speed=z/1.6/(x/60+y/60/60)

print("Speed = {:.1f}".format(speed))