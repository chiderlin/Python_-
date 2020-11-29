# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:27:37 2020

@author: user
"""

f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read903.txt","a",encoding="UTF-8")
for i in range(5):
    f.write("\n"+input())

print("Append completed!")
print("Content of \"data.txt\":")
f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read903.txt","r",encoding="UTF-8")
s=f.read()
print(s)