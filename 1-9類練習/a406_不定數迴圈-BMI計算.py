
while 1:
    h=int(input())
    if h==-9999:
        break
    w=int(input())
    if w==-9999:
        break
    bmi=w/((h/100)**2)
    if bmi<18.5:
        m="under weight"
    elif 18.5<=bmi<25:
        m="normal"
    elif 25<=bmi<30:
        m="over weight"
    elif 30<=bmi:
        m="fat"
    print("BMI: {:.2f}".format(bmi))
    print("State: {}".format(m))