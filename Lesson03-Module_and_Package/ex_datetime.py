#datetime套件
import datetime

def print_next_day():
    time_now = datetime.datetime.now()
    time = str(time_now + datetime.timedelta(days=1))
    print(time[0:11])

print_next_day()