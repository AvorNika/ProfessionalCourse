# программа, выводящая количество дней между соседними датами в списке
from datetime import datetime, timedelta
dates = [datetime.strptime(i, '%d.%m.%Y') for i in input().split()]
days = []
for i in range(len(dates) - 1):
    days.append(abs(dates[i] - dates[i + 1]).days)

print(days)
