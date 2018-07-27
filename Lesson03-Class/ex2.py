class Life :
    def set_map(self , n_arg) :
        self.n = n_arg
        self.map =[ ['*' for x in range(n_arg)] for x in range(n_arg)]

    def set_pattern(self , p_arg) :
        if p_arg == 1 :
            self.map[int((self.n-1)/2)-1][int((self.n-1)/2)] = '0'
            self.map[int((self.n-1)/2)-1][int((self.n-1)/2)+1] = '0'
            self.map[int((self.n-1)/2)-1][int((self.n-1)/2)-1] = '0'
            self.map[int((self.n-1)/2)][int((self.n-1)/2)-1] = '0'
            self.map[int((self.n-1)/2)+1][int((self.n-1)/2)] = '0'

    def display(self):
        for x in range(self.n) :
            for y in range(self.n) :
                print(self.map[x][y] , end='')
            print()
            
my_map = Life()
my_map.set_map(9)
my_map.set_pattern(1)
my_map.display()
