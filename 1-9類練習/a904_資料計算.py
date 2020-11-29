# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 10:48:39 2020

@author: user
"""

f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read904.txt","r",encoding="UTF-8")
s=f.readlines()
#print(s)
n=[]
h=[]
w=[]
for i in range(len(s)):
    print(s[i])
    list1=s[i].split(" ")
    n.append(list1[0])
    h.append(int(list1[1]))
    w.append(int(list1[2]))

print("Average height: {:.2f}".format(sum(h)/len(h)))
print("Average height: {:.2f}".format(sum(w)/len(w)))
print("The tallest is {} with {:.2f}cm".format(n[h.index(max(h))],max(h)))
print("The heaviest is {} with {:.2f}kg".format(n[w.index(max(w))],max(w)))
