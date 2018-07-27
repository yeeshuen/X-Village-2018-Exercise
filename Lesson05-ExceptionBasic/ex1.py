def div(dividend, divisor):
    print("The answer is {}".format(dividend/divisor))

for i in range(5, -1, -1):
    for j in range(5, -1, -1):
        div(i, j)

# 出現了error 
# 在line6 div(i,j) 和 line2 (div) print("The answer is {}".format(dividend/divisor))
# ZerodivisionError:division by zero  (除零錯誤)
#Traceback是回溯的意思也就是找到一個錯誤發生的地方，
# 在第幾行的那個模塊中，這裡我們返回的錯誤名稱是ZeroDivisionError除零錯誤。
