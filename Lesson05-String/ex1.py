# 99multi.py

RANGE1 = [1, 3]
RANGE2 = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]

for i in range(RANGE1[0], RANGE1[1] + 1):
    for j in range(RANGE2[0], RANGE2[1] + 1):
        for k in calc(i, j):
            print(str(i) + k['sign'] + str(j) + '=' + str(k['result']), end="|")
    print()

    
RANGE1 = [1, 3]
RANGE2 = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]

for i in range(RANGE1[0], RANGE1[1] + 1):
    for j in range(RANGE2[0], RANGE2[1] + 1):
        for k in calc(i, j):
            s = '{:>2}{}{:>2}={:>2}'.format(str(i), k['sign'], str(j), str(k['result']))
            print(s, end="|")
    print()

#before

#1*1=1|1*2=2|1*3=3|1*4=4|1*5=5|1*6=6|1*7=7|1*8=8|1*9=9|
#2*1=2|2*2=4|2*3=6|2*4=8|2*5=10|2*6=12|2*7=14|2*8=16|2*9=18|
#3*1=3|3*2=6|3*3=9|3*4=12|3*5=15|3*6=18|3*7=21|3*8=24|3*9=27|

#after
 #1* 1= 1| 1* 2= 2| 1* 3= 3| 1* 4= 4| 1* 5= 5| 1* 6= 6| 1* 7= 7| 1* 8= 8| 1* 9= 9|
 #2* 1= 2| 2* 2= 4| 2* 3= 6| 2* 4= 8| 2* 5=10| 2* 6=12| 2* 7=14| 2* 8=16| 2* 9=18|
 #3* 1= 3| 3* 2= 6| 3* 3= 9| 3* 4=12| 3* 5=15| 3* 6=18| 3* 7=21| 3* 8=24| 3* 9=27|