# программа, выводящая количество минут до окончания работы магазина
from datetime import datetime
user_string = input().split()
current_date = datetime.strptime(user_string[0], '%d.%m.%Y')
current_time = datetime.strptime(user_string[1], '%H:%M')
data = {(0, 1, 2, 3, 4): ('9:00', '21:00'),
        (5, 6): ('10:00', '18:00')}

for elem in data:
    if current_date.weekday() in elem:
        work_hours = data[elem]


start_work = datetime.strptime(work_hours[0], '%H:%M')
finish_work = datetime.strptime(work_hours[1], '%H:%M')

if start_work <= current_time < finish_work:
    print((finish_work - current_time).seconds // 60)
else:
    print('Магазин не работает')
