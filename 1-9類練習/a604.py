
N=[]
for i in range(10):
    N.append(eval(input()))
maxn=0
for i in range(10):
    if N.count(N[i])>maxn: #count出現次數
        maxn=N.count(N[i])
        n=N[i]

print(n)
print(maxn)
