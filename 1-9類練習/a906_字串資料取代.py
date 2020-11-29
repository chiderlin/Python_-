# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:45:49 2020

@author: user
"""
file=input()
s1=input()
s2=input()

print("=== Before the replacement")
f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read906.txt","r",encoding="utf-8")
s=f.read()
print(s)
print("=== After the replacment")
s3=s.replace(s1,s2)
print(s3)
fw=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read906.txt","w",encoding="utf-8")
fw.write(s3)