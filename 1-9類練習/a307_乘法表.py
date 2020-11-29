
n=int(input())

for i in range(1,n+1): #直的
    for j in range(1,n+1): #橫的
        print("{} * {} = {:<4d}".format(j,i,(j*i)),end="")
    print()