class Calculator:
    def __init__(self,name,number,stock,price):
         self.n=name #.n是自己定義 name不用一定要是name
         self.num=number
         self.stock=stock
         self.price=price
    def profit(self,cost):
        self.cost=cost
        profit=self.price-self.cost
        print("售價:${},成本:${}".format(c.price,c.cost))
        return (profit*self.stock)
    
c=Calculator("water","itemNo.11",10,50)
money=c.profit(20)

print("{}獲利:${}".format(c.n,money))

#class其實就是依類別自己定義自己玩 很好玩的一個東西 