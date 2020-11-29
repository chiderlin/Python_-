


n=input().split(" ")
total=0
for i in range(len(n)):
    total+=int(n[i])
print("Total = {}".format(total))
print("Average = {}".format(total/len(n)))