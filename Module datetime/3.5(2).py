# программа, вычисляющая количество пятниц 13, приходящихся на каждый день недели
from datetime import datetime
start = datetime(year=1, month=1, day=1).toordinal()
finish = datetime(year=9999, month=12, day=31).toordinal()
result = {0: 0, 1: 0, 2: 0,
          3: 0, 4: 0, 5: 0,
          6: 0}

for day in range(start, finish + 1):
    if datetime.fromordinal(day).day == 13:
        result[datetime.fromordinal(day).weekday()] += 1

for value in result.values():
    print(value)
