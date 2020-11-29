dict1={}
while 1:
    Key=input("Key:")
    if Key=="end":
        break
    else:
        Value=input("Value:")
        dict1[Key]=Value
word=input("Search key:")
if word not in dict1.keys(): #如果是要查詢KEY 在變數後面.keys()
    print("False")
else:
    print("True")
# print(dict1)
