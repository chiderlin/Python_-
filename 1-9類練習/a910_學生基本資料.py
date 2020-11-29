# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:42:48 2020

@author: user
"""
f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read910.dat","r",encoding="UTF-8")
s=f.readlines()
#print(s)
f=0
m=0
for i in range(len(s)):
    print(s[i])

s[i].split("\n") #先行切  #在for迴圈裡面做才有用
for i in range(1,len(s)):
    list1=s[i].split(" ") #直切
    #print(int(list1[2]))
    if int(list1[2])==0:
        f+=1
    else:
        m+=1
print("Number of males: {}".format(m))
print("Number of females: {}".format(f))