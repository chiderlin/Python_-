def compute(row, cols):
    for i in range(rows):
        for j in range(cols):
            print("%4d"%(j-i),end="") #4欄寬 和以下用法一樣 試試%用法
            # print("{:4d}".format(j-i),end="")
        print()

rows, cols=int(input()),int(input())
compute(rows,cols)