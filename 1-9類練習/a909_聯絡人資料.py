# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:16:24 2020

@author: user
"""
fw=open("data.dat","w",encoding="UTF-8")
for i in range(5):
    fw.write(input()+"\n")
fw.close()
print("The content of \"data.dat\":")
f=open("data.dat","r",encoding="utf-8")
for i in f:
    print(i)
f.close()