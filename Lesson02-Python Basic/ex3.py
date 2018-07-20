#課堂練習 - 終極密碼 (計分)
#說明：隨機產生一個1~100整數的答案(已寫好)，寫一個可以一直猜答案的小程式，若猜的答案太小輸出"Too small"，若猜的答案太大輸出"Too big"，猜對答案輸出"Correct"，程式才結束。¶
import random

question = random.randint(1,100)
Flag = True

while Flag:
    ans = int(input("number between 1 and 100"))
    if question == ans:
        print('so clever')
        Flag = False
    elif ans < question:
        print('too small try again')
    else :
        print('too big are you crazy')
