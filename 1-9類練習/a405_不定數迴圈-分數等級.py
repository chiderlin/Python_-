
while 1:
    n=int(input())
    if n==-9999:
        break
    elif 90<=n<=100:
        s="A"
    elif 80<=n<=89:
        s="B"
    elif 70<=n<=79:
        s="C"
    elif 60<=n<=69:
        s="D"
    elif n<=59:
        s="E"
    print(s)