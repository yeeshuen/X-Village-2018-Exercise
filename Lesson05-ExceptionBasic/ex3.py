#寫一個 function，function 需要 raise exception

#呼叫 function 的時候需要用 try...except 包起來

def function(m):
    if m==0:
        raise ValueError("divisor cannot be zero!")

try:
    function(0)
except ValueError as e:
    print(e)
else:
    print("okay.good")

try:
    function(3)
except ValueError as e:
    print(e)
else:
    print("okay.good")
   