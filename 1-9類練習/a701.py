list=[]
while 1:
    n=eval(input())
    if n==-9999:
        break
    else:
        list.append(n)
print(tuple(list))
print("Length:",len(list))
print("Max:",max(list))
print("Min:",min(list))
print("Sum:",sum(list))