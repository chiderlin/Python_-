L=[]
for i in range(4):
    print("Week {}:".format(i+1))
    for j in range(3):
        temp=eval(input("Day {}:".format(j+1)))
        L.append(temp)
    # print(L)
print("Average: {:.2f}".format(sum(L)/len(L)))
print("Highest: ",max(L))
print("Lowest: ",min(L))
    