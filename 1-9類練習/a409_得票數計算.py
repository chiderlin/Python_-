

nami=0
cho=0
null=0

for i in range(5):
    n=int(input())
    if n==1:
        nami+=1
    elif n==2:
        cho+=1
    else:
        null+=1
    print("Total votes of No.1: Nami =  {}".format(nami))
    print("Total votes of No.2: Chopper =  {}".format(cho))
    print("Total null votes =  {}".format(null))

if nami > cho:
    print("=> No.1 Nami wins the election.")
elif nami < cho:
    print("=> No.2 Chopper wins the election.")
else:
    print("No one wins the election.")
    

