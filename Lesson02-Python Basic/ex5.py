while a < 50 :
    b = 1
    c = 0
    while b < a :
        if (a % b) == 0 :
            c = c + 1
        b = b + 1

    if c <= 1:
        print(a)
        
    a = a +1