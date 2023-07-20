# программа, составляющая расписание занятий (45 мин занятие, 10 мин перерыв)
from datetime import datetime, timedelta
time_start = datetime.strptime(input(), '%H:%M')
time_finish = datetime.strptime(input(), '%H:%M')
result = []
classes = (time_finish - time_start) // timedelta(minutes=45)
if classes > 0:
    for _ in range(classes):
        finish_class = time_start + timedelta(minutes=45)
        if finish_class <= time_finish:
            result.append([time_start.strftime('%H:%M') + ' - ' + finish_class.strftime('%H:%M')])
            time_start = finish_class + timedelta(minutes=10)
        else:
            break
    for res in result:
        print(*res)

