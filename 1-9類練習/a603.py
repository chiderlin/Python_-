N=[]
for i in range(10):
    N.append(int(input()))

N.sort(reverse=True) #sort reverse排序 True大到小 False小到大
print(N)
print(N[0],N[1],N[2])
