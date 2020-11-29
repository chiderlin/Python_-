list1=[]
while 1 :
    w=input()
    if w=="end":
        break
    else:
        list1.append(w)
tu=tuple(list1)
print(tu)
print(tu[0:3])
print(tu[-3:]) #倒數三個
