#set 用什麼加入 ? => add
#或者用list轉set
SET=set()
while 1:
    n=eval(input())
    if n==-9999:
        break
    else:
        SET.add(n)
print(SET)
print("Length:",len(SET))
print("Max:",max(SET))
print("Min:",min(SET))
print("Sum:",sum(SET))

#集合特性 : 顯示的key不重複