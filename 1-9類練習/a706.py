
count=eval(input())
eng=26
for i in range(count):
    sentence = input()
    set1=set(sentence.lower())
    if len(set1)>=eng:
        print("True")
    else:
        print("False")