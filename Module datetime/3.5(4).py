# программа, выводящая каждую третью дату, соответствующую условиюЖ
# это не ПН, не ЧТ, а сумма дня и месяца нечётная
from datetime import datetime
start = datetime.strptime(input(), '%d.%m.%Y')
finish = datetime.strptime(input(), '%d.%m.%Y')

i = 0
while (start.day + start.month) % 2 != 1:
    i += 1
    start = datetime.fromordinal(start.toordinal() + 1)
else:
    for i in range(start.toordinal(), finish.toordinal() + 1, 3):
        current_date = datetime.fromordinal(i)
        if current_date.weekday() != 0 and current_date.weekday() != 3:
            print(current_date.strftime('%d.%m.%Y'))
