N=[]
for i in range(9): N.append(int(input()))

maxN=max(N)
maxIndex=N.index(maxN) #最大的數字在索引第幾個
print(maxIndex) #印出來了解一下
print("Index of the largest number {} is: ({}, {})"
        .format(maxN,maxIndex//3,maxIndex%3))


minN=min(N)
minIndex=N.index(minN) #最小的數字在索引第幾個
print(minIndex) #印出來了解一下
print("Index of the smallest number {} is: ({}, {})"
        .format(minN,minIndex//3,minIndex%3))

#不太明白這個題目的意思，提到3*3矩陣，所以這邊使用//3 & %3