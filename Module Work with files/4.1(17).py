# программа, определяющая, в каком порядке расположены даты в последовательности
import sys
from datetime import datetime
dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin.readlines()]
counter_asc = 0
counter_desc = 0

for i in range(len(dates) - 1):
    if dates[i] < dates[i + 1]:
        counter_asc += 1
    elif dates[i] > dates[i + 1]:
        counter_desc += 1

if counter_asc == len(dates) - 1:
    print('ASC')
elif counter_desc == len(dates) - 1:
    print('DESC')
else:
     print('MIX')