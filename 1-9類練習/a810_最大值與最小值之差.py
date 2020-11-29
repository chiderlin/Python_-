
num=eval(input())
for i in range(num):
    str=input()
    list1=str.split(" ")
    
    list2=[]
    #print(list1)
    for j in range(len(list1)):
        list2.append(eval(list1[j])) #轉換成數字
    #print(list2)
    print("{:.2f}".format(max(list2)-min(list2)))





