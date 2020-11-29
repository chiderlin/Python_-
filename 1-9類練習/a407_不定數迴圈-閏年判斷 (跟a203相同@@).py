
while 1:
    n=int(input())
    if n==-9999:
        break
    elif n%4==0 and n%100!=0:
        w="{} is a leap year.".format(n)
    elif n%400==0:
        w="{} is a leap year.".format(n)
    else:
        w="{} is not a leap year.".format(n)
    print(w)
