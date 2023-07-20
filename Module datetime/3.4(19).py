# программа, выводящая даты подготовки задач (в виде арифметичесокй прогрессии)
from datetime import datetime, timedelta
start_date = datetime.strptime(input(), '%d.%m.%Y')

for i in range(1, 11):
    print(start_date.strftime('%d.%m.%Y'))
    start_date += timedelta(days=i+1)
