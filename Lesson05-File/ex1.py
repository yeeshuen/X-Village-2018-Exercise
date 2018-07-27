#寫一個程式，輸入日期、事件、心得，將輸入文字寫入檔案 note.txt。

date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')

# wrtie a file 'note.txt'
f = open('note.txt', 'w')

f.write(date)
f.write(event)
f.write(description)
f.close()