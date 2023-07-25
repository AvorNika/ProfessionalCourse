# программа, выводящая количество секунд, прошедших с начала чуток
from datetime import timedelta
my_hours, my_minutes, my_seconds = [int(i) for i in input().split(':')]
my_time = timedelta(hours=my_hours, minutes=my_minutes, seconds=my_seconds)
print(int(my_time.total_seconds()))

