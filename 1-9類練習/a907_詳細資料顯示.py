# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:07:00 2020

@author: user
"""

f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read907.txt","r",encoding="utf-8")
line=0
word=0
char=0
for i in f:
    line+=1
    split=i.split(" ")
    word+=len(split)
    for i in range(len(split)):
        char+=len(split[i])
print(line,"line(s)")
print(word,"word(s)")
print(char,"charater(s)")

f.close()

