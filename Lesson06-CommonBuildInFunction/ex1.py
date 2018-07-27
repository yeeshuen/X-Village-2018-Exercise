def eight_queens(queen_list):
    FLAG_A = False
    a = 0

    slope_minus_plus = [[0 , 0] for i in range(8)]
    slope_minus_minus = [[0 , 0] for i in range(8)]
    slope_plus_minus = [[0 , 0] for i in range(8)]
    slope_plus_plus = [[0 , 0] for i in range(8)]
    
    while a <= 7 :
        b = a + 1         
        while b <= 6 :
            if queen_list[a][1] == queen_list[b][1] or queen_list[a][0]==queen_list[b][0] :
                print("False")
                FLAG_A = True
                print("haha")
                break
            
            for i in range(8) :
                slope_minus_minus[i] = [queen_list[a][0] - i - 1 , queen_list[a][1] - i - 1]
                slope_plus_plus[i] = [queen_list[a][0] + i + 1 , queen_list[a][1] + i + 1]
                slope_minus_plus[i] =  [queen_list[a][0] - i - 1 , queen_list[a][1] + i + 1]
                slope_plus_minus[i] = [queen_list[a][0] + i + 1 , queen_list[a][1] - i - 1]

                if slope_minus_minus[i] == queen_list[b] or slope_minus_plus[i] == queen_list[b] or slope_plus_minus[i] == queen_list[b] or slope_plus_plus[i] == queen_list[b] :
                    print("False")
                    FLAG_A = True
                    break
            
            if FLAG_A :
                break

            b = b + 1  

        if FLAG_A :
            break
                    
        a = a + 1
    
    if FLAG_A==False :
        print("True")
   
    

eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [0, 1]])
#eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])