#更改ex1.py的程式碼讓程式可以正常運作

def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))
    
for i in range(5, -1, -1):
    for j in range(5, 0, -1):
        div(i, j)
  
