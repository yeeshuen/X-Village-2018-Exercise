A = [45 , 14 , "A"]
B = [96 , 13 , "B"]
C = [85 , 22 , "C"]

def SALARY(WORKER) :
    salary = 0
    if WORKER[0] > 90 :
        salary = salary + 8000
    elif 70 < WORKER[0] <= 90 :
        salary = salary + 6000
    else :
        salary = salary + 4000

    print("員工" , WORKER[2] , "績效評級為:" , WORKER[0] , "加班時數" , WORKER[1] , "小時" , "->月薪" , (salary + WORKER[1] *200) , "元" )

    return 0
mixed = [A , B ,C]

SALARY(A)
SALARY(B)
SALARY(C)