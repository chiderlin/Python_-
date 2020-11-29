
t=int(input())
for j in range(t):
    sum=0
    n=input()
    for i in range(1,len(n)+1):
        sum=sum+int(n[-i])
    print("Sum of all digits of {} is {}".format(n,sum))