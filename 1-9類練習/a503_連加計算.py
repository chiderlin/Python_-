
def compute(x,y):
    sum=0
    for i in range(x,y+1):
        sum+=i
    return sum

a=int(input())
b=int(input())
print(compute(a,b))

