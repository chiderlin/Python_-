
grade=[[0 for i in range(5)] for j in range(3) ] #先建一個二維度list
print(grade)
a=["1st","2nd","3rd"]
for i in range(3):
    print("The {} student:".format(a[i])) #要先建好list在這邊才能直接讀取list取得想要的字
    for j in range(5): grade[i][j]=int(input()) #這邊再輸入數值取代原本的0
for i in range(3): #分開來寫才能在最後 一次印出來三個學生的成績
    total=sum(grade[i]) #grade[i]用法讀取裡面數值做計算需熟悉一點
    print("Student {}".format(i+1))
    print("#Sum {}".format(total))
    print("#Average {:.2f}".format(total/5))