# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:11:22 2020

@author: user
"""

f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read902.txt","r")
s=f.read()
list1=s.split(" ")
print(list1)
sum=0
for i in list1: 
    sum+=eval(i)
print(sum)

#len(list1)是用在算 列的數量
#這題是要加總裡面的內容，
#所以直接用list1進去
#用list1進去搭配 就是直接使用i 
