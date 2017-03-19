import datetime

#should try doing a mergesort instead. Easier to conceive

class Entry:
    def __init__(self,price,qty,time,side):
        self.price = price
        self.qty = qty
        self.time = time
        self.side = side

def partition(orders,left,right,pivot):
    while(left <= right):
        while(orders[left].price < pivot.price):
            left+=1
        while(orders[right].price > pivot.price):
            right-=1
            
        if(left <= right):
            orders[left], orders[right] = orders[right],orders[left]
            left+=1
            right-=1

    return left

def price_time_sort(orders,left,right):
    if (left >= right):
        return

    pivot = orders[(left + right) // 2]
    index = partition(orders,left,right,pivot)
    price_time_sort(orders,left,index-1)
    price_time_sort(orders,index,right)

        

s1 = Entry(20.30,200,datetime.time(9,5),"SELL")
s2 = Entry(20.30,100,datetime.time(9,1),"SELL")
s3 = Entry(20.25,100,datetime.time(9,3), "SELL")
b1 = Entry(20.20,200,datetime.time(9,8),"BUY")
b2 = Entry(20.15,100,datetime.time(9,6),"BUY")
b3 = Entry(20.15,200,datetime.time(9,9),"BUY")

sell_orders = [s3,s2,s1]
buy_orders = [b3,b2,b1]

price_time_sort(sell_orders,0,len(sell_orders)-1)
price_time_sort(buy_orders,0,len(buy_orders)-1)

print("sell orders: ")
sell_sorted = ""

for a in sell_orders:
    sell_sorted += str(a.price) + " "
print(sell_sorted)

print("buy orders: ")
buy_sorted =""

for b in buy_orders:
    buy_sorted += str(b.price) + " "
print(buy_sorted)
