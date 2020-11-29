
set1,set2,set3=set(),set(),set() #set 這邊卻是用() 
for i in range(3):
    print("Input to set{}:".format(i+1))
    if i==0:
        for j in range(5):
            set1.add(eval(input())) #分兩行打會有錯誤 所以要塞到一行裡..
    elif i==1:
        for j in range(3):
            set2.add(eval(input()))
    elif i==2:
        for j in range(9):
            set3.add(eval(input()))

# print(set1)
# print(set2)
#print(set3) 是{}沒錯
print("set2 is subset of set1:",set2<=set1) #set2是否為set1的子集合（subset）？
print("set3 is superset of set1:",set3>=set1) #set3是否為set1的超集合（superset）
