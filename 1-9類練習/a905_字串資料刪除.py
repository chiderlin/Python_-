# -*- coding:utf-8 -*-

file=input()
word=input()

print("=== Before the deletion")
f=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read905.txt","r",encoding="UTF-8")
s=f.read()
print(s)

print("=== After the deletion")
s2=s.replace(word,"")
print(s2)
fw=open(r"C:\Users\user\Desktop\大數據班資料 eclipse\第9類試題txt檔\read905.txt","w",encoding="UTF-8")
fw.write(s2)

