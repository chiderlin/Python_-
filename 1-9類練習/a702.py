
word=["Create tuple1:","Creat tuple2:"]
list1=[]
for i in word:
    print(i)
    while 1:
        n=eval(input())
        if n==-9999:
            break
        else:
            list1.append(n)
#list2=list1.sort(reverse=False) 這裡不能用 WHY..?

#sort 与 sorted 区别：
#sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#list 的 sort 方法返回的是对已经存在的列表进行操作，
# 无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
print("Combined tuple before sorting:",tuple(list1))
print("Combined list after sorting:",sorted(list1))