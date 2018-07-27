# TODO: 按照敘述定義出兩個 Exception
class FallDownException(Exception):
    def __init__(self,floor):
        self.floor=floor
    def __str__(self):
        return ("在 {} 樓被接住了！".format(self.floor))
class FallDownStrongerException(Exception):
    def __init__(self,floor):
        self.floor=floor
    def __str__(self):
        return ("在 {} 樓被接住了！".format(self.floor))  

def slip(floor):
    try:
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))

            if floor == 80:
                # TODO: 要 raise 一個 exception
                raise FallDownException(floor)

    #except '''TODO: 要用一個 exception 接''' as e:
     except FallDownException as e:
        print(e)
        print("突破機關！")
        while floor:
            floor -= 1
            print("現在在 {} 樓".format(floor))
            
            if floor == 5:
                # TODO: 要 raise 一個 exception
                raise FallDownStrongerException(floor)

# TODO: 用 try...except 把 slip(106) 包起來
try:
    slip(106)
except FallDownStrongerException as e:
    print(e)
    print("安全!")

#輸出
#現在在 105 樓
#現在在 104 樓
#....（略）
#在 80 樓被接住了！
#突破機關！
#....（略）
#現在在 5 樓
#在 5 樓被接住了！
#安全！
