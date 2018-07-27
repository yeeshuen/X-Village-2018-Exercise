import random

'''
TODO: define exception classes
'''
class HungryException(Exception):
    def __init__(self,hunger):
        self.hunger=hunger
    def __str__(self):
        return ("I'm hungry (status: {}), need to eat!".format(self.hunger))

class ThirstyException(Exception):
    def __init__(self,water):
        self.water=water
    def __str__(self):
        return ("I'm thirsty (status: {}), need to drink!".format(self.water))

class BoredException(Exception):
    def __init__(self,mood):
        self.mood=mood
    def __str__(self):
        return ("I'm boring (status: {}), need to play!".format(self.mood))
print('='*30)
def check(man):
    # TODO: in what condition need to raise exception?
    if man["hunger"]<=0:
        raise HungryException(man["hunger"])
    elif man["water"]<=0:
        raise ThirstyException(man["water"])
    elif man["mood"]<=0:
        raise BoredException(man["mood"])

def play(man):
    print("playing...")
    man["hunger"] -= 15
    man["water"] -= 15
    man["mood"] += 5
    check(man)
def eat(man):
    print("eating...")
    man["hunger"] += 5
    check(man)
def drink(man):
    print("drinking...")
    man["water"] += 5
    check(man)
    
actionList = [play, eat, drink]
    
child = {"hunger": 20, "water": 20, "mood": 20}

while True:
    
    rand = random.randint(0,2)
    print("status",child["hunger"],child["water"],child["mood"])
    # TODO: 把隨機的動作用 try...except 包起來   
    
    try:
        actionList[rand](child)
    except HungryException as e:
        print(e)
        break
    except ThirstyException as e:
        print(e)
        break
    except BoredException as e:
        print(e)
        break
    

    # TIPS: 記得只要抓到 exception 之後就要 break 了，不然會造成無窮迴圈 