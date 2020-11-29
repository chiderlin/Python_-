s=0
N=[]
for i in range(12):
    N.append(int(input()))

for index in range(12):
    if index%2==0:
        s+=N[index]
    print("{:3d}".format(N[index]),end="")
    if index%3==2:
        print()
print(s)
