sum=0
for i in range(5):
    n=input()
    if n=="J":
        s=11
    elif n=="Q":
        s=12
    elif n=="K":
        s=13
    elif n=="A":
        s=1
    else:
        s=eval(n)
    sum+=s
print(sum)