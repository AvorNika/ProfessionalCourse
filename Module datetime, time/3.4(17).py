# программа, выводящая время через n секунд от вводимого
from datetime import timedelta, datetime
my_time = datetime.strptime(input(), '%H:%M:%S')
n = int(input())
result = my_time + timedelta(seconds=n)
print(result.time())
