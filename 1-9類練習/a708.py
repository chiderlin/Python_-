dict1={}
for i in range(2):
    print("Create dict{}:".format(i+1))
    while 1:
        Key=input("Key:")
        if Key=="end":
            break
        Value=input("Value:")
        dict1[Key]=Value #這邊的Key跟Value是帶入外面的變數

for i in sorted(dict1.keys()): #對key值做排序
    print(i,": ",dict1[i]) #dict1[i]的value
