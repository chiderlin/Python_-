
money=int(input())
rate=eval(input())/100
month=eval(input())

print("Month\tAmount")
for i in range(1,month+1):
    
    total=money+(money*rate)/12
    money=total
    print(" {}\t{:.2f}".format(i,total))
    