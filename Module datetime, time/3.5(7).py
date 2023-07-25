# программа, определяющая самого молодого сотрудника, празднующего свой ДР в ближайшие 7 дней
from datetime import datetime, timedelta

current_date = datetime.strptime(input(), '%d.%m.%Y')
n = int(input())
info = [input().split() for _ in range(n)]

finish_date = current_date + timedelta(days=7)

birthday_emp = []
for elem in info:
    birthday = datetime.strptime(elem[2], '%d.%m.%Y')
    if current_date < birthday.replace(year=finish_date.year) <= finish_date:
        birthday_emp.append((elem[0], elem[1], birthday))

birthday_emp.sort(key=lambda x: x[2], reverse=True)

if birthday_emp:
    print(birthday_emp[0][0], birthday_emp[0][1])
else:
    print('Дни рождения не планируются')
