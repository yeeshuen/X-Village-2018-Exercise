#小明買醬油

import random
item_in_shop = {"soybean_sauce": 0, "milk": 4, "salt": 10, "soybean_milk": 3}
items = [item for item in item_in_shop.keys()]
cnt = 5

def buy(item):
    # TODO: 補上程式碼和完成邏輯
    # tips: 如果東西數量是 0 需要 raise Exception,否則就把物品的數量減 1
    if item_in_shop[item]==0:
        raise Exception('You need to buy something for your mom!')
    else:
        item_in_shop[item]=item_in_shop[item]-1
        print("Mommy! I've bought {} for you!".format(item))

# 買五個隨機的東西
while cnt:
    cnt -= 1
    index = random.randint(0,3)
    item = items[index]
    try:
        buy(item)
    except Exception as x:
        print(x)
        cnt=cnt+1
    # 想要買的東西是 item，利用 buy() 來買東西
    # TODO: 補上程式碼
    # tips: 記得用 try...except 包起來
 