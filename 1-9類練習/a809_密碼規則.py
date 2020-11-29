# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:58:20 2020

@author: user
"""

def ck1(t):
    if len(t)>=8:
        return True
    else:
        return False
def ck2(t):
    for i in range(len(t)):
        if "0"<=t[i]<="9" or "A"<=t[i]<="Z" or "a"<=t[i]<="z":
            continue
        else:
            return False
    return True
def ck3(t):
    for i in range(len(t)):
        if "A"<=t[i]<="Z":
            return True
        else:
            continue
    return False


passw=input()
t=list(passw)
ans=ck1(t) and ck2(t) and ck3(t)
if ans==True:
    print("Valid password")
else:
    print("Invalid password")


#xx.isalnum() 判斷由字母及數字組成 (中間有空白也不行)
#另一解法
psword,uppernum=input(),0
for i in range(len(psword)):
    if psword[i].isupper():
        uppernum=1
if len(psword)>=8 and psword.isalnum() and uppernum ==1:
    print("Valid password")
else:
    print("Invalid password")


