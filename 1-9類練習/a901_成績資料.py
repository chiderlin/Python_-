# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:58:30 2020

@author: user
"""

fw=open("read.txt","w",encoding="UTF-8")
for i in range(5):
    fw.write(input())
    fw.write("\n")

fw.close()
