N=[]
for i in range(10):
    N.append(eval(input()))

S=sum(N)-max(N)-min(N) #直接用減法篩選掉就好，不用到delect list裡面的東西
print(S)
print("{:.2f}".format(S/(len(N)-2)))